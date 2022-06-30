import requests
import dataYandex as dataYa
import json


class YandexDisk:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f"OAuth {self.token}"
        }

    def get_folder_info(self, folder_name):
        params = {'path': folder_name}
        response = requests.get(dataYa.url, headers=self.get_headers(), params=params)
        if response.status_code == 200:
            result = json.loads(response.text)
            return result.get('path')
        else:
            return response.status_code

    def delete_folder(self, folder_name):
        params = {'path': folder_name}
        response = requests.delete(dataYa.url, headers=self.get_headers(), params=params)
        return response.status_code

    def create_folder(self, folder_name):
        params = {'path': folder_name}
        response = requests.put(dataYa.url, headers=self.get_headers(), params=params)
        return response.status_code


if __name__ == '__main__':
    yaD = YandexDisk(dataYa.token)
    folder = "test 2"
    # print(yaD.create_folder(folder))
    # print(yaD.get_folder_info(folder))
    # print(yaD.delete_folder(folder))
