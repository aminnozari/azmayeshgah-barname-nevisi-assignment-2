import random
Number_Of_User_Guesses = 0
RandNumber = random.randint(1,15)
while True:
    UserNumber = int(input("Yek Add Hads Bezanid : "))
    Number_Of_User_Guesses += 1
    if  UserNumber == RandNumber:
        print("Barande Shodid :)")
        break
    elif UserNumber < RandNumber :
        print("Yek Adad Ke Bozorgtar Az Adade Hadset Bgo")
    elif  UserNumber > RandNumber :
         print("Yek Adad Ke Kochiktar Az Adade Hadset Bgo")
print("Tedad Hads Haye Shoma :", Number_Of_User_Guesses)