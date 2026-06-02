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
# LANGUAGE STRINGS
# ==========================================
STRINGS = {
    "en": {
        "title":               " Telegram Forwarder ",
        "last_id":             "Last forwarded ID",
        "tracked":             "Tracked messages",
        "ignore_duplicates":   "Ignore media already forwarded by the script? (y/n): ",
        "ignore_input":        "y",
        "resume_prompt":       "Continue from where script stopped? (y/n): ",
        "resume_input":        "y",
        "watch_prompt":        "Enable watch mode? Script will keep checking for new messages. (y/n): ",
        "watch_interval":      "Check interval in minutes (e.g. 5): ",
        "watch_max_hours":     "Maximum runtime in hours (0 = no limit): ",
        "watch_active":        "Watch Mode Active",
        "watch_checking":      "Checking for new messages...",
        "watch_none":          "No new messages. Waiting",
        "watch_found":         "New messages found. Forwarding...",
        "watch_timeout":       "Maximum runtime reached. Stopping.",
        "watch_minutes":       "minutes",
        "resume_mode":         "Resume Mode",
        "resume_detail":       "Starting after ID",
        "full_mode":           "Full Mode",
        "full_detail":         "Reading all messages",
        "processing":          "Processing message ID",
        "skipped":             "Skipped",
        "already_forwarded":   "Already Forwarded",
        "forwarding":          "Forwarding",
        "message":             "Message",
        "sent":                "Sent",
        "sleeping":            "Sleeping",
        "delay":               "Delay",
        "paused":              "Paused",
        "long_break":          "Long Break",
        "floodwait":           "FloodWait",
        "tg_limit":            "Telegram Limit",
        "waiting":             "Waiting",
        "error":               "Error",
        "forward_failed":      "Forward Failed",
        "error_delay":         "Error Delay",
        "runtime":             "Runtime",
        "avg":                 "Avg",
        "finished":            " FORWARD FINISHED ",
        "total_sent":          "Total sent",
        "total_runtime":       "Total runtime",
        "no_messages":         "--No new messages.--",
        "seconds":             "seconds",
        "warn_full_no_filter": "⚠️  Full mode without duplicate filter enabled.",
        "warn_full_detail":    "All messages will be re-forwarded, including already sent ones.",
        "warn_confirm":        "Confirm? (y/n): ",
        "cancelled":           "Operation cancelled.",
        "restart_prompt":      "Run again with new options? (y/n): ",
    },
    "pt": {
        "title":               " Telegram Forwarder ",
        "last_id":             "Último ID encaminhado",
        "tracked":             "Mensagens rastreadas",
        "ignore_duplicates":   "Ignorar mídias já encaminhadas pelo script? (s/n): ",
        "ignore_input":        "s",
        "resume_prompt":       "Continuar de onde o script parou? (s/n): ",
        "resume_input":        "s",
        "watch_prompt":        "Ativar modo watch? O script ficará verificando novas mensagens. (s/n): ",
        "watch_interval":      "Intervalo de verificação em minutos (ex: 5): ",
        "watch_max_hours":     "Tempo máximo de execução em horas (0 = sem limite): ",
        "watch_active":        "Modo Watch Ativo",
        "watch_checking":      "Verificando novas mensagens...",
        "watch_none":          "Sem novas mensagens. Aguardando",
        "watch_found":         "Novas mensagens encontradas. Encaminhando...",
        "watch_timeout":       "Tempo máximo atingido. Encerrando.",
        "watch_minutes":       "minutos",
        "resume_mode":         "Modo Continuação",
        "resume_detail":       "Iniciando após o ID",
        "full_mode":           "Modo Completo",
        "full_detail":         "Lendo todas as mensagens",
        "processing":          "Processando mensagem ID",
        "skipped":             "Ignorado",
        "already_forwarded":   "Já Encaminhada",
        "forwarding":          "Encaminhando",
        "message":             "Mensagem",
        "sent":                "Enviado",
        "sleeping":            "Aguardando",
        "delay":               "Intervalo",
        "paused":              "Pausado",
        "long_break":          "Pausa Longa",
        "floodwait":           "FloodWait",
        "tg_limit":            "Limite do Telegram",
        "waiting":             "Aguardando",
        "error":               "Erro",
        "forward_failed":      "Falha no Encaminhamento",
        "error_delay":         "Atraso por Erro",
        "runtime":             "Tempo rodando",
        "avg":                 "Média",
        "finished":            " ENCAMINHAMENTO FINALIZADO ",
        "total_sent":          "Total enviado",
        "total_runtime":       "Tempo total",
        "no_messages":         "--Sem novas mensagens.--",
        "seconds":             "segundos",
        "warn_full_no_filter": "⚠️  Modo completo sem filtro de duplicatas ativado.",
        "warn_full_detail":    "Todas as mensagens serão reencaminhadas, incluindo as já enviadas.",
        "warn_confirm":        "Confirmar? (s/n): ",
        "cancelled":           "Operação cancelada.",
        "restart_prompt":      "Executar novamente com novas opções? (s/n): ",
    }
}


