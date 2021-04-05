tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

if len(tutors) > len(klasses):
    for i in range(len(tutors) - len(klasses)):
            klasses.append(None)
tutor_klass = ((tutor, klass) for tutor, klass in zip(tutors, klasses))

#print(*tutor_klass)
print(next(tutor_klass))
print(next(tutor_klass))
