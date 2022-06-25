import requests
import os

ms_notion_api_token = os.environ.get('MS_NOTION_API_TOKEN')
ms_database_id_money = os.environ.get('MS_DATABASE_ID_MONEY')
url = "https://api.notion.com/v1/databases/" + ms_database_id_money

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Authorization": "Bearer " + ms_notion_api_token
}

response = requests.get(url, headers=headers)

print(response.text)
