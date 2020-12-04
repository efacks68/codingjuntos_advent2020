using DelimitedFiles

data= readdlm("input_day2", '\n')

valid_pass = 0

for line in data

   i1 = findfirst(isequal('-'),line)
   i2 = findfirst(isequal(' '),line)

   #position which has to have letter
   pos_1 = parse(Int, line[1:i1-1])
   #position which has to not have the letter
   pos_2 = parse(Int, line[i1+1:i2-1])

   letter = line[i2+1]
   password = line[i2+4:end]

   if password[pos_1] == letter
      if password[pos_2] != letter
         global valid_pass += 1
      end 
   else
      if password[pos_2] == letter
         global valid_pass += 1
      end 
   end
  
 
end

println(valid_pass)
