import pyautogui
import time
def start():
    print("This program servers only for educational purposes, do not use this for hurting someone yk.")
    print("I do not take any responsibilites for you being motherfucker.")
    print("Enter the message you want to spam: ")
    spam()

def spam():
    msg = input()
    count = input("How many times? ")
    print("Let's begin!")
    timer = 5
    while(timer !=0):
        print(timer)
        time.sleep(1)
        timer -= 1
    for i in range(0, int(count)):
        pyautogui.typewrite(msg + '\n')
    print("Do you want to continue?")
    choices()
    
def choices():
    print("[1] - Do it again lol [2] - Close the app")
    choice = input()
    match choice:
        case "1": start()
        case "2": quit()
        case _: choices()

start()
    
