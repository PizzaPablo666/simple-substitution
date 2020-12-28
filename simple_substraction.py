import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
ascii_letters = "abcdefghijklmnopqrstuvwxyz"
mapping = {}
encrypted = ""

msg_org = "dear participant when i was five years old i owned my first computer it was not very powerful like the machine you are using now but i was able to do more because software was better back then i am leaving this message here out of respect for your commitment to solve this very complex task years ago i learned about simple substitution and the only thing that came to my mind is that i shall make a ctf task out of this whenever i find the time this is not the message you are looking for just kidding the actual verifier is located at slash usr slash local slash libexec slash cyhubctf slash simsub you shall run the program and it will tell you what to do next follow your heart your flags might be correct only then may the force be with you"

for i in alphabet:
    mapping[i] = random.choice(ascii_letters)
    ascii_letters = ascii_letters.replace(mapping[i],'',1)

#without space
msg = msg_org.replace(" ","")

#cipher
i = 0
while i < len(msg):
    encrypted += mapping[msg[i]]
    i+=1

#check if the key exists
pairs = {}
key = ""

for i in mapping.values():
    key+=i

file1 = open("keys","r+")
Lines = file1.readlines()

valid = True
striped_line = ""
count = 0

for line in Lines:
    striped_line = line
    striped_line = striped_line[:-2]
    if key == line:
        valid = False
        break
if valid:
    file1.write(key)
    file1.write("\n")
    f = open("pairs","a")
    pair = ""
    for i in mapping.values():
         pair += i
    pair+="|"
    for i in encrypted:
        pair += i
    print(encrypted)
    f.write(pair)
    f.write("\n")














