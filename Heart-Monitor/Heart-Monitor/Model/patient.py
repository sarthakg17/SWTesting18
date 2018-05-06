# Author : Tanjina Islam
# Creation Date : 3rd May, 2018

class Patient:
    def __init__(self, name, age, pulse, oxygen_level, sistolic_bp, diastolic_bp):
        self.name = name
        self.age = age
        self.pulse = pulse
        self.oxygen_level = oxygen_level
        self.sistolic_bp = sistolic_bp
        self.diastolic_bp = diastolic_bp


    @property
    def patient_name(self):
        return str(self.name)

    @property
    def patient_age(self):
        return str(self.age)

    @property
    def patient_pulse(self):
        return str(self.pulse) + ' bpm'

    @property
    def patient_oxygen_level(self):
        return str(self.oxygen_level) + ' mm Hg'

    @property
    def patient_blood_pressure(self):
        return str(self.sistolic_bp) + '/' + str(self.diastolic_bp) + ' mm Hg'