# ==========================================
# LANGUAGE SELECTION
# ==========================================
def select_language():
    print("\n============================")
    print(" Telegram Forwarder Enhanced ")
    print("---by Wagg13---") 
    print("============================")
    print("\n[1] English")
    print("[2] Português (BR)")
    choice = input("\nSelect language / Selecione o idioma: ").strip()
    return "pt" if choice == "2" else "en"


# ==========================================
# LOG SYSTEM
# ==========================================
def log_message(s, action, message_type, details=""):
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
            "last_forwarded_id": 0,
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
# FORWARD LOOP
# ==========================================
def forward_messages(client, s, state, forwarded_messages, script_start_time):
    """Encaminha mensagens a partir do último ID salvo. Retorna total enviado."""

    last_forwarded_id = state.get("last_forwarded_id", 0)
    amount_sent = 0

    messages = client.iter_messages(
        BOT_SETTING.SOURCE_CHAT_ID,
        min_id=last_forwarded_id,
        reverse=True
    )

    for message in messages:

        try:
            if isinstance(message, MessageService):
                continue

            print(f"\n{s['processing']}: {message.id}")

            if not message.message and not message.media:
                continue

            if message.id in forwarded_messages:
                log_message(s, s["skipped"], s["already_forwarded"], f"ID: {message.id}")
                continue

            log_message(s, s["forwarding"], s["message"], f"ID: {message.id}")

            client.forward_messages(
                BOT_SETTING.DESTINATION_CHAT_ID,
                message
            )

            log_message(s, s["sent"], s["message"], f"ID: {message.id}")

            forwarded_messages.add(message.id)
            state["last_forwarded_id"] = message.id
            state["forwarded_messages"] = list(forwarded_messages)

            amount_sent += 1

            if amount_sent % 10 == 0:
                save_state(state)

            elapsed_time = get_elapsed_time(script_start_time)
            elapsed_seconds = time.time() - script_start_time
            rate = (amount_sent / elapsed_seconds * 60) if elapsed_seconds > 0 else 0

            print(
                f"\n{s['runtime']}: {elapsed_time} | "
                f"{s['sent']}: {amount_sent} | "
                f"{s['avg']}: {rate:.1f}/min"
            )

            delay = random.uniform(4, 9) if has_media(message) else random.uniform(2, 5)
            log_message(s, s["sleeping"], s["delay"], f"{delay:.2f} {s['seconds']}")
            time.sleep(delay)

            if amount_sent % 20 == 0:
                long_break = random.uniform(20, 45)
                log_message(s, s["paused"], s["long_break"], f"{long_break:.2f} {s['seconds']}")
                time.sleep(long_break)

        except FloodWaitError as e:
            save_state(state)
            wait_time = e.seconds + random.randint(10, 25)
            log_message(s, s["floodwait"], s["tg_limit"], f"{s['waiting']} {wait_time} {s['seconds']}")
            time.sleep(wait_time)

        except Exception as e:
            save_state(state)
            log_message(s, s["error"], s["forward_failed"], str(e))
            error_wait = random.uniform(15, 30)
            log_message(s, s["sleeping"], s["error_delay"], f"{error_wait:.2f} {s['seconds']}")
            time.sleep(error_wait)

    return amount_sent


