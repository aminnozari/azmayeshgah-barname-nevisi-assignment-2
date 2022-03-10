import math
while True:
    Opration = input("Enter What You Want Me To Do?\n1.Sin\n2.Cos\n3.Tan\n4.Cot\n5.Log\n6.Fact\n7.+\n8.-\n9.*\n10./\n11.Exit\n")
    if Opration == "11":
        break
    if Opration =="1" or Opration == "2" or Opration =="3" or Opration =="4" or Opration == "5" or Opration =="6":
        Number = int(input("Enter Your Number :"))
    else:
        Num1 = int(input("Enter Number 1 :"))
        Num2 = int(input("Enter Number 2 :"))
    if Opration == "1":
        result = math.sin(Number)
    elif Opration == "2":
        result = math.cos(Number)
    elif Opration == "3":
        result = math.tan(Number)
    elif Opration == "4":
        result = 1/math.tan(Number)
    elif Opration == "5":
        result = math.log10(Number)
    elif Opration == "6":
        result = math.factorial(Number)
    elif Opration == "7":
        result = Num1 + Num2
    elif Opration == "8":
        result = Num1 - Num2
    elif Opration == "9":
        result = Num1 * Num2
    elif Opration == "10":
        result = Num1 / Num2
    elif Opration == "11":
        print("GoodLuck")
        break
    else: 
        result = "Wrong"
    print (result)