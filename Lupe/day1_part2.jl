using DelimitedFiles

# doing a hello world, because why not
println("hello world")

# reading the input 
data = readdlm("input_day1",Int)

#loop through the elements in the array
for i in eachindex(data)
  #select number in the array  
   n1 = data[i]   
   data2 = data[i:end]

   #compare (sum) with the rest of the numbers in the array
   for j in eachindex(data2)
     n2 = data2[j] 
     data3 = data2[j:end]

     for k in eachindex(data3)    
        n3 = data3[k]
        sum = n1 + n2+ n3
        if sum == 2020
           println(n1)
           println(n2)
           println(n3)
           println(n1*n2*n3)
        end

     end
   end

end

