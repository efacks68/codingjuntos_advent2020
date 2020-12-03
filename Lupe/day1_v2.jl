using DelimitedFiles

# doing a hello world, because why not
println("hello world")

# reading the input 
data = readdlm("input_day1",Int)

#would give the tuples whith numbers that summ gives 2020
#since the for is going through the whole list, it will give
#2 tuples following that condition
#I'm ok with that for now :)

numbers = [(i,j) for i in data for j in data if i+j==2020]

print("part one!")
println(numbers)
println(numbers[1][1] * numbers[1][2])

numbers = [(i,j,k) for i in data for j in data for k in data if i+j+k==2020]
println("part2")
println(numbers)
println(numbers[1][1]*numbers[1][2]*numbers[1][3])

