import requests


def send_request(url):
    return requests.get(url)


if __name__ == '__main__':
    target_link = 'https://pypi.org/project/copydetect/'
    print(send_request(target_link))
