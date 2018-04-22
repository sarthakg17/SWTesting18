import json
import time
from pprint import pprint

def checkPulse(pulse):
    print "The puls is: " + pulse
    if pulse < 60:
        print 'WARNING: PULSE IS TOO LOW - ' + pulse +  ' beats per minute'
    elif pulse > 100:
        print 'WARNING: PULSE IS TOO HIGH - ' + pulse +  ' beats per minute'
    else:
        print 'Normal pulse'

    return

def checkOxygenLevel(oxygen):
    if oxygen < 80:
        print 'WARNING: OXYGEN LEVEL IS TOO LOW - ' + oxygen +  ' millimeters of mercury'
    elif oxygen > 100:
        print 'WARNING: OXYGEN LEVEL IS TOO HIGH - ' + oxygen +  ' millimeters of mercury'
    return

def checkBloodPressure(systolic, diastolic):
    if systolic > 120 and systolic < 130  and diastolic < 80:
        print 'Blood pressure is elevated - ' + systolic + '/' + diastolic +  ' mm Hg'
    elif systolic > 130 and systolic < 140 or diastolic > 80 and diastolic < 90:
        print 'WARNING: HIGH BLOOD PRESSURE - ' + systolic + '/' + diastolic +  ' mm Hg'
    elif systolic > 140 or diastolic > 90:
        print 'WARNING: HIGH BLOOD PRESSURE STADGE 2- ' + systolic + '/' + diastolic +  ' mm Hg'
    elif systolic > 180 or diastolic > 120:
        print 'WARNING: HIGH BLOOD PRESSURE HYPERTENSIVE CRISIS- ' + systolic + '/' + diastolic +  ' mm Hg'


    return


print 'Initializing heart monitor'
data = json.load(open('heartdata.json'))


# print len(data["heartdata"])
# pprint(data["heartdata"][0]["heartrate"])

for x in range(0, len(data["heartdata"])):
    curr = data["heartdata"][x]
    checkPulse(curr["pulse"])
    checkOxygenLevel(curr["oxygenlevel"])
    checkBloodPressure(curr["bloodpressure"]["systolic"],curr["bloodpressure"]["diastolic"])
    print "Normal state. Pulse: " + curr["pulse"] + ", Oxygen level: " + curr["oxygenlevel"] + ", Blood pressure: " + curr["bloodpressure"]["systolic"] + "/" + curr["bloodpressure"]["diastolic"]
    time.sleep(1)

time.sleep(2)
print 'End of sequence, turning of heart monitor'
