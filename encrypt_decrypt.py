import string


alpha = string.ascii_lowercase

def encrypt(s, num):
    s.lower()
    s_list = list(s)
    encrypted = []
    for i in s_list:
        if i in alpha:
            ascii = ord(i)
            ascii += num
            alphabet = chr(ascii)
            encrypted.append(alphabet)
        else:
            encrypted.append(i)
    print(''.join(encrypted))
    return(''.join(encrypted))


def decrypt(s, num):
    s.lower()
    s_list = list(s)
    decrypted = []
    for i in s_list:
        if i in alpha:
            ascii = ord(i)
            ascii -= num
            alphabet = chr(ascii)
            decrypted.append(alphabet)
        else:
            decrypted.append(i)
    print(''.join(decrypted))


def brut(s):
    s.lower()
    s_list = list(s)
    decrypted = []
    for num in range(26):
        for i in s_list:
            if i in alpha:
                ascii = ord(i)
                ascii -= num
                alphabet = chr(ascii)
                decrypted.append(alphabet)
            else:
                decrypted.append(i)
        print(''.join(decrypted))
        del decrypted[:]

num =2
encrypted = encrypt("sanket.bondre", num)
decrypt(encrypted,num)
brut(encrypted)
