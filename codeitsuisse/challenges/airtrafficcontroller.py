def evaluate(data):
    print(data)
    runways = False
    runwaySchedule = {}
    reserveTime = int(int(data["Static"]["ReserveTime"])/60)
    flights = sorted(data["Flights"],key = lambda info: int(info["Time"]))
    flightsCopy = flights.copy()
    answer = []

    def getTimeIndexFromFlight(flight):
        time = flight["Time"]
        hours = int(time[0:2])
        minutes = int(time[2:4])
        return hours*60 + minutes

    def getTimeFromTimeIndex(timeIndex):
        hours = int(timeIndex/60)
        minutes = int(timeIndex%60)
        return '{:0>2d}'.format(hours) + '{:0>2d}'.format(minutes)

    def getbestRunway(timeIndex):
        bestRunway = "default"
        timeToSchedule = 1440
        for runway, schedule in runwaySchedule.items():
            start = timeIndex
            count = 0
            while (count < reserveTime and start < 1440):
                if schedule[start + count]:
                    start = start + count + 1
                    count = 0
                else:
                    count += 1
            if start < timeToSchedule:
                timeToSchedule = start
                bestRunway = runway
        return bestRunway, timeToSchedule

    def schedule(flight):
        timeIndex = getTimeIndexFromFlight(flight)
        bestRunway, timeToSchedule = getbestRunway(timeIndex)
        for i in range(timeToSchedule, timeToSchedule+ reserveTime):
            runwaySchedule[bestRunway][i] = flight["PlaneId"]
        tempAns = {"PlaneId": flight["PlaneId"], "Time": getTimeFromTimeIndex(timeToSchedule)}
        if "Runways" in data["Static"]:
            tempAns["Runway"] = bestRunway
        answer.append(tempAns)


    if "Runways" in data["Static"]:
        runways = data["Static"]["Runways"]
    if runways:
        for runway in runways:
            runwaySchedule[runway] = [ None for y in range( 1440 )]
    else:
        runwaySchedule["default"] = [ None for y in range( 1440 )]

    # schedule distressed first
    for flight in flights:
        if "Distressed" in flight:
            schedule(flight)
            del flightsCopy[flights.index(flight)]

    for flight in flightsCopy:
        schedule(flight)

    print(answer)
    return {"Flights":answer}


tests = [
{
    "Flights": [
        {
            "PlaneId": "TR123",
            "Time": "0200"
        },
        {
            "PlaneId": "SQ255",
            "Time": "0210"
        },
        {
            "PlaneId": "TH544",
            "Time": "0155"
        },
        {
            "PlaneId": "BA123",
            "Time": "0212"
        },
        {
            "PlaneId": "VA521",
            "Time": "0230"
        }
    ],
    "Static": {
        "ReserveTime": "600"
    }
},
{
    "Flights": [
        {
            "PlaneId": "TR123",
            "Time": "0200"
        },
        {
            "PlaneId": "SQ255",
            "Time": "0210"
        },
        {
            "PlaneId": "TH544",
            "Time": "0155"
        },
        {
            "PlaneId": "BA123",
            "Time": "0212"
        },
        {
            "PlaneId": "VA521",
            "Time": "0230"
        }
    ],
    "Static": {
        "Runways": ["A", "B"],
        "ReserveTime": "600"
    }
},
{
    "Flights": [
        {
            "PlaneId": "TR123",
            "Time": "0200",
            "Distressed": "true"
        },
        {
            "PlaneId": "SQ255",
            "Time": "0210"
        },
        {
            "PlaneId": "TH544",
            "Time": "0155"
        },
        {
            "PlaneId": "BA123",
            "Time": "0212"
        },
        {
            "PlaneId": "VA521",
            "Time": "0230"
        }
    ],
    "Static": {
        "Runways": ["A"],
        "ReserveTime": "600"
    }
}
]
