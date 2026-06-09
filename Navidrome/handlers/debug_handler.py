from telegram import Update
from telegram.ext import ContextTypes
from log import logger

async def debug_unhandled_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """记录未被其它 Handler 捕获的 CallbackQuery，便于调试"""
    try:
        query = update.callback_query
        user = query.from_user
        message = query.message
        chat = message.chat if message else None
        logger.warning(f"UNHANDLED CallbackQuery - user_id={user.id} username={user.username} data={query.data} chat_id={chat.id if chat else 'N/A'} message_id={message.message_id if message else 'N/A'}")
        # 回复以防止 Telegram 超时提示（不打扰用户）
        await query.answer(cache_time=5)
    except Exception as e:
        logger.error(f"Error in debug_unhandled_callback: {e}")
