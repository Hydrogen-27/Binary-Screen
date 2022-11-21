## Developer: Hydrogen-27         THE BINARY SCREEN
print('') ##  Version: 1.0.1
print('')  ##  
print("Welcome to Binary Screen!") ##
print('') ##
print("Developer:       Hydrogen 27") ##
print("Youtube channel: Hydrogen 27") ##
print("Github:          https://github.com/Hydrogen-27  ") ##
print('') ##
print("Usages:") ##
print('') ##
print(" * cd Binary-Screen") ##
print(" * python3 Binary.py") ##
print(" * To Stop the Binary Screen use \033[32mCTRL + c \033[00mto \033[33mSTOP\033[00m") ##
print('') ##
print("Current version: v.1.0") ##
print('') ##
## 
print("1 \033[32m01001000\033[00m") ##
print("2 \033[34m01100101\033[00m") ##
print("3 \033[31m01101100\033[00m") ##
print("4 \033[33m01101100\033[00m") ##
print("5 \033[35m01101111\033[00m") ##
print("6 \033[36m00110010\033[00m") ##
print("7 \033[00m00110111") ##
print('') ##
##
while True: ##
    choice = input("\033[32m~ \033[00m$ Select color: ") ##
##
    if choice in ('0', '1', '2', '3', '4', '5', '6', '7',): #
        if choice == '1': #
            print('') #
            print("\033[32m01001000\033[00m") #
            print("\33[32m") #
 ##           
        elif choice == '2':
            print('') ##
            print("\033[34m01100101\033[00m") ##
            print("\033[34m") ##
##            
        elif choice == '3': ##
            print('') ##
            print("\033[31m01101100\033[00m") ##
            print("\033[31m") ##
##            
        elif choice == '4': ##
            print('') ##
            print("\033[33m01101100\033[00m") ##
            print("\033[33m") ##
##                      
        elif choice == '5': ##
        	print('') ##
        	print("\033[35m01101111\033[00m") ##
        	print("\033[35m") ##
##        	
        elif choice == '6': ##
        	print('') ##
        	print("\033[36m00110010\033[00m") ##
        	print('\033[36m') ##
##        	
        elif choice == '7': ##
        	print('') ##
        	print("\033[00m00110111") ##
        	print("\033[00m") ##
        else: ## 
        	print("\033[32m~ \033[00m$ Invalid Command!") ##
##         	
        next_calculation = input("Are you sure in this color? (y/n): ") ##
        print('') ##
        if next_calculation == "y": ##
          break ##
## Hydrogen_generate_num    
import math,random
def generateHydrogen27() :
    Digits = "010101010101"
    Hydrogen27 = ''
    for i in range(10000) :
        Hydrogen27 += Digits[math.floor(random.random() * 12)]
    return Hydrogen27
while __name__ == "__main__" :     
    print('',generateHydrogen27())

#The End of CODE