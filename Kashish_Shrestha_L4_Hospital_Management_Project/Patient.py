from Person import Person


class Patient(Person):
    """Patient class - inherits from Person"""

    def __init__(self, first_name, surname, age, mobile, postcode, illness_type='General'):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            postcode (string): postcode
            illness_type (string): Type of illness
        """
        super().__init__(first_name,surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = ['Fever', 'Cough', 'Headache','Fatigue']
        self.__illness_type = illness_type 

    def get_doctor(self) :
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile

    def get_postcode(self):
        return self.__postcode

    def get_illness_type(self):
        return self.__illness_type

    def get_symptoms(self):
        """Returns the list of symptoms"""
        return self.__symptoms

    def print_symptoms(self):
        print("Symptoms:")
        for symptom in self.__symptoms:
            print(f'- {symptom}')

    def view_doctor(self):
        """Display the assigned doctor for this patient"""
        print(f"\n-----Assigned Doctor for {self.full_name()}-----")
        if self.__doctor == 'None':
            print("No doctor assigned yet.")
        else:
            print(f"Your assigned doctor is: {self.__doctor}")

    def to_file_string(self):
        return f"{self.__first_name},{self.__surname},{self.__age},{self.__mobile},{self.__postcode},{self.__doctor},{self.__illness_type}\n"
    
    @staticmethod
    def from_file_string(line):
        parts = line.strip().split(',')
        if len(parts) >= 7:
            first_name, surname, age, mobile, postcode, doctor, illness_type = parts[:7]
            patient = Patient(first_name.strip(), surname.strip(), int(age), mobile.strip(), postcode.strip(), illness_type.strip())
            patient.link(doctor.strip())
            return patient
        elif len(parts) >= 6:
            first_name, surname, age, mobile, postcode, doctor = parts[:6]
            patient = Patient(first_name.strip(), surname.strip(), int(age), mobile.strip(), postcode.strip())
            patient.link(doctor.strip())
            return patient
        return None

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
