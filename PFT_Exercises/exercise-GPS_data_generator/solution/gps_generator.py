import random

if __name__ == '__main__':
    # Set start values
    latitude = 59.47399
    longitude = 18.27499
    # open file and write first line
    # '\n' writes a line break / end of line character
    f = open('route.log', 'w')
    f.write('type,latitude,longitude\n')

    for i in range(20):
        # Create random diff numbers between 0.005 and -0.005
        y_diff = 0.005 - random.random() / 100
        x_diff = 0.005 - random.random() / 100
        # Modify the coordinate
        latitude += y_diff
        longitude += x_diff
        # Write to file
        f.write('T,' + str(latitude) + ',' + str(longitude) + '\n')

    # Close the file when we're done with it
    f.close()
