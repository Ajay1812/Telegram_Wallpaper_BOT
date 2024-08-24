import asyncio
from datetime import datetime
import os
from telegram import Bot
from telegram.request import HTTPXRequest
from get_file_name import extract_image_paths
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

with open('image_file_names.txt', 'r') as f:
    uploaded_image_paths = f.read().split('\n')
    print("Read Successfully")


def add_path(extract_file_names,uploaded_image_paths):
    image_path_list = []
    for file in extract_file_names:
        if '/Users/ajay/Documents/Personal/Wallpapers' + "/" + file not in uploaded_image_paths:
            image_path_list.append('/Users/ajay/Documents/Personal/Wallpapers' + "/" + file)
    return image_path_list


async def main():
    bot = Bot(token=BOT_TOKEN, request=HTTPXRequest())

    file_path = '/Users/ajay/Documents/Personal/Wallpapers'
    extract_file_names = extract_image_paths(file_path)
    file_paths =  add_path(extract_file_names,uploaded_image_paths)
    # print(file_paths)

    for file_path in file_paths:
        try:
            file_name = os.path.basename(file_path)
            print("Uploading... :", file_name)
            with open(file_path, 'rb') as file:
                await bot.send_photo(chat_id=CHAT_ID, photo=file,caption=f"{file_name}")
                with open('image_file_names.txt', 'a+') as f:
                    f.write(file_path + "\n")
                print("Image Paths Written Successfully")
        except Exception as e:
            print("Error: ", e)

    print("Files uploaded successfully.", datetime.now())

if __name__ == "__main__":
    asyncio.run(main())
