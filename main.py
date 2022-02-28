import evn as keys
from telegram.ext import *
from telegram.ext.filters import Filters
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
import responses as r
print("Bot Started...")
import os
PORT = int(os.environ.get('PORT', 5000))

# JFEB 14 Kulla Project Mudikiro !!! SLICE PANROM !!!
# (Few Commands Listed Below)

def help_command(update,context):
    update.message.reply_text("""
	FEB 14 Kulla Project Mudikiro !!! SLICE PANROM !!!
	(Few Commands Listed Below)
	
	/meet - To get the meet link   
	/gen1 - To get the output link
	/gen2 - To get the output link

	""")
 
def handle_message(update ,context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text,update)
    update.message.reply_text(response)
    
def error(update,context):
    print(f"Update {update} caused error {context.error}")


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Mudiyathu Yenna Panuva")


# def unknown(update: Update, context: CallbackContext):
	# update.message.reply_text(
		# "Sorry '%s' is not a valid command" % update.message.text)


# def unknown_text(update: Update, context: CallbackContext):
	# update.message.reply_text(
		# "Sorry I can't recognize you , you said '%s'" % update.message.text)


def main():        
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    # updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    # updater.dispatcher.add_handler(MessageHandler(
	# Filters.command, unknown)) # Filters out unknown commands
    # Filters out unknown messages.
    # updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)
	
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=keys.API_KEY)
    # updater.start_polling()
    updater.bot.setWebhook('https://hey-sad-bot.herokuapp.com/' + keys.API_KEY)
    updater.idle()

main()


# $ git add .
# $ git commit -am "make it better"
# $ git push heroku master