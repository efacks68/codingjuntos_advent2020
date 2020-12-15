#function that returns array with the bags
#that contain the color we are searching for
function contain_color(color, bags)
  
   bags_containing_color = ""   

   for bag in bags
      if occursin(color, bag)

        #get what is before "contain"
        m = match(r".+(?= contain)",bag) 
        before = m.match
        
        if !occursin(color,before)
 
           #get what is after "contain"
           #m = match(r"(?<=contain ).+",bag)
           #after = m.match
 
           #append the name of bag containing color
           bags_containing_color= bags_containing_color * before
        end

         
                 
      end
   end    
   return bags_containing_color
end

#read file
f = open("input_day7","r")

#file has 594 lines
lines = Array{String}(undef,594)

c = 1
for line in readlines(f)
   lines[c] = line
   global c += 1
end


#search for shiny gold
first_level = contain_color("shiny gold", lines)
let first_colors = split(first_level," bags")
println(first_colors)
total = length(first_colors) - 1 #account for the ""
println(total)


old_colors = first_colors


i = 1
while i < 10

   second_level_ts = ""

   #search for the ones containing the prev ones
   for color in first_colors
      if color != ""
         second_level = contain_color(color,lines)
         second_level_ts *= second_level
      end
   end

   second_colors_ts = split(second_level_ts," bags")
   second_colors =unique([s for s in second_colors_ts if !(s in old_colors)])
   println(second_colors)
   total = total + length(second_colors)
   println(total)
   first_colors = second_colors
   old_colors = vcat(old_colors,second_colors)
   
   i+= 1 
end

end #let 
