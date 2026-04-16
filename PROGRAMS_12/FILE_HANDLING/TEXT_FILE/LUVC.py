file=open("yo.txt","r")
contents=file.read()
vowels=0
consonants=0
lowercase=0
uppercase=0
for ch in contents:
    if(ch.islower()):
        lowercase+=1
    elif(ch.isupper()):
        uppercase+=1
    ch=ch.lower()
    if ch in 'aeiou':
        vowels+=1
    elif ch in 'bcdfghjklmnpqrstvwxyz':
        consonants+=1
file.close()
print("no of vowels=",vowels)
print("no of consonants=",consonants)
print("no of uppercase=",uppercase)
print("no of lowercase=",lowercase)
