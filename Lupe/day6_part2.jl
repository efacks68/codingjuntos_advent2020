#find how many different letters appear
#in all the persons from a group 
#here that is each string separated by space
function find_yes(group_ans)

   #split string by spaces
   #string is coming with "" in the front, and it gets caught in the split
   person_ans = split(group_ans, " ")
   
   #find shortest string    
   ans_l = [length(i) for i in person_ans if i!=""]  
   shortest_string = findmin(ans_l)
   shortest_index = shortest_string[2] + 1 #correct index due to "" being counted as element
   shortest_ans = person_ans[shortest_index]

   n_words = length(person_ans)
   occur_in_all = 0 

   #see how many times  the shortest string letters occur in 
   #the group answers, if it occurs as many times as the number
   #of total words, then it appears in all words 
   for letter in shortest_ans
      rx = Regex(string(letter))
      m = eachmatch(rx,group_ans)
      ocurrences = size(collect(m))[1]
      if ocurrences == n_words - 1 #correct because n_words counts "" as an element 
         occur_in_all += 1
      end
   end

   return occur_in_all
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

