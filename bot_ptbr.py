# Telegram Forwarder com Resume + Detecção de Duplicados
# + Runtime Timer + Média de envio

import json
import os
import random
import time
from datetime import datetime

from telethon.sync import TelegramClient
from telethon.tl.types import MessageService
from telethon.errors import FloodWaitError

from config import Config as BOT_SETTING


STATE_FILE = "forward_state.json"


# ==========================================
# LOG SYSTEM
# ==========================================
def log_message(action, message_type, details=""):
    print(
        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
        f"{action}: {message_type} {details}"
    )


# ==========================================
# EXECUTION TIMER
# ==========================================
def get_elapsed_time(start_time):

    elapsed = int(time.time() - start_time)

    hours, remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"


# ==========================================
# LOAD STATE
# ==========================================
def load_state():

    if not os.path.exists(STATE_FILE):
        return {
            "last_forwarded_id": 2008,
            "forwarded_messages": []
        }

    try:

        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:

        return {
            "last_forwarded_id": 0,
            "forwarded_messages": []
        }


# ==========================================
# SAVE STATE
# ==========================================
def save_state(state):

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)


# ==========================================
# CHECK IF MESSAGE HAS MEDIA
# ==========================================
def has_media(message):
    return bool(message.media)


# ==========================================
# MAIN
# ==========================================
with TelegramClient(
    BOT_SETTING.NAME,
    BOT_SETTING.API_ID,
    BOT_SETTING.API_HASH
) as client:

    state = load_state()

    forwarded_messages = set(state.get("forwarded_messages", []))

    last_forwarded_id = state.get("last_forwarded_id", 2008)

    print("\n============================")
    print(" Telegram Forwarder Enhanced ")
    print("============================\n")

    print(f"Último ID encaminhado: {last_forwarded_id}")
    print(f"Mensagens rastreadas: {len(forwarded_messages)}\n")

    # ==========================================
    # DUPLICATE MEDIA CHECK OPTION
    # ==========================================
    ignore_duplicates = (
        input(
            "Ignorar mídias já encaminhadas pelo script? (s/n): "
        )
        .strip()
        .lower()
        == "s"
    )

    # ==========================================
    # RESUME OPTION
    # ==========================================
    resume_mode = (
        input(
            "Continuar de onde o script parou? (s/n): "
        )
        .strip()
        .lower()
        == "s"
    )

    # ==========================================
    # LOAD MESSAGES
    # ==========================================
    if resume_mode and last_forwarded_id > 0:

        log_message(
            "Info",
            "Modo Continuação",
            f"Iniciando após o ID {last_forwarded_id}"
        )

        messages = client.iter_messages(
            BOT_SETTING.SOURCE_CHAT_ID,
            min_id=last_forwarded_id,
            reverse=True
        )

    else:

        log_message(
            "Info",
            "Modo Completo",
            "Lendo todas as mensagens"
        )

        messages = client.iter_messages(
            BOT_SETTING.SOURCE_CHAT_ID,
            reverse=True
        )

    amount_sent = 0

    # ==========================================
    # START TIMER
    # ==========================================
    script_start_time = time.time()

    # ==========================================
    # PROCESS LOOP
    # ==========================================
    for message in messages:

        try:

            if isinstance(message, MessageService):
                continue

            print(f"\nProcessando mensagem ID:: {message.id}")

            # Ignore empty messages
            if not message.message and not message.media:
                continue

            # ==========================================
            # DUPLICATE CHECK
            # ==========================================
            if ignore_duplicates:

                if message.id in forwarded_messages:

                    log_message(
                        "Ignorado",
                        "Já Encaminhada",
                        f"ID: {message.id}"
                    )

                    continue

            # ==========================================
            # FORWARD MESSAGE
            # ==========================================
            log_message(
                "Encaminhando",
                "Mensagem",
                f"ID: {message.id}"
            )

            client.forward_messages(
                BOT_SETTING.DESTINATION_CHAT_ID,
                message
            )

            log_message(
                "Enviado",
                "Mensagem",
                f"ID: {message.id}"
            )

            # ==========================================
            # UPDATE STATE
            # ==========================================
            forwarded_messages.add(message.id)

            state["last_forwarded_id"] = message.id
            state["forwarded_messages"] = list(forwarded_messages)

            save_state(state)

            amount_sent += 1

            # ==========================================
            # RUNTIME STATUS
            # ==========================================
            elapsed_time = get_elapsed_time(script_start_time)

            elapsed_seconds = time.time() - script_start_time

            if elapsed_seconds > 0:
                rate = amount_sent / elapsed_seconds * 60
            else:
                rate = 0

            print(
                f"\nTempo rodando: {elapsed_time} | "
                f"Enviadas: {amount_sent} | "
                f"Média: {rate:.1f}/min"
            )

            # ==========================================
            # SMART HUMAN DELAYS
            # ==========================================
            if has_media(message):

                delay = random.uniform(4, 9)

            else:

                delay = random.uniform(2, 5)

            log_message(
                "Aguardando",
                "Intervalo",
                f"{delay:.2f} seconds"
            )

            time.sleep(delay)

            # ==========================================
            # LONG BREAKS
            # ==========================================
            if amount_sent % 20 == 0:

                long_break = random.uniform(20, 45)

                log_message(
                    "Pausado",
                    "Pausa Longa",
                    f"{long_break:.2f} seconds"
                )

                time.sleep(long_break)

        # ==========================================
        # FLOOD WAIT HANDLER
        # ==========================================
        except FloodWaitError as e:

            wait_time = e.seconds + random.randint(10, 25)

            log_message(
                "FloodWait",
                "Limite do Telegram",
                f"Aguardando {wait_time} seconds"
            )

            time.sleep(wait_time)

        # ==========================================
        # GENERAL ERRORS
        # ==========================================
        except Exception as e:

            log_message(
                "Erro",
                "Falha no Encaminhamento",
                str(e)
            )

            error_wait = random.uniform(15, 30)

            log_message(
                "Aguardando",
                "Atraso por Erro",
                f"{error_wait:.2f} seconds"
            )

            time.sleep(error_wait)

    # ==========================================
    # FINAL SUMMARY
    # ==========================================
    final_runtime = get_elapsed_time(script_start_time)

    print("\n============================")
    print(" ENCAMINHAMENTO FINALIZADO ")
    print("============================")
    print(f"Total enviado: {amount_sent}")
    print(f"Tempo total: {final_runtime}")

    if amount_sent == 0:
        print("--Sem novas mensagens.--")

    print("============================\n")