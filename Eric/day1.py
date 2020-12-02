#Day 1 - find the two expenses that add to 2020 and then multiply them. Return the product.

f = open('input_day1.txt', 'r')
lines = f.readlines()
#print(lines)
f.close()

#print(len(lines))

expenses=[]
i=0
for number in lines:
    #print(int(number))
    expenses.append(int(lines[i]))
    #print(expenses[i])
    i=i+1
#print("expenses list ",expenses[:])
#print("count = ",i)
i=0
j=1
k=2
for i in range(len(expenses)):
    #print('i',i)
    for j in range(len(expenses)):
        #print('j',j)
        year=expenses[i]+expenses[j]
        
        if (year ==2020):
            num1=expenses[i]
            num2=expenses[j]
            break
        j=j+1
    if (year ==2020):
        break
    i=i+1
print(num1,' + ',num2,' = ',year)
print(i,",",j)
print('Part 1 product is: ',num1*num2)

i=0
j=1
k=2
for i in range(len(expenses)):
    #print('i',i)
    for j in range(len(expenses)):
        #print('j',j)
        for k in range(len(expenses)):
            #print('k',k)
            year=expenses[i]+expenses[j]+expenses[k]
        
            if (year ==2020):
                num1=expenses[i]
                num2=expenses[j]
                num3=expenses[k]
                break
            k=k+1
        if(year==2020):
            break
        j=j+1
    if (year ==2020):
        break
    i=i+1
print(num1,' + ', num2,' + ',num3,' = ',year)
print(i,",",j,",",k)
print('Part 2 product is: ',num1*num2*num3)
