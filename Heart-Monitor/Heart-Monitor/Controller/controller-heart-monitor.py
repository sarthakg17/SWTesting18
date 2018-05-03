from .. Simulation import simulation
from faker import Faker


print ("*** Select patient from the list to monitor his/her heart beat ***")


# Print patient list
print("Patient ID :\t" + "Patient Name")
print("--------------------------------------------")
count = 1

# Create Patient Name
fake = Faker('nl_NL')
fake.random.seed(54321)

patients = simulation.SimulationTest.setUp(fake)



# print(patients)
for patient in  patients:
    print("\t" + str(count) + "\t" + patient.patient_name)
    count = count + 1

# Prompt for user input

patient_record = input("Type patient ID to check his/her record: ")

try:
   val = int(patient_record)
except ValueError:
   print("That's not an int! Type Integer ID")
   patient_record = input("Type patient ID to check his/her record: ")

# Create patient record


# patientRecords = {'1': {'name': 'Robert', 'age': '45', 'pulse': '69', 'oxygenlevel': '88', 'bloodpressure': {'systolic': '100', 'diastolic': '67'} },'2': {'name': 'Smith', 'age': '50', 'pulse': '50', 'oxygenlevel': '75', 'bloodpressure': {'systolic': '120', 'diastolic': '70'} }}

# print("Patient's ID: " + str(patient_record))
# print("Patient's Name: " + patientRecords[str(patient_record)]['name'])
# print("Age: " + patientRecords[str(patient_record)]['age'])


patientRecords = {}

for a, b in enumerate(patients):
    patientRecords[a+1] = b

# for key, value in patientRecords.items() :
    # print (key, value)

for id in patientRecords.keys():
    # print(id)
    # print(patient_record)
    # print(patientRecords[id])

# need to match key with user input somehow!!! Now it's not working
    if id == patient_record:
        print(id)
        print(patient_record)
        print(patientRecords[id].patient_name)