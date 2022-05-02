import os
from dotenv import load_dotenv


load_dotenv()

file_results = 'results.json'
folder_use = os.getcwd()
folder_storage = 'storage'
folder_use_storage = os.path.join(folder_use, folder_storage)
file_use_results = os.path.join(folder_use_storage, file_results)

API_KEY = os.getenv('API_KEY')
LINK = 'https://data.fixer.io/api/latest'