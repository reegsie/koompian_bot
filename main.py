#! /usr/bin/python

import constants as keys
import responses as R
from telegram.ext import *
from long_str import *

# Marking the beginning of the converstation 
print ("Bot session has begun")

# Adding an about SEL command 
def help_command(update, context):
    
    update.message.reply_text("You can ask me ANYTHIN")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.main_listener(text)

    update.message.reply_text(response)

def error(update, context):

    print(f"Update {update} caused error {context.error}")

# creating the main function
def main():
    
    # Stats checking for user input
    updater = Updater(keys.API_KEY, use_context=True)
    # variable for output disbatching
    dp = updater.dispatcher
    
    # linking /help to the help_command
    dp.add_handler(CommandHandler("help", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    # setting the update refresh 'null' speed, to define the frequency in which the bot searches for user input (0 refresh = update ever 0.01 seconds)
    updater.start_polling()
    # Setting 'null' timeout so the bot is always active
    updater.idle()

# Calling the main function
main()
