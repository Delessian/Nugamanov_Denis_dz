import json
from sys import exit
from itertools import zip_longest


with open('users.csv', 'r', encoding='utf-8') as user:
    user_list = user.readlines()
 
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        hobby_list = hobby.readlines()
  
        if len(user_list) >= len(hobby_list):
            dict_user = {key: val for key, val in zip_longest(user_list, hobby_list)}
            with open('dict_user.txt', 'w', encoding='utf-8') as f:
                json.dump(dict_user, f)
            with open('dict_user.txt', 'r', encoding='utf-8') as f:
                print(json.load(f))   
        else:
            exit('1')               
