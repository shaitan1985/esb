from getpass import getpass
from urllib import request

import requests as requests

from atimo.sandra import FSHandler


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    response = requests.get('http://atimo.kt-team.de/data/get?client_id=12', auth=('admin', input()))
    json_response = response.json()
    FSHandler.log(json_response)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
