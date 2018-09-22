from datetime import time, timedelta

def evaluate(data):
    runwaySchedule = []
    runways = False
    if "Runways" in data["Static"]:
        runways = data["Static"]["Runways"]
    print(runways)
    reserveTime = data["Static"]["ReserveTime"]
    reserveTime = timedelta(seconds=int(reserveTime))

    def schedule(flight):
        flightTime = flight["Time"]
        flightTime = time(hour=int(flightTime[0:2]), minute=int(flightTime[2:4]))
        print(flightTime.strftime('%H%M'))

    def earliestLanding(flightTime, runway):
        if len(runwaySchedule[runway]) == 0:
            return flightTime
        for scheduledTime in sorted(runwaySchedule[runway]):
            if canLand(flightTime, scheduledTime):
                return flightTime


    def canLand(newLandTime, scheduledLandTime):
        if newLandTime < scheduledLandTime + reserveTime or newLandTime + reserveTime < scheduledLandTime:
            return True
        else:
            return False


    # if runways:
    #     for runway in runways:
    #         runwaySchedule[runway] = []
    # print("runwaySchedule", runwaySchedule)
    # schedule(data["Flights"][0])





tests = [
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
