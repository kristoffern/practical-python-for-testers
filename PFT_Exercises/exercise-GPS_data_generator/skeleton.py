#import the random module

#Set your starting coordinates

#Open a file to write into
out = open("coordinates.csv")
out.write('type,latitude,longitude\n')  # Start line

#A for loop to repeat X times
    #Random choice: North/South
  # Random choice: Up/Down, Left/Right?

  # Random difference: What difference in lat/long pos?

  # Latitude
   if up:
        latPos += latDiff
    else:
        ...
    #The same for Longitude

    #Write into the file
    output = 'T,{},{}\n'.format(latPos, longPos)
    out.write(output)
    
#Close the file to behave nicely