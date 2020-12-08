function valid_pid(id_number)
   is_v = true
   #has to be 9 digit number to be valid
   n = match(r"[0-9]{9}",id_number)
   
   if (n == nothing) || (length(id_number)!=9)
      is_v = false 
   end

   return is_v
end

function valid_byr(year)
   is_v = true

   #has to be 4 digit 1920<number<2002 
   n = match(r"[0-9]{4}",year)
   if (n == nothing) || (length(year)!=4) 
      return is_v = false
   end       
  
   y = parse(Int,n.match)
   if (y<1920) || (y>2002)
      is_v = false
   end 

   return is_v
end

function valid_iyr(year)
   is_v = true

   #has to be 4 digit 2010<number<2020 
   n = match(r"[0-9]{4}",year)
   if (n == nothing) || (length(year)!=4)
      return is_v = false
   end       
  
   y = parse(Int,n.match)
   if (y<2010) || (y>2020)
      is_v = false
   end 

   return is_v
end

function valid_eyr(year)
   is_v = true

   #has to be 4 digit 2020<number<2030 
   n = match(r"[0-9]{4}",year)
   if (n == nothing) || (length(year)!=4) 
      return is_v = false
   end       
  
   y = parse(Int,n.match)
   if (y<2020) || (y>2030)
      is_v = false
   end 

   return is_v
end

function valid_ecl(color)
   is_v = true

   #has to be exactly one of:
   #amb blu brn gry grn hzl oth 
   n = eachmatch(r"(amb|blu|brn|gry|grn|hzl|oth)",color)
   if (size(collect(n))[1] != 1) 
      return is_v = false
   end       
  
   return is_v
end

function valid_hcl(color)
   is_v = true

   #6 characters 0-9 or a-f 
   n = match(r"[0-9a-f]{6}",color)
   if (n == nothing) || (length(color) != 6) 
      return is_v = false
   end       
  
   return is_v
end

function valid_hgt(height)
   is_v = true

   #number followed by cm  or in
   #150<height_cm<193, 59<height_in<76  
   n = match(r"\d+(?=cm)",height)
   if (n == nothing) 
      n = match(r"\d+(?=in)",height)
      if (n == nothing)
         is_v = false
      else 
         h = parse(Int,n.match)
         if (h<59) || (h>76)
            is_v = false
         end
      end
   else
      h = parse(Int,n.match)
      if (h<150) || (h>193)
         is_v = false
      end  
   end       
  
   return is_v
end


function valid(string_to_validate)
   is_valid = true
     
   req_words  = ["byr","iyr","eyr","hgt", "hcl", "ecl", "pid"]    

   for word in req_words
       if ! occursin(word, string_to_validate)
          is_valid = false
          return is_valid
       end
   end     

   m = match(r"(?<=pid:)\w+",string_to_validate)       
   if (m == nothing) || ! (valid_pid(m.match))
      is_valid = false
      return is_valid
   end

   m = match(r"(?<=byr:)\w+",string_to_validate)       
   if (m == nothing) || ! (valid_byr(m.match))
      is_valid = false
      return is_valid
   end
  
   m = match(r"(?<=iyr:)\w+",string_to_validate)       
   if (m == nothing) || ! (valid_iyr(m.match))
      is_valid = false
      return is_valid
   end

   m = match(r"(?<=eyr:)\w+",string_to_validate)       
   if (m == nothing) || ! (valid_eyr(m.match))
      is_valid = false
      return is_valid
   end

   m = match(r"(?<=ecl:)\w+",string_to_validate)       
   if (m == nothing) || ! (valid_ecl(m.match))
      is_valid = false
      return is_valid
   end

   m = match(r"(?<=hcl:#)\w+",string_to_validate)       
   if (m == nothing) || ! (valid_hcl(m.match))
      is_valid = false
      return is_valid
   end
   
   m = match(r"(?<=hgt:)\w+",string_to_validate)       
   if (m == nothing) || ! (valid_hgt(m.match))
      is_valid = false
      return is_valid
   end

   return is_valid
end

#could have done the valid one with Regex
#m = eachmatch(r"(?<=(eyr|pid):)\w+",string_to_study)
#collect(m)[1] would give "pid" and collect(m)[1].match the value after :
#size(collect(m)[1]) would return size of iterator


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
