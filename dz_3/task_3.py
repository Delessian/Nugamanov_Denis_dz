name_employ = {}
def thesaurus(*args):
    for i in args:
        def accepted(first_later):
            return first_later.startswith(i[0])
        name_filter = filter(accepted, args)
        name_employ.setdefault(i[0], list(name_filter))
    for key, val in name_employ.items():
        print(f'{key}:{val}', sep='\n')
    
thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Ильнур')
