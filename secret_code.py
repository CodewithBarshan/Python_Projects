#code for turning your message into a secret code
inp=input("Enter your secret message to Encode:  ")
import random
#F=random.choice(["hjd","sks","wdx","xsa","xsa","mal","pqk","pla","Sax","xAA","xae"])
#L=random.choice(["mkc","sos","xoq","xom","jbc","coo","Cps","msk","mmc","pqd","lcj","lqb"])

#if len(inp)>=3:
    #inp=inp+inp[0]
    #rem=inp[1:] 
    #encode_msg=F+rem+L
    #print(encode_msg)

#else:
    #pass    
#code for decoding secret message

if len(inp)<3:
    rev=inp[::-1]
    print(rev)
else:
    output=inp[3:-3]
    final=output[-1]+output
    re=final[:-1]
    print(re)           