# ==========================================
# RUN
# ==========================================
def run(client, s):

    state = load_state()
    forwarded_messages = set(state.get("forwarded_messages", []))
    last_forwarded_id = state.get("last_forwarded_id", 0)

    print("\n============================")
    print(s["title"])
    print("============================\n")
    print(f"{s['last_id']}: {last_forwarded_id}")
    print(f"{s['tracked']}: {len(forwarded_messages)}\n")

    # ==========================================
    # DUPLICATE MEDIA CHECK OPTION
    # ==========================================
    ignore_duplicates = (
        input(s["ignore_duplicates"])
        .strip()
        .lower()
        == s["ignore_input"]
    )

    # No modo watch, duplicatas são sempre ignoradas por design.
    # A pergunta abaixo só aparece se watch estiver desativado.

    # ==========================================
    # WATCH MODE OPTION
    # ==========================================
    watch_mode = (
        input(s["watch_prompt"])
        .strip()
        .lower()
        == s["ignore_input"]
    )

    watch_interval = 5
    max_hours = 0

    if watch_mode:
        try:
            watch_interval = max(1, int(input(s["watch_interval"]).strip()))
        except ValueError:
            watch_interval = 5

        try:
            max_hours = max(0, float(input(s["watch_max_hours"]).strip()))
        except ValueError:
            max_hours = 0

    # ==========================================
    # RESUME OPTION (apenas sem watch)
    # ==========================================
    if not watch_mode:
        resume_mode = (
            input(s["resume_prompt"])
            .strip()
            .lower()
            == s["resume_input"]
        )

        if not ignore_duplicates and not resume_mode:
            print(f"\n{s['warn_full_no_filter']}")
            print(s["warn_full_detail"])
            confirm = input(s["warn_confirm"]).strip().lower()
            if confirm != s["ignore_input"]:
                print(s["cancelled"])
                return

        if not resume_mode:
            state["last_forwarded_id"] = 0
            forwarded_messages = set()
            state["forwarded_messages"] = []

    script_start_time = time.time()
    total_sent = 0

    # ==========================================
    # WATCH MODE LOOP
    # ==========================================
    if watch_mode:
        max_seconds = max_hours * 3600 if max_hours > 0 else None
        log_message(s, "Info", s["watch_active"], "")

        while True:

            # Verifica timeout
            if max_seconds and (time.time() - script_start_time) >= max_seconds:
                log_message(s, "Info", s["watch_timeout"], "")
                break

            log_message(s, "Info", s["watch_checking"], "")

            sent = forward_messages(client, s, state, forwarded_messages, script_start_time)
            total_sent += sent

            if sent > 0:
                log_message(s, "Info", s["watch_found"], f"+{sent}")
            else:
                log_message(
                    s, "Info", s["watch_none"],
                    f"{watch_interval} {s['watch_minutes']}"
                )

            # Aguarda intervalo, verificando timeout a cada segundo
            for _ in range(watch_interval * 60):
                if max_seconds and (time.time() - script_start_time) >= max_seconds:
                    break
                time.sleep(1)

    # ==========================================
    # NORMAL MODE
    # ==========================================
    else:
        log_message(s, "Info", s["full_mode"] if state["last_forwarded_id"] == 0 else s["resume_mode"], "")
        total_sent = forward_messages(client, s, state, forwarded_messages, script_start_time)

    # ==========================================
    # FINAL SUMMARY
    # ==========================================
    save_state(state)
    final_runtime = get_elapsed_time(script_start_time)

    print("\n============================")
    print(s["finished"])
    print("============================")
    print(f"{s['total_sent']}: {total_sent}")
    print(f"{s['total_runtime']}: {final_runtime}")

    if total_sent == 0:
        print(s["no_messages"])

    print("============================\n")


# ==========================================
# MAIN
# ==========================================
lang = select_language()
s = STRINGS[lang]

with TelegramClient(
    BOT_SETTING.NAME,
    BOT_SETTING.API_ID,
    BOT_SETTING.API_HASH
) as client:

    while True:
        run(client, s)

        restart = input(s["restart_prompt"]).strip().lower()
        if restart != s["ignore_input"]:
            break