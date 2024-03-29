import json

import requests
import sys
import os


def get_updated():
    url = f'https://api.github.com/repos/{repo}/pulls/{pr}/files'
    response = requests.get(url)
    files = response.json()
    return [file['filename'] for file in files]

def find_info(context):
    #head = context['event']['pull_request']['base']['sha']
    base = context['event']['pull_request']['base']['ref']
    curr = context['event']['after']

    # run git diff
    os.system(f'git diff {base}')

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        context = json.load(f)

    find_info(context)





