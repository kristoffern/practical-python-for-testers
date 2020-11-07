import random
latitude = 59.5
longitude = 18.3
out = open("log.csv", "wt")
out.write("type,latitude,longitude,\n")
for i in range(200):

    latDiff = (random.random() - 0.4) * 0.2
    latitude += latDiff
    lonDiff = (random.random() - 0.5) * 0.1
    longitude += lonDiff
    if random.random() < 0.01:
        out.write("T," + latitude + ",tsrsty")
    out.write("T," + str(latitude) +
              "," + str(longitude) + '\n')
out.close()
