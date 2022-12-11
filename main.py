from aiogram import executor
from bot_instance import dp
from handlers import client, extra
from handlers import fsmadmin

fsmadmin.register_handler_fsmadmin(dp)
client.register_handlers_client(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
