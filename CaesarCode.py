#CaesarCode.py
org = input()
enc = ''
for i in range(len(org)):
    if (ord(org[i])>64 and ord(org[i])<91)：
        value = ord(org[i])-64
        charEnc = (value+3)%26+int((value+3)/26)+64
        if ord(org[i])<88:
            enc += chr(charEnc)
        else:
            enc += chr(charEnc-26)           
    elif (ord(org[i])>96 and ord(org[i])<122):
        value = ord(org[i])-96
        charEnc = (value+3)%26+int((value+3)/26)*26+96
        if ord(org[i])<120:
            enc += chr(charEnc)
        else:
            enc +=chr(charEnc-26)
    else:
        enc += org[i]        
print(enc)

#Answer:
s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z': 
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
    elif 'A'<=c<='Z':
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
    else:
        t += c
print(t)
