# try:
#     file=open('list.txt','a')
# except:
#     print("bunday fayl joq")
# else:
#     print(file.write(' Awesbaev'))
#     file.close


import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.json())
