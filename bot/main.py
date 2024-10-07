from pyrogram import Client
from decouple import config


assert config('API_ID') != 'None', 'API_ID must be defined in the .env file!'
assert config('API_HASH') != 'None', 'API_HASH must be defined in the .env file!'
assert config('BOT_TOKEN') != 'None', 'BOT_TOKEN must be defined in the .env file!'


def main():
    """
    ~ main function (bot run)
    """
    print('calculator robot V1.0.0 started...', end='\n')
    bot = Client(
        name=config('NAME'),
        api_id=config('API_ID'),
        api_hash=config('API_HASH'),
        bot_token=config('BOT_TOKEN'),
        plugins={
            'root': 'tools'
        }
    )
    bot.run()


if __name__ == '__main__':
    main()