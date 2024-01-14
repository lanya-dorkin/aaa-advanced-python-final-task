import pytest
from unittest.mock import Mock
from telegram import Update
from telegram.ext import CallbackContext
from src.game import game
from src.consts import CONTINUE_GAME, FINISH_GAME, FREE_SPACE, CROSS, ZERO


@pytest.fixture
def mock_update():
    return Mock(Update)


@pytest.fixture
def mock_context():
    return Mock(CallbackContext)


async def identity(*args, **kwargs):
    return args, kwargs


@pytest.mark.asyncio
async def test_game(mock_update, mock_context):
    mock_update.callback_query.data = '00'
    mock_update.callback_query.message.reply_text = identity
    mock_context.user_data = {'keyboard_state': [[FREE_SPACE] * 3 for _ in range(3)]}
    
    result = await game(mock_update, mock_context)

    assert result == CONTINUE_GAME
    assert mock_context.user_data['keyboard_state'][0][0] == CROSS


@pytest.mark.asyncio
async def test_game_win(mock_update, mock_context):
    mock_update.callback_query.data = '00'
    mock_update.callback_query.message.reply_text = identity
    mock_context.user_data = {'keyboard_state': [[CROSS]*3 for _ in range(3)]}
    mock_context.user_data['keyboard_state'][0][0] = FREE_SPACE

    result = await game(mock_update, mock_context)

    assert result == FINISH_GAME


@pytest.mark.asyncio
async def test_game_lose(mock_update, mock_context):
    mock_update.callback_query.data = '00'
    mock_update.callback_query.message.reply_text = identity
    mock_context.user_data = {'keyboard_state': [[ZERO]*3 for _ in range(3)]}
    mock_context.user_data['keyboard_state'][0][0] = FREE_SPACE
    mock_context.user_data['keyboard_state'][0][1] = FREE_SPACE

    result = await game(mock_update, mock_context)

    assert result == FINISH_GAME
