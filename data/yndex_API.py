import json

# with open('YA_token', 'r') as file_object:
#     TOKEN = file_object.read().strip()
token = ''
import requests

url = 'https://cloud-api.yandex.net/v1/disk/'
headers = {'Authorization': 'OAuth ' + token}


def createfolder(folder_name):
    params = {'path': folder_name}
    response = requests.put(url + 'resources', headers=headers, params=params)
    return response.status_code


def get_folder_info(folder_name):
    params = {'path': folder_name}
    response = requests.get(url + 'resources', headers=headers, params=params)
    if response.status_code == 200:
        result_dict = json.loads(response.text)
        return result_dict.get('type')


def del_folder(folder_name):
    params = {'path': folder_name, }
    response = requests.delete(url + 'resources', headers=headers, params=params)
    return response.status_code


if __name__ == '__main__':
    print(del_folder('TEST_YA_APi'))
