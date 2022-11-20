# Subscribe to  my Youtube Channel
str=input('Enter your Name: \033[32m')
lenght = len(str)
print() # Empty
print('\033[00mThe \033[07m\033[07m BINARY Screen \033[00m with:\033[32m',str)
str2='' # Empty string

for a in range(0,lenght,2):
	str2+str[a]
	if a<(lenght-1):
		str2+=str[a+1].upper()
import time
time.sleep(5)
print() # Empty	
print("\033[31mDeveloper: \033[33mHydrogen 27") 
print() # Empty
print("\033[31mYoutube: \033[00m[\033[33mhttps://www.youtube.com/@hydrogen2773\033[00m]")
print() # Empty
print("\033[31mGithub: \033[00m[\033[33mhttps://github.com/Hydrogen-27\033[00m]")
print() # Empty
print("\033[00mThe \033[07m BINARY Screen \033[00m\033[00m user:\033[32m",str)
print() # Empty
time.sleep(1)
print() # Empty
print() # Empty
print("\033[00mTo Stop the \033[00m\033[07m BINARY Screen \033[00m use \033[01m\033[32mCtrl + c \033[00m\033[00mto \033[33mSTOP")
print() # Empty
print() # Empty
print("\033[32m[\033[33m\033[01m1\033[00m\033[32m] \033[32mGreen\033[00m")
print("\033[32m[\033[33m\033[01m2\033[00m\033[32m] \033[34mBlue\033[00m")
print("\033[32m[\033[33m\033[01m3\033[00m\033[32m] \033[31mRed")
print("\033[00m\033[32m[\033[33m\033[01m4\033[00m\033[32m] \033[33mYellow\033[00m")
print("\033[32m[\033[33m\033[01m5\033[00m\033[32m] \033[00m\033[35mViolet\033[00m")
print("\033[32m[\033[33m\033[01m6\033[00m\033[32m] \033[00m\033[36mLight Blue")
print("\033[32m[\033[33m\033[01m7\033[00m\033[32m] \033[00mWhite")
print()# Empty
# Subscribe
print() # Empty
while True:
    # Select Color using Number
    choice = input("\033[00m\033[32mSelect Color\033[00m: ")
    print() # Empty

    # Choice from Number
    if choice in ('0', '1', '2', '3', '4', '5', '6', '7',):
        if choice == '1':
            print("\033[32mGreen \033[00mBinary")
            print("\33[32m")
        elif choice == '2':
            print("\033[34mBlue \033[00mBinary")
            print("\033[34m")
        elif choice == '3':
            print("\033[31mRed \033[00mBinary")
            print("\033[31m")
        elif choice == '4':
            print("\033[33mYellow \033[00mBinary")
            print("\033[33m")
        elif choice == '5':
        	print("\033[35mViolet \033[00mBinary")
        	print("\033[35m")
        elif choice == '6':
        	print("\033[36mBlue \033[00mBinary")
        	print('\033[36m')
        elif choice == '7':
        	print("\033[00mWhite \033[00mBinary")
        	print("\033[00m")
        elif choice == '0':
        	break
        print() # Empty
        next_calculation = input("Are you sure in this color? (y/n): ")
        if next_calculation == "y":
          break
          
        else:
          print() # Empty
          
    else:
        print("\033[31mInvalid Input!\033[00m")
        print() # Empty
import time
time.sleep(10)
  
  # do not Modify!
import math,random
def generateBinary() :
    Digits = "010101010101"
    Binary = ''
    for i in range(10000) :
        Binary += Digits[math.floor(random.random() * 12)]
    return Binary
while __name__ == "__main__" :     
    print('',generateBinary())
    
# ANTI-BACKDOOR
import sys
import webbrowser
webbrowser.open('https://www.youtube.com')
import time
time.sleep(0.1)
# The END!        