import re


def email_parse(email):
    pars = r'([\w.-]+)@([\w-]+)\.[\w.-]+'
    assert re.match(pars, email), f'wrong email {email}'
    result = re.findall(pars, email)
    info = ['user', 'domain']
    for i in result:
        print({key: val for key, val in zip(info, list(i))})
       
email_parse('someone@geekbrains.ru')
email_parse('Delessina@mail.ru')
email_parse('Denden508@rambler.ru')

