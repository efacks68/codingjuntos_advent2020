#Day 5 part1

f=open("input_day5.txt")
#f=open("input_day5_test.txt")
lines=f.readlines() #read in each line
f.close()
#print("lines\n",lines)
length=0
seats=[]
for row in lines:
    seats.append(str(row))  #move into new list for easier manipulation
    length+=1
#print("seats",seats)

#definitions:
rows=128
columns=8
#check if these should be -1 to account for the 0 place(?)

row=0
column=0
seatID=0
ghe=[]
ghef=[]

#print(rows)

def whatseat(seat):
    
    for line in seat:
#        print(line)

        if(line[0]=="F"):
            row=0
#            print(row)
        elif(line[0]=="B"):
            row=64
#            print(row)
        else:print("-")

        if(line[1]=="F"):
            row+=0
#            print(row)
        elif(line[1]=="B"):
            row+=32
#            print(row)
        else:print("-")

        if(line[2]=="F"):
            row+=0
#            print(row)
        elif(line[2]=="B"):
            row+=16
#            print(row)

        if(line[3]=="F"):
            row+=0
#            print(row)
        elif(line[3]=="B"):
            row+=8
#            print(row)

        if(line[4]=="F"):
            row+=0
#            print(row)
        elif(line[4]=="B"):
            row+=4
#            print(row)

        if(line[5]=="F"):
            row+=0
#            print(row)
        elif(line[5]=="B"):
            row+=2
#            print(row)

        if(line[6]=="F"):
            row+=0
#            print(row)
        elif(line[6]=="B"):
            row+=1
#            print(row)

#column

        if(line[7]=="L"):
            column=0
#            print("1",column)
        elif(line[7]=="R"):
            column=4
#            print("1",column)

        if(line[8]=="L"):
            column+=0
#            print("2",column)
        elif(line[8]=="R"):
            column+=2
#            print("2",column)

        if(line[9]=="L"):
            column+=0
#            print("3",column)
        elif(line[9]=="R"):
            column+=1
#            print("3",column)

#        print("row:",row,"column:",column)
#        print("Product:",row*8+column)
        prod=row*8+column
   #     print(prod)
        ghe.append(prod)
   # print(ghe)
    return ghe


ghef=whatseat(seats)
maxim=max(ghef)
#print("Maximum ID:",maxim)

ghef.sort()

print("Inputs:",ghef)


mini=53
maxi=897

#print(mini,maxi)

i=0
potent=[]
for i in range(127):
    for j in range(7):
        potent.append(i*8+j)
#       print(i,j,i*8+j)
poten=[]
potent.sort()
#print(potent)

#for row in potent:
#    if row not in ghef:
#        poten.append(row)

#print("potential",poten)
#poten.sort()
i=0
num=0
#print(poten)
for item in potent:
#    print("potent",item)
    for seat in ghef:
#        print(seat)
        if (item==seat):
            potent[num]=0
#            print(potent[num])
            num+=1
#            if(num==30):break
#    if(num==30):break



print("leftover",potent)










