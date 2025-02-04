from pyrogram import Client, filters
import os
from dotenv import load_dotenv
from time import sleep
from asyncio import sleep as assleep

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
MY_ID = os.getenv("OWNER_ID")
app = Client("my_userbot", api_id=API_ID, api_hash=API_HASH)


@app.on_message(filters.private)
async def start(client, message):
    if message.from_user.id == int(MY_ID):
        text = message.text
        command = text[:4]
        commands = [
            "repe",
            "anim",
            "ping",
        ]
        if command in commands:
            text = text[4:].strip()
            if command == "repe":
                count = int(text.split(" ")[0])
                text = text[len(str(count)):]

                chat_id = message.chat.id
                async for previous_message in app.get_chat_history(chat_id, limit=1):
                    await app.delete_messages(chat_id, previous_message.id)
                 
                for i in range(count):
                    await message.reply(f'{text} {i + 1}')
                    await assleep(0.2)
            elif command == "anim":

                space = False
                a = ""
                loading_texts = []
                for i in range(len(text)):
                    if text[i] == " ":
                        a += " " + text[i + 1]
                        space = True
                    elif space == True:
                        space = False
                        continue
                    else:
                        a += text[i]

                    loading_texts.append(a)

                chat_id = message.chat.id
                async for previous_message in app.get_chat_history(chat_id, limit=1):
                    await app.delete_messages(chat_id, previous_message.id)

                sent_message = await message.reply_text(loading_texts[0])

                for text in loading_texts[1:]:
                    await sent_message.edit(text)
                    await assleep(0.2)
            elif command == "ping":
                await message.reply(text)


if __name__ == "__main__":
    app.run()
