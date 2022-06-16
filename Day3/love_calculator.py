# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combinedstring = name1 + name2

lowercasestring = combinedstring.lower()

t = lowercasestring.count('t')
r = lowercasestring.count('r')
u = lowercasestring.count('u')
e = lowercasestring.count('e')

true = t + r + u + e

l = lowercasestring.count('l')
o = lowercasestring.count('o')
v = lowercasestring.count('v')
e = lowercasestring.count('e')

love = l + o + v + e

score = str(true) + str(love)

if (int(score) > 90) or (int(score) < 10): 
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (int(score) > 40) and (int(score) < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
