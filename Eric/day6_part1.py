#Day6 Part1 Custom Customs

f=open("input_day6.txt")
#f=open("input_test_day6.txt")
lines=f.readlines() #read in each line
f.close()
#print("lines\n",lines)

length=0
numgroups=0
declar=[]
for row in lines:
    declar.append(str(row))  #move into new list for easier manipulation
    length+=1
#print("input:",declar)

for row in declar:
    if(row=='\n'):
        numgroups+=1

print("Length:",length,"# Groups:",numgroups) #I added a blank line at the end of test input, be sure to add one to end of real input!!!

def count(dec):
    
    group=""
    rep=[]
    repL=0
    num=0
#    dig=0
    l=0
    summ=0
    unique=[]
    str=""

    for row in dec:
        if(row!='\n'):
            #row.replace('\n',"")
            
            wor=row.split("\n")
#            print("wor:",wor)
            



            group+=wor[0]
            num+=1
#            print(num,group)

        else:

#            print("group reply:",group)
            
            yes=len(set(group))
#            print("yeses:",yes)

            summ+=yes

            group=""
    

    return summ
#            for gr in grouprep:
#                repL+=len(gr)
#                print("group reply length:",repL)
            



counts=count(declar)
print("The sum of the counts is:",counts)

