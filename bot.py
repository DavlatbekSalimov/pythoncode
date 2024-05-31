
import requests
URL = 'https://65a3de1aa54d8e805ed41c6d.mockapi.io/contact/usersm'


while True:
    print("""
        Xush Kelibsiz
        1.Ma'lumotlarni ko'rish
        2.O'chirish
    """)
    inputt = input()
    if int(inputt) == 1:
        res = requests.get(URL).json()
        print(f'\x1B[31m{res}\x1B[0m')
    elif int(inputt) == 2:
        print("Id raqam kiriting")
        id =int(input())
        is_found = False
        for r in res:
            if r['id'] == str(id):
                is_found = True

        if not is_found:
            print('bu id yoq')
        else:
            delete = requests.delete(f'{URL}/{id}')
            if delete.status_code == 200 or delete.status_code ==201 :
                print("O'chirildi")
            else:
                print("error bo'lsi")
    else:
        print("bu tugma yo'q")

      
   






# s= {1,1,2}

# if res[0]["id"]=="2":
#     print(res)
# else:
#     print(s)



# a = '78'


# if type(a) == str:
#     print(f'salom {a}')
# else : 
#     print('bor')
# a = [1,2,3,4,5,6,7,8,9,10]
# for i in range (len(a)):
#         print(a[i])

