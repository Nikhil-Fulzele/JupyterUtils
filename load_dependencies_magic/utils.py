import json
import requests

from urllib.parse import urlparse

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def download_files(dependency_url, alias=None, file_type='ipynb', auth=None, verify=False):
    parse_path = urlparse(dependency_url)
    path = "/".join(parse_path.path.rsplit('/')[2:])
    netloc = parse_path.netloc
    scheme = parse_path.scheme

    content_api = f"{scheme}://{netloc}/api/contents/"
    final_path = content_api + path

    res = requests.get(final_path, auth=auth, verify=verify)

    with open(alias, 'w') as out:
        if file_type == 'ipynb':
            data = json.dumps(res.json()['content'])
        elif file_type in ['csv', 'py', 'txt']:
            data = res.json()['content']
        else:
            raise Exception(f"Illegal file type : {file_type}. Currently it supports only .ipynb, .csv, .py and .txt")
        out.write(data)
