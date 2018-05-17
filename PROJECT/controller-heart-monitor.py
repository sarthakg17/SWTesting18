# Author : Tanjina Islam
# Creation Date : 3rd May, 2018

#from .. Simulation import simulation
#import simulation
#from faker import Faker
import time
import sys
import json

def checkPulse(pulse):
    if int(pulse) < 60:
        print ('WARNING: PULSE IS TOO LOW : ' + str(pulse) +  ' beats per minute')
    elif int(pulse) >= 100:
        print ('WARNING: PULSE IS TOO HIGH : ' + str(pulse) +  ' beats per minute')

    return

def checkOxygenLevel(oxygen):
    if int(oxygen) < 80:
        print ( 'WARNING: OXYGEN LEVEL IS TOO LOW : ' + str(oxygen) +  ' millimeters of mercury')
    elif int(oxygen) > 100:
        print ('WARNING: OXYGEN LEVEL IS TOO HIGH : ' + str(oxygen) +  ' millimeters of mercury')
    return

def checkBloodPressure(systolic, diastolic):
    if int(systolic) > 120 and int(systolic) < 130  and int(diastolic) < 80:
        print ('Blood pressure is elevated : ' + str(systolic) + '/' + str(diastolic) +  ' mm Hg')
    elif int(systolic) > 130 and int(systolic) < 140 or int(diastolic) > 80 and int(diastolic) < 90:
        print ('WARNING: HIGH BLOOD PRESSURE : ' + str(systolic) + '/' + str(diastolic) +  ' mm Hg')
    elif int(systolic) > 140 or int(diastolic) > 90:
        print ('WARNING: HIGH BLOOD PRESSURE STAGE 2 : ' + str(systolic) + '/' + str(diastolic) +  ' mm Hg')
    elif int(systolic) > 180 or int(diastolic) > 120:
        print ('WARNING: HIGH BLOOD PRESSURE HYPERTENSIVE CRISIS : ' + str(systolic) + '/' + str(diastolic) +  ' mm Hg')

    return


# Prompt for user input

def user_input():

  ### Need to check for Incalid input (for example : 0, > 10 -1) ###

  patient_record = input("Type patient ID to check his/her record: ")

  try:
    val = int(patient_record)
  except ValueError:
    print("That's not an int! Type Integer ID")
    patient_record = input("Type patient ID to check his/her record: ")

  return patient_record



# Simulate 10 patients



#fake = Faker('nl_NL')
#fake.random.seed(54321)
#patients = simulation.SimulationTest.setUp(fake)

patients = ["Olivia Dorsman-Phillipsen", "Leah Schwartsbach", "Amelia Ehlert-Helmerhorst", "Benjamin Boudewijns-van Geest", "Janne Linschoten",
"Jade van Brenen", "David Smit", "Rayan Krabbe-Verkade", "Hidde van Oosten-van Breukelveen", "Helena der Kijnder"]

# print(patients)
def print_patient_list():
  print ("*** Select patient from the list to monitor his/her heart beat ***")
  # Print patient list
  print("Patient ID :\t" + "Patient Name")
  print("--------------------------------------------")
  print(patients)
  count = 1
  for i in  range(0, len(patients)):
    print("\t" + str(count) + "\t" + patients[int(i)])
    count = count + 1

print_patient_list()    

# Prompt for user input

patient_record = user_input()

