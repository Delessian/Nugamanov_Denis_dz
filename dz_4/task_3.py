import requests 

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
r = response.text
r = r.split('><')
dict_valute ={}

def foreign_currency(CharCode):
    for i in range(len(r)):
        if r[i].find(CharCode.upper()) != -1:
            part_r = r[(i+1):(i+4)]
            for j in range(len(part_r)):
                if part_r[j].find('Value') == 0:
                    part_j = part_r[j].replace('>','<')
                    part_j = part_j.split('<')
                    part_j = part_j[1].replace(',', '.')
            dict_valute.setdefault(CharCode.upper(), f'{round(float(part_j),2)} руб.')
    if dict_valute.get(CharCode.upper()) != None:
        print(f'{dict_valute.get(CharCode.upper())}\n{response.headers["Date"]}')
    else:
        print(dict_valute.get(CharCode.upper()))
        
if __name__ == '__main__':
    foreign_currency('Usd')


