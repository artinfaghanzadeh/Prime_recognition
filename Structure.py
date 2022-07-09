#First : improt the package.
import Prime_Recognition
#Second : Run.
try:
    input_number = int(input("Please entern number for solve : "))
    if input_number < 0 :
        print("This number that you choose is negative number.")
    elif input_number > 0 and input_number != 0 and input_number != 1 :
        print("The number that you choose is", '\x1b[6;30;42m' +Prime_Recognition.prime_r(input_number) + '\x1b[0m', "number.")
    elif input_number == 0 or input_number == 1:
        print(Prime_Recognition.prime_r(input_number))
except:
    print("Error.")
