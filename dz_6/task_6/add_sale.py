import sys

with open('bakery.csv', 'a', encoding='utf-8') as f:
    for arg in sys.argv[1:]:
        f.writelines(f'{arg}\n')
        