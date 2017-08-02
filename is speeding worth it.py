

def timesaved():
    print("The units are miles, minutes, and miles per hour.")
    speedlim = input("Speed Limit: ")
    speed = input("Speed: ")
    distance = input("Distance: ")
    speedlim = float(speedlim)
    speed = float(speed)
    distance = float(distance)
    timetotal = 60 * ((distance / speedlim) - (distance / speed))
    timerem = (timetotal % 1) * 60
    timerem = timerem - (timerem % 1)
    timetotal = timetotal - timetotal % 1
    print("You would save " + str(timetotal) + " minutes and " + str(timerem) + " seconds by going %d miles per hour."
          % speed)
timesaved()
