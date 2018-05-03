
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
        return self.name

    @property
    def patient_age(self):
        return self.age

    @property
    def patient_pulse(self):
        return self.pulse + ' bpm'

    @property
    def patient_oxygen_level(self):
        return self.oxygen_level + ' mm Hg'

    @property
    def patient_blood_pressure(self):
        return self.patient_sistolic_bp + '/' + self.patient_diastolic_bp + ' mm Hg'