#find row based on the code, to improve this function
# and the find_column could do a hi_lo funtion
# and then call that for both find_row and find_column

function find_row(code)
  row_code = code[1:7]
  lo_n = 0
  hi_n = 127

  count = 1  

  for i in row_code 
     #find the bounds of the range depending if we can the upper or lower half
     if i =='F'
        hi_n = lo_n + div(hi_n+1 - lo_n,2) - 1
        if count == 7
           return hi_n
        end     
     else
        lo_n = lo_n + div(hi_n+1 - lo_n,2)
        if count == 7 
           return lo_n
        end   
     end
     
    count += 1

  end

  return 1
end

function find_column(code)
  col_code = code[8:end]

  lo_n = 0
  hi_n = 7

  count = 1  

  for i in col_code 
    
     if i =='L'
        hi_n = lo_n + div(hi_n+1 - lo_n,2) - 1
        if count == 3
           return hi_n
        end     
     else
        lo_n = lo_n + div(hi_n+1 - lo_n,2)
        if count == 3 
           return lo_n
        end   
     end
     
    count += 1

  end
  

  return 1
end



using DelimitedFiles

# reading the input
data = readdlm("input_day5")

max_id = 0

for temp_code in data
   r = find_row(temp_code)
   c = find_column(temp_code) 

   #calculate id
   id = r*8 + c
   
   #find max id
   if id > max_id
     global max_id = id
   end
   
end

println(max_id)


