from discord import Intents, Client
import Responses
from datetime import datetime



def run_bot(token: str):
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    knowledge: dict = Responses.load_knowledge('knowledge.json')

    @client.event
    async def on_ready():
        print(f'{client.user} is now running.')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return



        if message.content:
            if 'time' in message.content:
                current_time = datetime.now()
                await message.channel.send(current_time)
            print(f'{message.channel} {message.author} : {message.content}')
            response: str = Responses.get_response(message.content, knowledge=knowledge)
            await message.channel.send(response)
        else:
            print('Couldn\'t send message.')

    client.run(token=token)


def main() -> None:
    run_bot('PLACE_YOUR_DISCORD_BOT_API_KEY_HERE')

if __name__ == '__main__':
    main()