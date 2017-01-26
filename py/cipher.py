print('''
                 ____
                |####|
                |####|
                |####|
                |####|
                |####|
                |####|
                |####|
                |####|
           _____|####|_____
          |################|
           ----------------
                  /\\
                 /  \\
                /    \\
               /      \\
              /        \\
             /          \\
            /            \\
           /___|_|__|_|___\\
          //              \\\\
         / \\     ####     / \\
        /   \\____________/   \\
       /                      \\
      /          \\##/          \\
     /___________/##\\___________\\
    /_____|________________|_____\\
   /_____________|__|_____________\\
  /_______|________________|_______\\
         |#|   |#|   |#|  |#|
         |#|   |#|   |#|  |#|
         |#|   |##3  |#|  |#|
         |#|         |##3 |#|
         |#|              |#|
         |#|              |#|
         |#|              |#|
         |#|              |#|
          3                3
bill           is             watching''')
import string,math
dL=dict(zip(string.ascii_lowercase,range(1,27)))
dL2=dict(zip(range(1,54),string.ascii_lowercase+string.ascii_lowercase))
def atbash(text):
    ret=''
    for x in text:
        ret=ret+dL2[27-(dL[x])]
    return ret
def vigenere(text,key):
    ret=''
    i=0
    for x in text:
        if x not in string.ascii_lowercase:
            ret=ret+x
        else:
            ret=ret+dL2[dL[x]+dL[key[i-math.floor(i/len(key))*len(key)]]-1]
            i=i+1
    return ret
def vigenere2(text,key):
    ret=''
    i=0
    for x in text:
        if x not in string.ascii_lowercase:
            ret=ret+x
        else:
            ret=ret+dL2[27+dL[x]-dL[key[i-math.floor(i/len(key))*len(key)]]]
            i=i+1
    return ret
def cParse(c,text):
    for x in range(len(c)):
        if c[x]=='a':
            text=atbash(text)
        if c[x]=='v':
            vigenereP=c[x+1]
            for y in range(len(c)-(x+1),len(c)):
                if c[y]=='/':
                    x=y+1
                    break
                else:
                    vigenereP=vigenereP+c[y]
        print('vigenere key: '+vigenereP)
        text=vigenere(text,vigenereP)
    return text
