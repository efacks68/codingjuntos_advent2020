function valid(string_to_validate)
   is_valid = true
     
   req_words  = ["byr","iyr","eyr","hgt", "hcl", "ecl", "pid"] 
   
   for word in req_words
       if ! occursin(word, string_to_validate)
          is_valid = false
       end
   end     

   return is_valid
end

f = open("input_day4","r")

temp_s = ""
valid_p = 0

#note that I modified my inputs to have an empty line at the end
for lines in readlines(f)
   #if not empty line concatenate de string with space
   if lines != ""  
      global temp_s = temp_s*" "*lines
   else
      #println(temp_s)
      if valid(temp_s)
         global valid_p += 1 
      end
      global temp_s = ""
      
   end 
end

println(valid_p)
