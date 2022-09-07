print("Welcome to the Love Calculator")

name1 = input('What is your name? \n').lower()
name2 = input('What is their name? \n').lower()
combined_name = name1 + name2

t = combined_name.count('t')
print(f"T occurs {t}")
r = combined_name.count('r')
print(f"R occurs {r}")
u = combined_name.count('u')
print(f"U occurs {u}")
e = combined_name.count('e')
print(f"E occurs {e}")

true = t + r + u + e

l = combined_name.count('l')
print(f"L occurs {l}")
o = combined_name.count('o')
print(f"O occurs {o}")
v = combined_name.count('v')
print(f"V occurs {v}")
e = combined_name.count('e')
print(f"E occurs {e}")

love = l + o + v + e 

result = str(true) + str(love) 
print(result)
love_score = int(result)

if (love_score < 10) or (love_score > 90):
 print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >=40) and (love_score <=50):
 print(f"Your love score is {love_score}, you are alright together.")
else:
 print(f"Your score is {love_score}")
