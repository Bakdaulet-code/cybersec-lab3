import random
import pyautogui
import time

inPasswd = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789"

inPasswdList = list(inPasswd)

passwd = pyautogui.password(title='Password field',
                              text='Enter the password',
                              mask='x')

searchingPasswd = ""
final = '!! THE PASSWORD WAS FOUND !!'
while searchingPasswd != passwd:
    searchingPasswd = random.choices(inPasswdList, k=len(passwd))
    print("|=======" + str(searchingPasswd) + "=======|")
    if searchingPasswd == list(passwd):
        for each in final:
            print(each, end="")
            time.sleep(0.3)
        print('\n')
        print("Your password is : " + "".join(searchingPasswd))
        break

