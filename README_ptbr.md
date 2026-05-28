<h1 align="center">
    <samp>Telegram Forwarder Enhanced</samp>
</h1>

![telegram-forwarder-enhanced](/images/feature.png)

<p align="center">
    <img alt="GitHub License" src="https://img.shields.io/github/license/Warnigo/telegram-chanal-copy?style=flat&label=license&labelColor=%23ffffff&color=%23454545">
</p>

## Sobre                     
[![Sobre](http://www.randomnoun.com/wpf/shell32-avi/tshell32_160.gif)](#)

Telegram Forwarder Enhanced é uma ferramenta simples e eficaz desenvolvida em Python com Telethon para copiar e encaminhar mensagens entre canais e grupos do Telegram de forma rápida, segura e automatizada.

O projeto suporta textos, imagens, vídeos e documentos, além de incluir recursos como retomada automática após interrupções, detecção de mensagens duplicadas e proteção contra [FloodWait](https://core.telegram.org/api/errors#420-flood) do Telegram.


## ✨ Funcionalidades

- 📋 Clona **canal ou grupo do Telegram** (público ou privado compatíveis).
- 🔄 É **necessário ser membro** do canal ou grupo para copiar o conteúdo.
- 🛠 Suporte a texto, imagens, PDFs e vídeos.
- ⏱ Fluxo de execução seguro com pausas aleatórias para evitar flood.
- 🆔 Listagem de IDs de mensagem evitando envio duplicado

## 🚀 Melhorias desta versão

- Correção de falhas no envio de mídia
- Retomada automática após interrupções
- Melhor tratamento de FloodWait
- Sistema anti-duplicação
- Melhor estabilidade no Telethon
- Compatibilidade com versões recentes

## 🤝 Créditos

Este projeto é um fork do repositório original [telegram-chanal-copy](https://github.com/warnigo/telegram-chanal-copy) criado por Warnigo. Agradecemos ao autor original por sua contribuição. Todos os direitos autorais originais são mantidos sob a licença MIT.

## Instalação

### 📂 Clonar o Repositório

```bash
git clone https://github.com/WaggBR/telegram-forwarder-enhanced.git

cd telegram-forwarder-enhanced
```

## 🛠 Configurações

### 1. Edite o arquivo [config.py](./config.py) antes de executar.

- `API_ID` e `API_HASH` - Obtenha estes valores em [my.telegram.org](http://my.telegram.org/)
- `PHONE_NUMBER` - Seu número de telefone com código do país (ex.: +55199999999)
- `NAME` - Nome que você escolher
- `SOURCE_CHAT_ID` e `DESTINATION_CHAT_ID` - IDs obtidos dos canais/grupos do Telegram.

### Como obter o `chat_id` de um canal ou grupo

Existem várias formas de obter o `chat_id` de um canal ou grupo. Aqui estão duas maneiras simples:

#### Usando: - Cliente Telegram [Kotatogram](https://kotatogram.github.io/download/):

- Abra o canal ou grupo
- Acesse a tela de descrição do canal/grupo
- Copie o `chat_id` exibido abaixo do nome do canal/grupo

#### Usando: - Bot Telegram [@username_to_id_bot](https://t.me/username_to_id_bot)

- Abra o bot e inicie ele
- Encaminhe qualquer mensagem do canal/grupo para o bot
- O bot responderá com o ID do remetente
- Copie o `chat_id` exatamente como exibido (incluindo o sinal de menos)

> [!NOTE]
> Canais e supergrupos do Telegram normalmente começam com `-100`.                             

#### Exemplo de `config.py`:

```python
class Config:
    API_ID = "12345678"                  # Seu API ID
    API_HASH = "seu_api_hash"            # Seu API Hash
    PHONE_NUMBER = "+5511999999999"      # Seu número com código do país
    NAME = "telegram-forwarder"          # Nome escolhido
    SOURCE_CHAT_ID = -1001234567890      # ID do canal/grupo origem
    DESTINATION_CHAT_ID = -1009876543210 # ID do canal/grupo destino
```


>[!NOTE]
>Certifique-se de substituir os espaços reservados pelas suas credenciais reais.


## 🐍 Configuração de ambiente virtual

É altamente recomendável o uso de um ambiente virtual para evitar conflitos de dependência.

- #### Windows

```sh
python -m venv myenv
```

- #### macOS e Linux

```sh
python3 -m venv myenv
```

### Ativar ambiente virtual

- #### Windows

```powershell
.\myenv\Scripts\activate
```
> [!NOTE]
> **Deve retornar:** `(myenv) C:\Users\`

  
- #### macOS e Linux

```bash
source myenv/bin/activate
```

> [!NOTE]
> Para desativar o ambiente virtual a qualquer momento, basta executar o seguinte comando:

```bash
deactivate
```

## 📦 Instalação das Dependências

O script utiliza a biblioteca Telethon para interagir com o Telegram.

### Instalar o [telethon](https://pypi.org/project/Telethon/)

- #### Windows

```powershell
pip install telethon
```

- #### macOS e Linux

```bash
pip3 install telethon
```

## 🚀 Execução do Script

### Para iniciar a cópia de conteúdo:

- #### Windows

```powershell ou CMD
python bot_ptbr.py
```

- #### macOS e Linux

```bash
python3 bot_ptbr.py
```

## 📋 Instruções de Uso
Ao executar o script, você será solicitado a escolher se deseja carregar novas mensagens ou reenviar todas as mensagens do canal de origem.

- Digite `s` para copiar apenas as novas mensagens do canal de origem para o destino.
- Digite `n` para copiar todas as mensagens novamente da origem para o destino.

>[!NOTE]
> Se você interromper o script e reiniciá-lo, poderá optar por continuar de onde parou ou começar do zero.

## 🛠 Solução de problemas
- Certifique-se de ter entrado nos canais/grupos de origem e destino antes de executar o script.
- Verifique novamente suas credenciais de API se encontrar erros de autenticação.
  Se o script parar inesperadamente, você pode executá-lo novamente. 
  Use o prompt s/n para controlar qual conteúdo será copiado.

## 🤝 Contribuições da comunidade

Pull Requests são bem-vindos!

Se você tiver ideias para melhorias, correções ou novos recursos, abra uma *Issue* para discussão ou envie um *Pull Request* diretamente.

## ❤️ Apoio
Se você achar este projeto útil, por favor, dê uma estrela ⭐️ ao repositório para demonstrar seu apoio!

<p align="center"> <samp>Based on the original project by Warnigo</samp> </p> 
<p align="center">
  <samp>
    Enhanced and actively maintained by
    <a href="https://github.com/WaggBR">WaggBR</a>
  </samp>
</p>
<p align="center">
  <a href="https://t.me/Wagg13">
    <img src="https://img.shields.io/badge/Telegram-Contact-2CA5E0?logo=telegram&logoColor=white"/>
  </a>
</p>



