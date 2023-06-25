import requests
from mytoken import YA_TOKEN
from urllib.parse import quote


headers = {
    'Authorization': 'OAuth {}'.format(YA_TOKEN)
}


def create_folder(headers, foldername):
    url = f"https://cloud-api.yandex.net/v1/disk/resources?path={quote(foldername)}"
    response = requests.put(url=url, headers=headers)
    print(response.status_code)
    return response.status_code


def get_folder(headers, foldername):
    url = f'https://cloud-api.yandex.net/v1/disk/resources?path={quote(foldername)}'
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    return response.status_code


def delete_folder(headers, foldername):
    url = f'https://cloud-api.yandex.net/v1/disk/resources?path={quote(foldername)}'
    response = requests.delete(url=url, headers=headers)
    return response.status_code



def main():
    create_folder(headers, 'TESTFOLDERN1')
    get_folder(headers, "TESTFOLDER N1")


if __name__ == '__main__':
    main()