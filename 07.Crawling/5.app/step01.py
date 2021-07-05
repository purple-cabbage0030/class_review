# import pyttsx3
# engine = pyttsx3.init()
# engine.say('한글입니다')
# engine.runAndWait()                                                             


# import pyautogui
# num=int(input("Enter a value to divide 100"))
# if num == 0:
#     pyautogui.alert(" Alert!!! 100 cannot be divided by 0")
# else:
#     print(f'The value is {100/num}')


# from faker import Faker
# fake = Faker("ko_KR")
# print(fake.name())
# print(fake.email())
# print(fake.country())

# print(fake.profile())       

# # 언더바: 문법적 필요에 의해 선언하지만, 사용하지 않는 변수 선언 시 사용하는 표현
# for _ in range(10):
#     print(fake.name())


import pywhatkit
pywhatkit.text_to_handwriting('''Learning Python from the basics is 
extremely important. Before starting to learn python,understanding a 
base language like c is a must and 
some of the oops concepts.Python program has many modulesand packages, 
which helps with efficient programming.
Understanding these modules and 1proper usage of many syntax and libraries is recommended.
In this article, a few modules and packages are used in the program. 
Python includes tons of libraries and some of them are quiet intresting''')