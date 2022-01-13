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

# def help_command(update,context):
#     update.message.reply_text("Die")
 
def handle_message(update ,context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text,update)
    update.message.reply_text(response)
    
def error(update,context):
    print(f"Update {update} caused error {context.error}")


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/RealEstate - Link to - Create Real Estate React App 
	/Amazon - Link to - react-firebase course  built amazon 
	/NetNinja_React_Fire - Link to -React-Firebase - 2018
	/CSSNetNinja - Link to - NetNinja CSS - 2016
	/CSSDown - Link to - CSS - Dropdown Animation
	/CSSJonas - Link to -  CSS3 - HTML5 - Jonas 
""")


def NetNinja_React_Fire_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/watch?v=h9enkZBFCyA" )
		


def RealEstate_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\
	https://youtu.be/sKs9FiAHSN4")


def Amazon_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Youtube Link =>\
		https://www.youtube.com/watch?v=RDV3Z1KCBvo&t=56s")


def CSSNetNinja_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/watch?v=jgw82b5Y2MU&list=PL4cUxeGkcC9iGYgmEd2dm3zAKzyCGDtM5")


def CSSDown_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\https://www.youtube.com/watch?v=IF6k0uZuypA")


def CSSJonas_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/watch?v=inEUEYSjKX8&list=PLvtRgUbhWmy9VgVvvxfiXXriELtjaYYmw")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def main():        
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('RealEstate', RealEstate_url))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('Amazon', Amazon_url))
    updater.dispatcher.add_handler(CommandHandler('NetNinja_React_Fire', NetNinja_React_Fire_url))
    updater.dispatcher.add_handler(CommandHandler('CSSNetNinja', CSSNetNinja_url))
    updater.dispatcher.add_handler(CommandHandler('CSSDown', CSSDown_url))
    updater.dispatcher.add_handler(CommandHandler('CSSJonas', CSSJonas_url))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands
    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)
	
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=keys.API_KEY)
    # updater.start_polling()
    updater.bot.setWebhook('https://hey-sad-bot.herokuapp.com/' + keys.API_KEY)
    updater.idle()

main()


