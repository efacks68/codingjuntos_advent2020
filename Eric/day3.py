#Day3: Toboggan Trajectory
#Part1: Starting in Top-Left Corner, follow a slope of Right 3 and Down 1.

f=open("input_day3.txt")
lines=f.readlines() #read in each line
f.close()
#print("lines\n",lines)
length=0
mnt=[]
for row in lines:
    mnt.append(str(row))  #move into new list for easier manipulation
    length=length+1
    width=len(row)
#print("mnt\n",mnt)
print("L:",length,"W:",width)

trees0=0                   #sum of trees hit
i=0                #counter for 'x' direction
j=0                       #counter for 'y' direction
#print("length=",length)

#bc apprently you have to 'rotate' your input 90 degrees to the left (?) 
#to make it look like the example(which wasn't clear!), add the j to count the rows down
#so that it can move correctly
count=0
for row in mnt:
#    print("row:",j,"position:",i)
#    print(row[i])
    if(row[i]=="#"):  
        trees0=trees0+1
#        print("trees1:",trees1)
    i=i+3
    j=j-1
    count=count+1
    if(i>=width):
#        print("i:",i)
        rem=i%width
#        print("rem:",rem)
        i=rem
#        print(i)
#    if(count==50):break
    
print("Part1: num trees:",trees0)

#not 5 or 9 or 102 or 100

#Part2 - find the number of trees for each of the following slopes, then multiply them together
#R1,D1
#R3,D1 (already done)
#R5,D1
#R7,D1
#R1,D2

def slope(slp,R,D,W):
    i=0
    j=0
    trees=0
    for row in slp:
#        print("row:",j,"position:",i)
#        print(row[i])
        if(D==1):
            if(row[i]=="#"):
                trees=trees+1
#                print("trees:",trees)
            i=i+R
        else:
            if((j%D)==0) :
                if (row[i]=="#"): 
                    trees=trees+1
#                   print("trees:",trees)
                i=i+R


        j=j+1
        if(i>=(W-1)):
#            print("i:",i)
            rem=i%(W-1)
#            print("rem:",rem)
            i=rem
#            print(i)
#       if(count==10):break
    print("Trees:",trees)
    return trees

trees1=slope(mnt,1,1,width)
trees2=slope(mnt,3,1,width)
trees3=slope(mnt,5,1,width)
trees4=slope(mnt,7,1,width)
trees5=slope(mnt,1,2,width)

def bulkcomment():
    """
print("Trees:",trees)

#slope2
i=0
j=0
count=0
trees2=0
for row in mnt:
#    print("row:",j,"position:",i)
#    print(row[i])
    if(row[i]=="#"):
        trees2=trees2+1
#        print("trees2:",trees2)
    i=i+5
    j=j-1
#    count=count+1
    if(i>=31):
#        print("i:",i)
        rem=i%31
#        print("rem:",rem)
        i=rem
#        print(i)
#    if(count==10):break
print("Trees2:",trees2)

#slope3
i=0
j=0
count=0
trees3=0
for row in mnt:
#    print("row:",j,"position:",i)
#    print(row[i])
    if(row[i]=="#"):
        trees3=trees3+1
#        print("trees3:",trees3)
    i=i+7
    j=j-1
#    count=count+1
    if(i>=31):
#        print("i:",i)
        rem=i%31
#        print("rem:",rem)
        i=rem
#        print(i)
#    if(count==10):break
print("Trees3:",trees3)

#slope4
i=0
j=0
count=0
trees4=0
for row in mnt:
    print("row:",j,"position:",i)
    print(row[i])
    if((j%2)==0 and row[i]=="#"):
        trees4=trees4+1
        print("trees4:",trees4)
    i=i+1
    j=j-1
#    count=count+1
    if(i>=31):
        print("i:",i)
        rem=i%31
        print("rem:",rem)
        i=rem
        print(i)
#    if(count==10):break
print("Trees4:",trees4)
"""
print("Product:",trees1*trees2*trees3*trees4*trees5)

#Not:
#Trees1: 104
#Trees: 230
#Trees2: 83
#Trees3: 98
#Trees4: 104
#Product: 20234789120

#Not:
#Trees1: 104
#Trees: 230
#Trees2: 83
#Trees3: 98
#Trees4: 50
#Product: 9728264000

#later attempt: make a function out of it by sending the i and j changes
#function done!
