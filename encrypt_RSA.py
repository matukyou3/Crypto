import math
import sys


def lcm(n,m):
    return n*m // math.gcd(n,m)

def generate_key(p,q):
    n=p*q
    L = lcm(p-1,q-1)
    for i in range(2,L):
        if math.gcd(i,L)==1:
            E = i
            break
        
    for i in range(2,L):
        if (E*i)%L ==1:
            D = i
            break
    return (E,n),(D,n)
    
def encrypt(pub_key,text):
    E,N = pub_key
    plain_int =[ord(char) for char in text]
    encrypted_int = [pow(i,E,N) for i in plain_int]
    encrypted_text = ''.join(chr(i) for i in encrypted_int)
    
    return encrypted_text
    
def sanitize(encrypted_text):
    return encrypted_text.encode('utf-8', 'replace').decode('utf-8')

if __name__ == '__main__':
    p=13
    q=19
    
    pub_key,priv_key = generate_key(p,q)
    plain_text = 'Hello World!!!!'
    encrypted_text = encrypt(pub_key,plain_text)
    decrypted_text = encrypt(priv_key,encrypted_text)

    print(f'''
          秘密鍵: {pub_key}
          公開鍵; {priv_key}
          
          平文: {plain_text}
          暗号文:{sanitize(encrypted_text)}
          復号分:{decrypted_text}
          '''[1:-1])