patientRecords = {'1': {'name': 'Olivia Dorsman-Phillipsen', 'age': '45', 'pulse': '69', 'oxygenlevel': '88', 'bloodpressure': {'systolic': '100', 'diastolic': '70'} },
 '2': {'name': 'Leah Schwartsbach', 'age': '50', 'pulse': '50', 'oxygenlevel': '75', 'bloodpressure': {'systolic': '120', 'diastolic': '80'} },
  '3': {'name': 'Amelia Ehlert-Helmerhorst', 'age': '50', 'pulse': '50', 'oxygenlevel': '75', 'bloodpressure': {'systolic': '120', 'diastolic': '70'} },
   '4': {'name': 'Benjamin Boudewijns-van Geest', 'age': '50', 'pulse': '53', 'oxygenlevel': '95', 'bloodpressure': {'systolic': '140', 'diastolic': '90'} },
    '5': {'name': 'Janne Linschoten', 'age': '28', 'pulse': '89', 'oxygenlevel': '75', 'bloodpressure': {'systolic': '120', 'diastolic': '70'} },
     '6': {'name': 'Jade van Brenen', 'age': '40', 'pulse': '50', 'oxygenlevel': '75', 'bloodpressure': {'systolic': '110', 'diastolic': '80'} },
      '7': {'name': 'David Smit', 'age': '35', 'pulse': '70', 'oxygenlevel': '67', 'bloodpressure': {'systolic': '140', 'diastolic': '100'} },
       '8': {'name': 'Rayan Krabbe-Verkade', 'age': '58', 'pulse': '50', 'oxygenlevel': '72', 'bloodpressure': {'systolic': '90', 'diastolic': '50'} },
        '9': {'name': 'Hidde van Oosten-van Breukelveen', 'age': '50', 'pulse': '50', 'oxygenlevel': '75', 'bloodpressure': {'systolic': '120', 'diastolic': '70'} },
         '10': {'name': 'Helena der Kijnder', 'age': '38', 'pulse': '68', 'oxygenlevel': '67', 'bloodpressure': {'systolic': '110', 'diastolic': '70'} }}

print ('\n')
print("Patient's ID: " + str(patient_record))
print("Patient's Name: " + patientRecords[str(patient_record)]['name'])
print("Age: " + patientRecords[str(patient_record)]['age'])
print("Pulse Rate : " + patientRecords[str(patient_record)]['pulse'] +  ' bpm')
print("Oxygen Level : " + patientRecords[str(patient_record)]['oxygenlevel'] +  ' mm Hg')
print("Blood Pressure : " + patientRecords[str(patient_record)]['bloodpressure']['systolic'] + '/' + patientRecords[str(patient_record)]['bloodpressure']['diastolic'] +  ' mm Hg')
print ('----------------------------------------------------------------------------------')

print ("Initializing heart monitor")
print ('\n')
try:
    data = json.load(open("simulated-data.json"))
except:
    print ("Could not connect to sensor/could not open file simulated-data.json")
    sys.exit(1)

def monitorPatient(id):

  #if(patient_record == '1'):

    #print("Name : " + patients[int(id) - 1].patient_name)
    #print("Age : " + patients[int(id) - 1].patient_age)
    #print("Pulse Rate : " + patients[int(id) - 1].patient_pulse)
    #print("Oxygen Level : " + patients[int(id) - 1].patient_oxygen_level)
    #print("Blood Pressure : " + patients[int(id) - 1].patient_blood_pressure)
    print ('----------------------------------------------------------------------------------')

    curr = data[0][id]
    #print(curr)
    for i in range(0, 10):
      print("Pulse Rate : " + str(curr[i]['pulse']) + ' bpm')
      print("Oxygen Level : " + str(curr[i]['oxygen_level'])  + ' mm Hg')
      print("Blood Pressure : " + str(curr[i]['sistolic_bp']) + "/" + str(curr[i]['diastolic_bp'])  + ' mm Hg')
      print ('\n')
      checkPulse(curr[i]['pulse'])
      checkOxygenLevel(curr[i]['oxygen_level'])
      checkBloodPressure(curr[i]['sistolic_bp'],curr[i]['diastolic_bp'])
      print ('----------------------------------------------------------------------------------')
      time.sleep(1)

  

    time.sleep(2)
    print ('End of sequence, turning off heart monitor for patient ' + str(id))

#while (patient_record != None):
#if(patient_record == null):
 # print("Type Integer ID")
#if(int(patient_record) <= int(0) and int(patient_record) > int(10)):
 # print("Type valid Id")

monitorPatient(patient_record)

print ('----------------------------------------------------------------------------------')

### NEED To implement something like while true with exit condition ###

print ('\n')
print ('Continue Monitoring....')
print ('\n')

# print(patients)
print_patient_list()
 
# Prompt for user input

patient_record = user_input()
monitorPatient(patient_record)

### NEED To implement something like while true with exit condition ###
