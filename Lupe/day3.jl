using DelimitedFiles

data= readdlm("input_day3", '\n')

horizontal = (size(data)[1])*3 
lline = length(data[1])

#number of times to repet the pattern
rep = horizontal/lline

#println(horizontal)
#println(lline)
println(rep) #it is a 32, need to automatize it

#repeat the pattern the ammount needed 
for i in eachindex(data)
   data[i] = data[i]^32
end

#horizontal index
h_i = 1

#number of trees
n_t = 0

for i in eachindex(data)
  if i < size(data)[1]
     line = data[i+1]
     global h_i += 3
     index = h_i
    
     if line[h_i] == '#'
        global n_t += 1
     end  
  end
end


println(n_t)

