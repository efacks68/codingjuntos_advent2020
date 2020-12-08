#find how many different letters are there
#counting same letters just once
function find_yes(group_ans)
   #remove spaces
   group_ans_no_spaces = replace(group_ans, " " => "")
   #get size of array with unique occurrences in the string
   number_of_y = length(unique(group_ans_no_spaces))
   return number_of_y
end

f = open("input_day6","r")

temp_s = ""
sum_y = 0

#note that I modified my inputs to have an empty line at the end
for lines in readlines(f)
   #if not empty line concatenate de string with space
   if lines != ""  
      global temp_s = temp_s*" "*lines
   else
      #println(temp_s)
      n = find_yes(temp_s)
      global sum_y += n 
      global temp_s = ""
      
   end 
end

println(sum_y)

