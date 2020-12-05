using DelimitedFiles

data= readdlm("input_day2", '\n')

valid_pass = 0

for line in data

   i1 = findfirst(isequal('-'),line)
   i2 = findfirst(isequal(' '),line)

   #get minimum number of occurrences
   min_o = parse(Int, line[1:i1-1])
   #get maximum number of occurrences
   max_o = parse(Int, line[i1+1:i2-1])

   letter = line[i2+1]
   password = line[i2+4:end]

   rx = Regex(string(letter))
   m = eachmatch(rx,password)
   ocurrences = size(collect(m))[1]

   if  min_o <= ocurrences <= max_o 
     global  valid_pass += 1
   end

end

println(valid_pass)
