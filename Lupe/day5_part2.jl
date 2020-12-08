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

function create_ids()
  
  ids = zeros(Int, 128, 8)
 
  for r = 0:127
      for c = 0:7
          ids[r+1,c+1] = r*8 + c  
      end
  end 
  
  return ids
end

using DelimitedFiles

# reading the input
data = readdlm("input_day5")


#get all ids from r: 0-127 and c: 0-7
#also store corresponding r and c
all_ids = create_ids()

#get ids from the inputs
for temp_code in data
   r = find_row(temp_code)
   c = find_column(temp_code) 

   #calculate id
   id = r*8 + c
   
   #find if id is in array with all the ids
   #if so change that entry with a 0 
   loc = findfirst(isequal(id),all_ids)   
   global  all_ids[loc[1],loc[2]] = 0    
   
end


#print ids that are not a 0
for r = 0:127
    for c = 0:7
       if all_ids[r+1,c+1] != 0
          println("r: "*string(r)*" c: "*string(c))
          println(all_ids[r+1,c+1]) 
       end
    end
end




