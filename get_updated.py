import json

import requests
import sys


def get_updated():
    url = f'https://api.github.com/repos/{repo}/pulls/{pr}/files'
    response = requests.get(url)
    files = response.json()
    return [file['filename'] for file in files]


if __name__ == '__main__':
    context = json.loads(sys.argv[1])

    print(context)
