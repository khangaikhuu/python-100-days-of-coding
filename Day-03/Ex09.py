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
print(f"L occurs {counter1}")
o = combined_name.count('o')
print(f"O occurs {counter1}")
v = combined_name.count('v')
print(f"V occurs {counter1}")
e = combined_name.count('e')
print(f"E occurs {counter1}")

love = l + o + v + e 

result = str(true) + str(love) 
print(result)

