function number_of_trees(right,down)
   
   data= readdlm("input_day3", '\n')
   horizontal = div( (size(data)[1])*right, down ) 
   lline = length(data[1])

   #number of times to repet the pattern
   rep = div(horizontal,lline)+1

   #repeat the pattern the ammount needed 
   for i in eachindex(data)
      data[i] = data[i]^rep
   end

   #horizontal index
   h_i = 1

   #number of trees
   n_t = 0

   for i in Iterators.countfrom(1,down)
      i > size(data)[1]-down && break
      line = data[i+down]
      h_i += right 
      index = h_i
    
      if line[h_i] == '#'
        n_t += 1
      end  
   end

  
   return (n_t)
  
end


using DelimitedFiles

r = [ 1, 3, 5, 7, 1 ]
d = [ 1, 1, 1, 1, 2 ]
slope = zeros(5)

product = 1

for i in eachindex(r) 
   slope[i] = number_of_trees(r[i], d[i])
   global product *= slope[i]
   println(product)   
end



println(product)
