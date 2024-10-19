# Regular Expressions in Python


import re

pattern = r"[A-Z]+acker"

text = '''
Hi! This is Saifur Rahman Udoy, I am from Bangaldesh, I am a programmer and I am currently learning
Ethical Hacking, I want ot become a ethical hacker in my life, this is my ultimate goal. and I am learning
python. my name is udoy, my email addressis srudoy436@gmail.com and my phone number is 0178299436 --- Hacker --- Lacker
'''

# match = re.search(pattern, text)
# print(match)



matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    print(text[match.span()[0] : match.span()[1]])