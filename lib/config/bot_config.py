from pydantic import BaseSettings as BS


class BotConfig(BS):
    token: str

bot_config = BotConfig(_env_file='env')