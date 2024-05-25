import random
LETTERS=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMBERS=['0','1','2','3','4','5','6','7','8','9']
SYMBOLS=['~','!','@','#','$','%','^','&','*','(',')','{','}']
passwd_list=[]
N_LETTERS=int(input("How many letters do you need in your passwd?\n"))
N_NUMBERS=int(input("How many numbers do you need in your passwd?\n"))
N_SYMBOLS=int(input("How many  symbols do you need in your passwd?\n"))
for i in range(1,N_LETTERS+1):
    ch= random.choice(LETTERS)
    passwd_list+=ch
for i in range(1,N_NUMBERS+1):
    ch= random.choice(NUMBERS)
    passwd_list+=ch
for i in range(1,N_SYMBOLS+1):
    ch= random.choice(SYMBOLS)
    passwd_list+=ch


random.shuffle(passwd_list)

passwd=""
for ch in  passwd_list:
    passwd+=ch
    

print("your password is:",passwd)
