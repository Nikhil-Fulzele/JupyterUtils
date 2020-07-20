import requests

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def download_files(dependency_url, alias, **kwargs):

    response = requests.get(dependency_url, **kwargs)

    with open(alias, 'wb') as out:
        out.write(response.content)
