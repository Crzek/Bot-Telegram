
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Define las palabras clave que deseas buscar
palabras_clave = ["palabra1", "palabra2", "palabra3"]

# Define una función para manejar los mensajes que contienen las palabras clave


def manejar_mensaje(update, context):
    mensaje = update.message.text
    for palabra in palabras_clave:
        if palabra in mensaje:
            context.bot.forward_message(
                chat_id=CHAT_ID_DESTINO, from_chat_id=update.message.chat_id, message_id=update.message.message_id)


# Crea un objeto Updater y pasa el token de acceso del bot
updater = Updater("TOKEN_DE_ACCESO")

# Crea un objeto MessageHandler y pasa la función manejar_mensaje
manejador_mensaje = MessageHandler(
    Filters.text & ~Filters.command, manejar_mensaje)

# Agrega el manejador al Updater
updater.dispatcher.add_handler(manejador_mensaje)

# Inicia el bot
updater.start_polling()
