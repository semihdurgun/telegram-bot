import logging, json, random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    Filters
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND, THIRD, FOURTH, FIFTH = range(5)
# Callback data
ONE, TWO, THREE, FOUR, FIVE, SIX = range(6)


def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("❤️‍🔥 Exosama?", callback_data=str(ONE)),
            InlineKeyboardButton("❤️‍🔥 Moonsama?", callback_data=str(THREE)),
            InlineKeyboardButton("⭐ Tiggah?", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("🤜                <b>EXOSAMA MENU</b>                🤛", reply_markup=reply_markup, parse_mode="HTML")
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

def start_over(update: Update, context: CallbackContext) -> int:
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [ 
            InlineKeyboardButton("❤️‍🔥 Exosama?", callback_data=str(ONE)),
            InlineKeyboardButton("❤️‍🔥 Moonsama?", callback_data=str(THREE)),
            InlineKeyboardButton("⭐ Tiggah?", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="🤜                <b>EXOSAMA MENU</b>                🤛", reply_markup=reply_markup, parse_mode="HTML")
    return FIRST

def moonsama(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("❤️‍🔥 Moonsama Information", callback_data=str(TWO))
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Moonsama's Last Tweets", callback_data=str(THREE))
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Donnie Tweet", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("❤️‍🔥 All Tweets of Exosama", url='https://twitter.com/moonsamanft')
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Moonsama Discord", url='https://discord.gg/moonsama')
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Moonsama WIKI", url='https://wiki.moonsama.com/')
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Moonsama Chat", url='https://t.me/moonsamanft')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="❤️‍🔥😻                <b>EXOSAMA</b>                😻❤️‍🔥", reply_markup=reply_markup, parse_mode="HTML"
    )
    return FIFTH

def exosama(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("❤️‍🔥 Exosama Information", callback_data=str(TWO))
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Exosama Random Fan Arts", callback_data=str(FOUR))
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Exosama's Last Tweets", callback_data=str(THREE))
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Last Tweets About Exosama", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("❤️‍🔥 All Tweets of Exosama", url='https://twitter.com/exosamanft')
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Exosama Discord", url='https://discord.gg/exosama')
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Exosama WIKI", url='https://wiki.moonsama.com/18-exosama')
        ],
        [
            InlineKeyboardButton("❤️‍🔥 Exosama Chat", url='https://t.me/exosama')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="❤️‍🔥😻                <b>EXOSAMA</b>                😻❤️‍🔥", reply_markup=reply_markup, parse_mode="HTML"
    )
    return SECOND

def tiggah(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("⭐ Tiggah's Last Activity", callback_data=str(THREE)),
        ],
        [
            InlineKeyboardButton("⭐ Tiggah's Last Telegram Messages", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("⭐ Tiggah's Last Tweets", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("⭐ All Tweets of Tiggah", url='https://twitter.com/tiggerscrypto'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="⭐😻                <b>About Tiggah</b>                😻⭐", reply_markup=reply_markup, parse_mode="HTML"
    )
    return THIRD

def exosama_info(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="""<b>What is Exosama?🔥</b>
    Exosama is the newest collection from Moonsama to add to our existing Moonsama universe that started in September 2021. Exosama is getting a browser-based cyberpunk RPG built on Polkadot with access to our other metaverses.

    There will be 10000 Exosamas and unlike most NFTs they are composable, multi-chain, multi-resourced, multi-verse NFTs that can adapt to the newest trends seamlessly and have a longer lifespan than normally.

    A concrete example is that we’ll have evolvable NFTs (Exosama) that can have other NFTs on top of it such as weapons, in-game items, and clothes that then we can use with our existing Exosamas without creating a totally new Exosama NFT while changing the looks and utilities of our existing Exosamas.

    On which blockchain will the mint happen?
    We have not decided yet on which blockchain the mint will be on, however you'll be airdropped an NFT on the ETH mainnet. Expect to hear more details after Moonsama v2 is out.

    How will the funds be used?
    All funds will be used for the development of the project.

    When will Exosama come out?
    As of now due to our changes with how to proceed with the launch due to wanting to finish Moonsama v2 first and making Exosamas more advanced than initially thought before the launch, the date is TBA although our first priority after Moonsama v2

    I own a Moonsama, will I be whitelisted?
    Moonsamas will get 2 Exosamas airdropped but not whitelist. You can still earn a whitelist spot through other means.

    What will be the price to mint one Exosama?
    Most likely be around $500-$1000 depending on chain/gas costs.

    How to get whitelisted?
    We give whitelists based on activity, contributions (videos, articles, art) and the progress made in researching the project COMBINED. Submitting a contribution does not usually guarantee you a whitelist if you are not active otherwise unless it really stands out though so best to get to know the community first

    Researching > art

    You should also research Dotsama, Moonsama, XCM, resources and the history as well as they're all part of our Moonsama multiverse. Good places to start is t.me/MoonsamaNFT and https://wiki.moonsama.com/

    If you're already somehow familiar how blockchain does work https://wiki.polkadot.network/docs/learn-crosschain

    Please do not ask admins to give an opinion about your contribution. We'll see them all even if we do not react and it always increases your chances of getting whitelisted even if it happens a long time after submitting your contribution. 

    
    Will there be a public mint?
    TBA

    How to find more information about the project and follow its progress?

    https://wiki.moonsama.com/ """, reply_markup=reply_markup
    ,parse_mode="HTML")
    # Transfer to conversation state `THIRD`
    return FOURTH

def moonsama_info(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="""<b>What is Moonsama?🔥</b>
    Moonsama is the first NFT collection from Moonsama to add to our existing Moonsama universe that started in September 2021. Moonsama is getting a browser-based cyberpunk RPG built on Polkadot with access to our other metaverses.
     

    Donnie's tweets♥️ https://twitter.com/DonnieBigBags + https://wiki.moonsama.com/ """, reply_markup=reply_markup
    ,parse_mode="HTML")
    # Transfer to conversation state `THIRD`
    return FOURTH

def exosama_fan_art(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    query.delete_message()
    #context.bot.delete_message(chat_id=update.effective_chat.id,message_id=all)
    keyboard = [
        [
            InlineKeyboardButton("💫 Get Random Art", callback_data=str(FIVE))
        ],
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    #print(query)
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('fan-art/1 ('+str(random.randint(1, 148)) +').jpg','rb'))
    context.bot.send_message(
        chat_id=update.effective_chat.id,text="💣<b>Exosama Fan Arts</b>💣", reply_markup=reply_markup, parse_mode="HTML"
    )
    
    # Transfer to conversation state `SECOND`
    return FOURTH

def exosama_tweet(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""

    with open("exosama_tweet.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("💣 See Previous Tweets!", callback_data=str(THREE))
        ],
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='\n'.join(firstline[10::-1]), reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def exosama_site_tweet(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""

    with open("exosama_site_tweet.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='\n'.join(firstline[10::-1]), reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def exosama_tweet_last(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""

    with open("exosama_tweet.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='\n'.join(firstline[:10:-1]), reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def moonsama_site_tweet(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""

    with open("moonsama_site_tweet.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='\n'.join(firstline[10::-1]), reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def donnie_tweet(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    with open("donnie_tweet.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("💣 See Previous Tweets!", callback_data=str(FOUR))
        ],
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='\n'.join(firstline[11::-1]), reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def donnie_tweet_last(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    with open("donnie_tweet.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='\n'.join(firstline[:11:-1]), reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def tiggah_activity(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    with open("tiggah_telegram.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="<b>"+firstline[-1][6:26]+"</b>", reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def tiggah_tweet(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    with open("tiggah_tweet.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("💣 See Previous Tweets!", callback_data=str(FOUR))
        ],
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='\n'.join(firstline[11::-1]), reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def tiggah_tweet_last(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    with open("tiggah_tweet.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='\n'.join(firstline[:11:-1]), reply_markup=reply_markup, parse_mode="HTML"
    )
    # Transfer to conversation state `SECOND`
    return FOURTH

def tiggah_message(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    with open("tiggah_telegram.txt",'r', encoding="utf8") as f:
        firstline = f.readlines()

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔙 Take Me Back!", callback_data=str(ONE))
        ],
        [
            InlineKeyboardButton("👋 Thank You!", callback_data=str(TWO))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        query.edit_message_text(
            text='\n'.join(firstline[-40:]), reply_markup=reply_markup, parse_mode="HTML"
        )
    except:
        query.edit_message_text(
            text='\n'.join(firstline[-30:]), reply_markup=reply_markup, parse_mode="HTML"
        )
    # Transfer to conversation state `SECOND`
    return FOURTH

def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See You Later💋 All for EXOSAMA💪🙏\n\n\nhttps://twitter.com/TiggersCrypto\nhttps://twitter.com/DonnieBigBags\nhttps://twitter.com/ExosamaNFT\nhttps://twitter.com/MoonsamaNFT\nhttps://twitter.com/Polkadot\n",parse_mode="HTML")
    return ConversationHandler.END

def deneme(update, context):

    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5336844972:AAGOEwxDZcTH4oLBgkGs3c3c53CFN6FDBmI")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(exosama, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(tiggah, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(moonsama, pattern='^' + str(THREE) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(exosama_tweet, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(exosama_info, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(exosama_site_tweet, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(exosama_fan_art, pattern='^' + str(FOUR) + '$'),
            ],
            THIRD: [
                CallbackQueryHandler(tiggah_message, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(tiggah_tweet, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(tiggah_activity, pattern='^' + str(THREE) + '$'),
            ],
            FOURTH: [
                CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(exosama_tweet_last, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(tiggah_tweet_last, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(exosama_fan_art, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(donnie_tweet_last, pattern='^' + str(SIX) + '$'),
            ],
            FIFTH: [
                CallbackQueryHandler(donnie_tweet, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(moonsama_info, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(moonsama_site_tweet, pattern='^' + str(THREE) + '$'),
            ]
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()