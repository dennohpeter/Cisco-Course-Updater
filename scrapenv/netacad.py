import re

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open('https://www.netacad.com/login/')
form = br.get_form()
form['_58_INSTANCE_fm_login'] = 'lelerukjaymoh@gmail.com'
form['_58_INSTANCE_fm_password'] = 'Jay17kish05'
br.submit_form(form)

src = str(br.parsed())

start = '<h1 id="banner-title">'
end = '</h1>'

result = re.search('%s(.*)%s' % (start, end), src).group(1)
print(result)
