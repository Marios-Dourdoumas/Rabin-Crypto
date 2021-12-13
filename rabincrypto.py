#Dourdoumas Marios | ICSD: 3212017045
#Zhthma 1
import Crypto.Util.number as number
    
#Epektamenos algorithmos eukleidh apo vivlio (algorithmos 2.107)

def extended(a,b):
    #ax + by = d
    d = x = y = q = r = 0
    if(b == 0):
        d = a
        x = 1
        y = 0
        return d, x, y
    else:
        x1 = 0
        x2 = 1 
        y1 = 1
        y2 = 0
        
        while(b>0):
            q = a//b
            r = a - (q*b)
            x = x2 - (q*x1)
            y = y2 - (q*y1)
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y

        d = a
        x = x2
        y = y2
        return d,x,y
        
# dhmiourgia prwtwn arithmwn

def generator(bit):
    flag = False
    
    while (flag == False):
        p = number.getPrime(bit)
        q = number.getPrime(bit)
        
        #elegxos gia 3 mod 4
        a = p % 4
        b = q % 4
        if (a == (3 % 4) and b == (3 % 4)):
            flag = True
            
    return p,q

# synarthsh kryptografhshs
def encrypt(m,n):
    
    x = ''.join(format(ord(i),"b") for i in m)
    #print(x)   
    x = int(x,2) 
    #print(x)
    if(x < n):
        cipher = format(x,"b")    
        #print("Cipher before: {}".format(cipher))
        
        #epanalhpsh tessarwn teleutaiwn bit
        for i in range(len(cipher)-4,len(cipher)):
            cipher = cipher + cipher[i]
        
        #print("Cipher after: {}".format(cipher))
        cipher = int(cipher,2)
        #print(cipher)
        m = int(format(cipher,"d"))
        cipher = pow(m,2,n)
        
    return cipher
        
def decrypt(p,q,c,n):
    d,a,b = extended(p,q)
    message = []
    start = 0
    end = 0
    if (d==1):
        r = pow(int(c),int((p+1)/4),p)
        s = pow(int(c),int((q+1)/4),q)
        x = (a*p*s + b*q*r) % n
        y = (a*p*s - b*q*r) % n
        
        #roots = [x,-x % n,y,-y % n]
        broots = {1:format(x,"b"), 2:format(-x%n,"b"),3:format(y,"b"),4:format(-y%n,"b")}
        for i in range(1,len(broots)):
            tmp = broots[i]
            hint = tmp[-4:]
            test = tmp[-8:-4]
            if(hint == test):
                res = tmp
                decipher = res[:-4]
                res = int(res,2)
                #print("Decrypted message is: ",decipher)
                
                while (start != len(decipher)):
                    end = end + 7
                    letter = int(decipher[start:end],2)
                    letter = format(letter,"c")
                    message.append(letter)
                    
                    start = end
                
                
    return message

# main program

length = int(input("Enter bit length: "))
p,q = generator(length)

n = p * q

message = input("Enter message: ")
print("Encryption\n")
c = encrypt(message,n)
print("The encrypted message is: ",c)

print("Decryption\n")
result = decrypt(p,q,c,n)
print("The decrypted message in binary is: ",result)
