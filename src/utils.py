from copy import deepcopy
import random
from telegram import InlineKeyboardButton
from consts import FREE_SPACE, DEFAULT_STATE


def get_default_state() -> list[list[str]]:
    """Helper function to get default state of the game"""
    return deepcopy(DEFAULT_STATE)


def generate_keyboard(state: list[list[str]]) -> list[list[InlineKeyboardButton]]:
    """Generate tic tac toe keyboard 3x3 (telegram buttons)"""
    return [
        [InlineKeyboardButton(state[r][c], callback_data=f"{r}{c}") for r in range(3)]
        for c in range(3)
    ]


def random_bot_choice(fields: list[list[str]]) -> tuple[int] | None:
    """Generate random turn for the bot."""
    empty_fields = [
        (row_idx, col_idx)
        for row_idx, row in enumerate(fields)
        for col_idx, field in enumerate(row)
        if field == FREE_SPACE
    ]
    return random.choice(empty_fields) if empty_fields else None
