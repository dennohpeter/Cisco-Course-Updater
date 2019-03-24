import re

from robobrowser import RoboBrowser

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
}

br = RoboBrowser()
br.open('https://www.netacad.com/login/')
form = br.get_form()
form['_58_INSTANCE_fm_login'] = 'denispeterson96@gmail.com'
form['_58_INSTANCE_fm_password'] = 'Dennis537301*'
br.submit_form(form, headers=headers)

src = str(br.parsed())

start = '<h1 id="banner-title">'
end = '</h1>'

result = re.search('%s(.*)%s' % (start, end), src).group(1)
print(result)
