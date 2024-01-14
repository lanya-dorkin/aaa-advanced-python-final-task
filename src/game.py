from telegram import InlineKeyboardMarkup, Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)
from utils import get_default_state, generate_keyboard, random_bot_choice
from consts import FREE_SPACE, CROSS, ZERO, CONTINUE_GAME, FINISH_GAME


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    context.user_data["keyboard_state"] = get_default_state()
    keyboard = generate_keyboard(context.user_data["keyboard_state"])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "X (your) turn! Please, put X to the free place", reply_markup=reply_markup
    )
    return CONTINUE_GAME


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Main processing of the game"""
    row, col = map(int, update.callback_query.data)
    fields = context.user_data["keyboard_state"]

    # continue if user picks non free space
    if fields[row][col] != FREE_SPACE:
        return CONTINUE_GAME

    # set user choice
    fields[row][col] = CROSS

    # get and set bot choice if there are any free fields
    bot_choice = random_bot_choice(fields)
    if bot_choice is not None:
        row, col = bot_choice
        fields[row][col] = ZERO

    # prepare and send reply
    keyboard = generate_keyboard(context.user_data["keyboard_state"])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "X (your) turn! Please, put X to the free place", reply_markup=reply_markup
    )

    # check user win
    if won(fields, CROSS):
        await update.callback_query.message.reply_text("You won! GJ")
        return FINISH_GAME

    # check bot win
    if won(fields, ZERO):
        await update.callback_query.message.reply_text("You lost! Pathetic")
        return FINISH_GAME

    return CONTINUE_GAME


def won(fields: list[str], label: str) -> bool:
    """Check if crosses or zeros have won the game"""
    # check rows
    for row in fields:
        if all(cell == label for cell in row):
            return True

    # check columns
    for col in zip(*fields):
        if all(cell == label for cell in col):
            return True

    # check diagonals
    forward_diag = all(fields[i][i] == label for i in range(len(fields)))
    backward_diag = all(
        fields[i][len(fields) - i - 1] == label for i in range(len(fields))
    )
    if forward_diag or backward_diag:
        return True

    return False


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    # reset state to default so you can play again with /start
    context.user_data["keyboard_state"] = get_default_state()
    return ConversationHandler.END
