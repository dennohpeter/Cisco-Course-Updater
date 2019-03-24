import requests
from bs4 import BeautifulSoup

headers = {     # Haeders ensure the site doest flag the requesr as coming from a bot thus denying access
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
}

login_data = {    # This is the login data to be passed in the login form
    '_58_INSTANCE_fm_login': 'denispeterson96@gmai',
    '_58_INSTANCE_fm_password': 'Dennis537301*',
}

with requests.Session() as s:

    url = 'https://www.netacad.com/login/'

    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html5lib')
    login_data['_58_INSTANCE_fm_formDate'] = soup.find('input', attrs={'name': '_58_INSTANCE_fm_formDate'})['value']
    login_data['_58_INSTANCE_fm_saveLastPath'] = soup.find('input', attrs={'name': '_58_INSTANCE_fm_saveLastPath'})['value']
    login_data['_58_INSTANCE_fm_doActionAfterLogin'] = soup.find('input', attrs={'name': '_58_INSTANCE_fm_doActionAfterLogin'})['value']
    login_data['_58_INSTANCE_fm_redirect'] = soup.find('input', attrs={'name': '_58_INSTANCE_fm_redirect'})['value']

    t = s.post(url, data=login_data, headers=headers)
    print(t.content)
