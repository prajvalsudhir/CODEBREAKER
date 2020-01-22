import random
gen=list(range(10))
random.shuffle(gen)
gnum=gen[:3]

def guess():
    codes=[]
    y=[]
    x=input("enter your 3 digits\n")
    for i in range(0,3,1):
        y.append(int(x[i]))

    if (y == gnum):
        return "code cracked"
    else:
        for j in range(0,3,1):
            if(y[j]==gnum[j]):
                codes.append("match")
            elif(y[j] in gnum):
                codes.append("close")
            else:
                codes.append("nope")
        return codes






while 1:
        gcode = []
        gcode = guess()
        print(gcode)
        if ("code cracked" in gcode):
            print("you have deciphered the secret code")
            exit()
        else:
         guess()
         print(gcode)
         continue











