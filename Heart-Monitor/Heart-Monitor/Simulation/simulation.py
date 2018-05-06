
# Author : Tanjina Islam
# Creation Date : 3rd May, 2018

from faker import Faker
from  .. Model import patient

patients = []

class SimulationTest:

    def __init__(self):
        self.data = []

    def setUp(fake):
        # self.fake = Faker('nl_NL')
        # self.fake.random.seed(54321)
        for fake.patient in range(10):
            fake.patient = patient.Patient(
            name = fake.name(),
            age = fake.random.randint(20, 65), # Need to check these range I put an approximation only!!
            pulse = fake.random.randint(0,200),
            oxygen_level = fake.random.randint(0,200),
            sistolic_bp = fake.random.randint(0,200),
            diastolic_bp = fake.random.randint(0,200)
        )
            patients.append(fake.patient)
            # print(fake.patient.pulse)
        return patients


    def create_names(fake):
        # Patient Name
        for patient in range(10):
            patient = fake.name()
            patients.append(patient)
        return patients

    # print(patients)

    # To-Do : Need to add a function that can simulate bpm/bp/oxygenlevel continuously for chosen patient - each 15/30 seconds maybe!!!

    ###########################

    if __name__ == "__main__":
         fake = Faker('nl_NL')
         fake.random.seed(54321)
         # create_names(fake)
         setUp(fake)


