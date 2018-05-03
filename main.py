import json
import time
import sys
from pprint import pprint

def checkPulse(pulse):
    if int(pulse) < 60:
        print ('WARNING: PULSE IS TOO LOW - ' + pulse +  ' beats per minute')
    elif int(pulse) >= 100:
        print ('WARNING: PULSE IS TOO HIGH - ' + pulse +  ' beats per minute')

    return

def checkOxygenLevel(oxygen):
    if int(oxygen) < 80:
        print ( 'WARNING: OXYGEN LEVEL IS TOO LOW - ' + oxygen +  ' millimeters of mercury')
    elif int(oxygen) > 100:
        print ('WARNING: OXYGEN LEVEL IS TOO HIGH - ' + oxygen +  ' millimeters of mercury')
    return

def checkBloodPressure(systolic, diastolic):
    if int(systolic) > 120 and int(systolic) < 130  and int(diastolic) < 80:
        print ('Blood pressure is elevated - ' + systolic + '/' + diastolic +  ' mm Hg')
    elif int(systolic) > 130 and int(systolic) < 140 or int(diastolic) > 80 and int(diastolic) < 90:
        print ('WARNING: HIGH BLOOD PRESSURE - ' + systolic + '/' + diastolic +  ' mm Hg')
    elif int(systolic) > 140 or int(diastolic) > 90:
        print ('WARNING: HIGH BLOOD PRESSURE STADGE 2- ' + systolic + '/' + diastolic +  ' mm Hg')
    elif int(systolic) > 180 or int(diastolic) > 120:
        print ('WARNING: HIGH BLOOD PRESSURE HYPERTENSIVE CRISIS- ' + systolic + '/' + diastolic +  ' mm Hg')


    return

print ('Initializing heart monitor')
try:
    data = json.load(open('heartdata.json'))
except:
    print ('Could not connect to sensor/could not open file heartdata.json')
    sys.exit(1)

# print len(data["heartdata"])
# pprint(data["heartdata"][0]["heartrate"])

for x in range(0, len(data["heartdata"])):
    curr = data["heartdata"][x]
    checkPulse(curr["pulse"])
    checkOxygenLevel(curr["oxygenlevel"])
    checkBloodPressure(curr["bloodpressure"]["systolic"],curr["bloodpressure"]["diastolic"])
    print ("Normal state. Pulse: " + curr["pulse"] + ", Oxygen level: " + curr["oxygenlevel"] + ", Blood pressure: " + curr["bloodpressure"]["systolic"] + "/" + curr["bloodpressure"]["diastolic"])
    time.sleep(1)

time.sleep(2)
print ('End of sequence, turning of heart monitor')
