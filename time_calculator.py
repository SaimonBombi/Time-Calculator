def add_time(start, duration, day = False):
    #striping time
    splitstart = start.split(":")
    hoursstart = int(splitstart[0])
    splitstart1 = splitstart[1].split()
    minutesstart = int(splitstart1[0])
    amorpmstart = splitstart1[1]
    splitduration = duration.split(":")
    hoursduration = int(splitduration[0])
    minutesduration = int(splitduration[1])
    dayslater = 0
    newhoursintoamorpm = 0
    newminutesintohours = 0

    if (minutesstart + minutesduration) < 60:
        newminutes = minutesstart + minutesduration
    elif (minutesstart + minutesduration) > 60:
        newminutes = minutesstart + minutesduration
        newminutesintohours = int(newminutes / 60)
        newminutes = (newminutes - (newminutesintohours * 60))
    if (hoursstart + hoursduration + newminutesintohours) < 12:
        newhours = hoursstart + hoursduration + newminutesintohours
        amorpmnew = amorpmstart
    elif (hoursstart + hoursduration + newminutesintohours) == 12:
        newhours = hoursstart + hoursduration + newminutesintohours
        if amorpmstart == "AM":
            amorpmnew = "PM"
        elif amorpmstart == "PM":
            amorpmnew = "AM"
    elif (hoursstart + hoursduration + newminutesintohours) > 12:
        newhours = hoursstart + hoursduration + newminutesintohours
        newhoursintoamorpm = int(newhours / 12)
        newhours = (newhours - (newhoursintoamorpm * 12))
        if newhours == 0 :
            newhours = 12
        if newhoursintoamorpm % 2 != 0:
            if amorpmstart == "AM":
                amorpmnew = "PM"
            elif amorpmstart == "PM":
                amorpmnew = "AM"
        else:
            amorpmnew = amorpmstart

    if len(str(newminutes)) == 1:
        newminutes = "0" + str(newminutes)
    if newhoursintoamorpm >= 2 :
        dayslater = round(newhoursintoamorpm / 2)


    new_time = str(newhours) + ":" + str(newminutes) + " " + amorpmnew

    if amorpmstart == "PM" and amorpmnew == "AM":
        new_time = str(newhours) + ":" + str(newminutes) + " " + amorpmnew + " (next day)"

    if dayslater == 1:
        new_time = str(newhours) + ":" + str(newminutes) + " " + amorpmnew + " (next day)"

    if dayslater > 1:
        new_time = str(newhours) + ":" + str(newminutes) + " " + amorpmnew + " (" + str(dayslater) + " days later)"

#Days of the week
    if day != False:
        day = day.lower()
        if day == "sunday":
            numday = 0
        elif day == "monday":
            numday = 1
        elif day == "tuesday":
            numday = 2
        elif day == "wednesday":
            numday = 3
        elif day == "thursday":
            numday = 4
        elif day == "friday":
            numday = 5
        elif day == "saturday":
            numday = 6

        if dayslater == 0 :
            newday = day.capitalize()
            numnewday = numday
            new_time = str(newhours) + ":" + str(newminutes) + " " + amorpmnew + ", " + newday
        elif dayslater > 0 :
            numnewday = numday + dayslater
            if 6 < numnewday < 13:
                numnewday = numnewday - 7
            elif 13 <= numnewday < 20:
                numnewday = numnewday - 14
            elif 20 <= numnewday < 27:
                numnewday = numnewday - 21
            elif 27 <= numnewday < 34:
                numnewday = numnewday - 28

        if numnewday == 0:
            newday = "Sunday"
        elif numnewday == 1:
            newday = "Monday"
        elif numnewday == 2:
            newday = "Tuesday"
        elif numnewday == 3:
            newday = "Wednesday"
        elif numnewday == 4:
            newday = "Thursday"
        elif numnewday == 5:
            newday = "Friday"
        elif numnewday == 6:
            newday = "Saturday"

        #new_time = str(newhours) + ":" + str(newminutes) + " " + amorpmnew + ", " + newday

        if dayslater == 1:
            new_time = str(newhours) + ":" + str(newminutes) + " " + amorpmnew + ", " + newday + " (next day)"
        if dayslater > 1:
            new_time = str(newhours) + ":" + str(newminutes) + " " + amorpmnew + ", " + newday + " (" + str(dayslater) + " days later)"


    return new_time
