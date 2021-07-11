import csv
from collections import Counter

def mean(totalweight, totalentries):
    mean = totalweight/totalentries
    print("Mean is: " + str(mean))

def median(totalentries, sorteddata):
    if totalentries % 2 == 0:
        median1 = float(sorteddata[totalentries//2])
        median2 = float(sorteddata[totalentries//2 -1])
        median = (median1+median2)/2
    else:
        median = float(sorteddata[totalentries//2])
    print("Median is: " + str(median))

def mode(sorteddata):
    data = Counter(sorteddata)
    modedataforrange = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0,
    }
    for weight, occurance in data.items():
        if 75 < weight < 85:
            modedataforrange["75-85"] += occurance
        elif 85 < weight < 95:
            modedataforrange["85-95"] += occurance
        elif 95 < weight < 105:
            modedataforrange["95-105"] += occurance
        elif 105 < weight < 115:
            modedataforrange["105-115"] += occurance
        elif 115 < weight < 125:
            modedataforrange["115-125"] += occurance
        elif 125 < weight < 135:
            modedataforrange["125-135"] += occurance
        elif 135 < weight < 145:
            modedataforrange["135-145"] += occurance
        elif 145 < weight < 155:
            modedataforrange["145-155"] += occurance
        elif 1555 < weight < 165:
            modedataforrange["155-165"] += occurance
        elif 165 < weight < 1755:
            modedataforrange["165-175"] += occurance
        moderange, modeoccurace = 0, 0
        for range, occurance in modedataforrange.items():
            if occurance > modeoccurace:
                moderange, modeoccurace = [int(range.split("-")[0]), int(range.split("-")[1])], occurance
        mode = float((moderange[0] + moderange[1]) / 2)
        print("Mode is: " + str(mode))

with open('data.csv', newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)

totalweight = 0
totalentries = len(filedata)
sorteddata = []

for persondata in filedata:
    totalweight += float(persondata[2])
    sorteddata.append(float(persondata[2]))

sorteddata.sort()


mean(totalweight, totalentries)
median(totalentries, sorteddata)
mode(sorteddata)