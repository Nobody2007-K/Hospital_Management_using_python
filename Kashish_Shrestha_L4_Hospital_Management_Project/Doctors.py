from Person import Person


class Doctor(Person):
    """A class that deals with the Doctor operations - inherits from Person"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        super().__init__(first_name, surname)
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    def get_speciality(self) :
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality
    
    def get_patients(self):
        return self.__patients

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_appointments(self):
        return self.__appointments
    
    def add_appointment(self, appointment):
        self.__appointments.append(appointment)

    def view_patients(self):
        """Display all patients assigned to this doctor"""
        print(f"\n-----Patients Assigned to Dr. {self.full_name()}-----")
        if len(self.__patients) == 0:
            print("No patients assigned yet.")
        else:
            print('ID |          Full Name           | Age |    Mobile     | Postcode ')
            for index, patient in enumerate(self.__patients):
                print(f'{index+1:3}| {patient.full_name():^28} | {patient.get_age():^3} | {patient.get_mobile():^13} | {patient.get_postcode():^8}')

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
