class Person:
    def __init__(self, name, id, contact_info):
        self.name = name
        self.id = id
        self.contact_info = contact_info

    def display_info(self):
        print(f"Name: {self.name}\nID: {self.id}\nContact Info: {self.contact_info}")


class Patient(Person):
    def __init__(self, name, id, contact_info):
        super().__init__(name, id, contact_info)
        self.__medical_history = []
        self.__prescriptions = []
        self.__appointments = []

    def set_medical_history(self, entry):
        self.__medical_history.append(entry)

    def get_medical_history(self):
        return self.__medical_history

    def set_prescription(self, medicine):
        self.__prescriptions.append(medicine)

    def get_prescriptions(self):
        return self.__prescriptions

    def set_appointment(self, details):
        self.__appointments.append(details)

    def get_appointments(self):
        return self.__appointments

    def display_info(self):
        super().display_info()
        print(f"Medical History: {self.__medical_history}")
        print(f"Prescriptions: {self.__prescriptions}")
        print(f"Appointments: {self.__appointments}")


class Doctor(Person):
    def __init__(self, name, id, contact_info):
        super().__init__(name, id, contact_info)
        self.assigned_patients = []

    def assign_patient(self, patient):
        if patient not in self.assigned_patients:
            self.assigned_patients.append(patient)

    def diagnose(self, patient, diagnosis):
        patient.set_medical_history(f"Diagnosis by Dr.{self.name}: {diagnosis}")
        print(f"{self.name} diagnosed {patient.name}: {diagnosis}")

    def prescribe(self, patient, medicine):
        patient.set_prescription(f"Prescribed by Dr.{self.name}: {medicine}")
        print(f"{self.name} prescribed {medicine} to {patient.name}")

    def display_patients(self):
        print(f"Dr.{self.name}'s Patients:")
        for p in self.assigned_patients:
            print(f"- {p.name} (ID: {p.id})")
            print(f"  Medical History: {p.get_medical_history()}")
            print(f"  Prescriptions: {p.get_prescriptions()}")

class GeneralDoctor(Doctor):
    def diagnose(self, patient, diagnosis):
        patient.set_medical_history(f"General diagnosis by Dr.{self.name}: {diagnosis}")
        print(f"{self.name} (General Doctor) diagnosed {patient.name}: {diagnosis}")


class SpecialistDoctor(Doctor):
    def diagnose(self, patient, diagnosis):
        patient.set_medical_history(f"Specialist diagnosis by Dr.{self.name}: {diagnosis}")
        print(f"{self.name} (Specialist Doctor) diagnosed {patient.name}: {diagnosis}")



class Staff(Person):
    def __init__(self, name, id, contact_info):
        super().__init__(name, id, contact_info)

    def schedule_appointment(self, patient, doctor, date):
        details = f"Appointment with Dr.{doctor.name} on {date}"
        patient.set_appointment(details)
        doctor.assign_patient(patient)
        print(f"Scheduled: {details}")

    def cancel_appointment(self, patient, doctor, date):
        details = f"Appointment with Dr.{doctor.name} on {date}"
        if details in patient.get_appointments():
            patient.get_appointments().remove(details)
            print(f"Cancelled: {details}")
        else:
            print("No such appointment found.")


class Hospital:
    def __init__(self, name):
        self.name = name
        self.__doctors = []
        self.__patients = []
        self.__staff = []

    def add_doctor(self, doctor):
        self.__doctors.append(doctor)

    def add_patient(self, patient):
        self.__patients.append(patient)

    def add_staff(self, staff_member):
        self.__staff.append(staff_member)

    def display_all(self):
        print(f"Hospital: {self.name}")
        print("Doctors:")
        for d in self.__doctors:
            d.display_info()
            d.display_patients()
        print("Patients:")
        for p in self.__patients:
            p.display_info()
        print("Staff:")
        for s in self.__staff:
            s.display_info()


h = Hospital("Cairo General Hospital")

d1 = GeneralDoctor("Dr. Sara", 201, "01098765432")
d2 = SpecialistDoctor("Dr. Ahmed", 202, "01012345678")
p1 = Patient("Ali", 101, "01055555555")
s1 = Staff("Mona", 301, "01099999999")

h.add_doctor(d1)
h.add_doctor(d2)
h.add_patient(p1)
h.add_staff(s1)

s1.schedule_appointment(p1, d1, "2026-02-01")
d1.diagnose(p1, "Flu")
d1.prescribe(p1, "Paracetamol")

d2.diagnose(p1, "Heart checkup")
d2.prescribe(p1, "Aspirin")

h.display_all()
