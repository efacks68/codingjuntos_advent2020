#Day2: identify how many passwords are valid according to their policies

f=open("input_day2.txt",'r')
lines=f.readlines()
f.close()


pwd=[]
for number in lines:
    pwd.append(str(number))

sumcorrect=0
#i=0

for line in pwd:
#    print(line[0:12])
    if (line[1]=='-'):
        
        count1=int(line[0])
        #print(count1)
        count2=int(line[2])
        #print(count2)

        if(line[3]==" "):
#            print("count1=",count1,",","count2=",count2)
            char=line[4]
#            print("char is ",char)
            countch=line.count(char)-1
#            print("count=",countch)
            if(countch >= count1 and countch <= count2):
                sumcorrect=sumcorrect+1
#                print(sumcorrect)
        else:
            count2=int(line[2])*10+int(line[3])
#            print("count1=",count1,",","count2=",count2)
            if(line[4]==" "):
                char=line[5]
#                print("char is ",char)
                countch=line.count(char)-1
#                print("count=",countch)
                if(countch >=count1 and countch <= count2):
                    sumcorrect=sumcorrect+1
#                    print(sumcorrect)
    else:
        count1=int(line[0])*10+int(line[1])
        count2=int(line[3])*10+int(line[4])
#        print("count1=",count1,",","count2=",count2)
        char = line[6]
#        print("char is ",char)
        countch=line.count(char)-1
#        print("count=",countch)
        if(countch >= count1 and countch <= count2):
            sumcorrect=sumcorrect+1
#            print(sumcorrect)
#    i=i+1
#    if(i==5):break

print("Part1: number of correct passwords is: ",sumcorrect)

#Part2: The numbers are actually the position the char should be in
#print(len(pwd))
#so I found a better way to do the finding of chars rather than an if statement like in Part1, but I am not going to change Part1 bc it works and this shows my progression :)
#logic is to find the dash location and space indeces to determine what the location numbers are, then find the colon index which will allow me to run an if statement for determining if the correct char is at the desired location.
#Initially I had misread the instructions and thought it was looking for when BOTH chars were at their correct positions, but then realized that wasn't the case and added the elif and that worked!
#I really like the str.find() function and the type casting, those definintely helped a bunch, as in Day1
#I realized that when I printed line[:] it has a \n at the end so that is why it is on the same line.
#I also realized that the , in prints add spaces, which is really nice compared with other languages.

i=0
sumcorrect2=0
for line in pwd:
#    print("\n\nattempt ",i)
#    print(line[:])
    dash=line.find("-")
#    print("dash @ ",dash)
    if(dash==1):
        loc1=int(line[0])
        space=line.find(" ")
#        print("space @ ",space)
        if(space==3):
            loc2=int(line[2])
            colon=line.find(":")
            char=str(line[colon-1])
            #print(line[:])#,"loc1:",loc1,"loc2:",loc2,"char is",char)
#            print(line[:],"For:",char,"@",loc1,":",line[loc1+colon+1],"&",loc2,":",line[loc2+colon+1],",len:",len(line)-colon-3)
            if(char==line[loc1+colon+1] and char!=line[loc2+colon+1]):
                sumcorrect2=sumcorrect2+1
#                print("sum:",sumcorrect2)
            elif(char!=line[loc1+colon+1] and char==line[loc2+colon+1]):
                sumcorrect2=sumcorrect2+1
#                print("sum:",sumcorrect2)
#            else:print("--",i)
        elif(space==4):
            loc2=int(line[2])*10+int(line[3])
            colon=line.find(":")
            char=str(line[colon-1])
            #print(line[:],"loc1:",loc1,"loc2:",loc2,"char is",char)
#            print(line[:],"For:",char,"@",loc1,":",line[loc1+colon+1],"&",loc2,":",line[loc2+colon+1],",len:",len(line)-colon-3)
            if(char==line[loc1+colon+1] and char!=line[loc2+colon+1]):
                sumcorrect2=sumcorrect2+1
#                print("sum:",sumcorrect2)
            elif(char!=line[loc1+colon+1] and char==line[loc2+colon+1]):
                sumcorrect2=sumcorrect2+1
#                print("sum:",sumcorrect2)
#            else:print("--",i)
        else:
            print("space didn't work",i)
    elif(dash==2):
        loc1=int(line[0])*10+int(line[1])
        loc2=int(line[3])*10+int(line[4])
        colon=line.find(":")
        char=str(line[colon-1])
        #print(line[:],"loc1:",loc1,"loc2:",loc2,"char is",char)
#        print(line[:],"For:",char,"@",loc1,":",line[loc1+colon+1],"&",loc2,":",line[loc2+colon+1],",len:",len(line)-colon-3)
        if(char==line[loc1+colon+1] and char!=line[loc2+colon+1]):
            sumcorrect2=sumcorrect2+1
#            print("sum:",sumcorrect2)
        elif(char!=line[loc1+colon+1] and char==line[loc2+colon+1]):
            sumcorrect2=sumcorrect2+1
#            print("sum:",sumcorrect2)
#        else:print("--",i)
    else:
        print("dash didn't work",i)
    
    i=i+1
#    if(i==200):break

print("Part2: number of correct passwords is: ",sumcorrect2)
