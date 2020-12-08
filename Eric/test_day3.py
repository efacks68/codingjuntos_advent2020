#Day3: Toboggan Trajectory
#Part1: Starting in Top-Left Corner, follow a slope of Right 3 and Down 1.

f=open("test_input_day3.txt")
lines=f.readlines() #read in each line
f.close()
#print("lines\n",lines)

mnt=[]
for row in lines:
    mnt.append(str(row))  #move into new list for easier manipulation
    #print(len(row))
    length=len(row)       #find the length of each row
#print("mnt\n",mnt)
trees=0                   #sum of trees hit
i=0 #length-1                #counter for 'x' direction
j=0                       #counter for 'y' direction
#print("length=",length)

#bc apprently you have to 'rotate' your input 90 degrees to the left (?) 
#to make it look like the example(which wasn't clear!), add the j to count the rows down
#so that it can move correctly

for row in mnt:
#    print(row[:])
#    print(str(row[i]))
    if(str(row[i])=="#"):  
        trees=trees+1
        print(trees)
#    print(row[i])
    i=i+3
    if(i==32):break
    
print("num trees:",trees)
