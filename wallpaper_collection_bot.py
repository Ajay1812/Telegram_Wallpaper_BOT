import asyncio
import os
from telegram import Bot
from telegram.request import HTTPXRequest
from get_file_name import extract_image_paths
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def add_path(extract_file_names):
    image_path_list = []
    for file in extract_file_names:
        image_path_list.append('/Users/ajay/Documents/Personal/Wallpapers' + "/" + file)
    return image_path_list


async def main():
    bot = Bot(token=BOT_TOKEN, request=HTTPXRequest())

    file_path = '/Users/ajay/Documents/Personal/Wallpapers'
    extract_file_names = extract_image_paths(file_path)
    file_paths =  add_path(extract_file_names)
    # print(file_paths)

    for file in file_paths:
        try:
            file_name = os.path.basename(file)
            print("Uploading... :", file_name)
            with open(file, 'rb') as file:
                await bot.send_document(chat_id=CHAT_ID, document=file,caption=f"{file_name}")
        except Exception as e:
            print("Error: ", e)


    print("Files uploaded successfully.")

if __name__ == "__main__":
    asyncio.run(main())



