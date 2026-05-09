# Imports
from Admin import Admin
from Doctors import Doctor
from Patient import Patient

def save_data(admin, doctors, patients, discharged_patients):
    """Save all data to txt files"""
    # Save doctors
    try:
        with open('doctors.txt', 'w') as f:
            for doc in doctors:
                f.write(f"{doc.get_first_name()},{doc.get_surname()},{doc.get_speciality()}\n")
        print("Doctors saved successfully.")
    except Exception as e:
        print(f"Error saving doctors: {e}")
    
    # Save patients
    try:
        with open('patients.txt', 'w') as f:
            for pat in patients:
                f.write(f"{pat.get_first_name()},{pat.get_surname()},{pat.get_age()},{pat.get_mobile()},{pat.get_postcode()},{pat.get_doctor()}\n")
        print("Patients saved successfully.")
    except Exception as e:
        print(f"Error saving patients: {e}")
    
    # Save admin
    try:
        with open('admin.txt', 'w') as f:
            f.write(f"{admin.get_username()},{admin.get_password()},{admin.get_address()}\n")
        print("Admin saved successfully.")
    except Exception as e:
        print(f"Error saving admin: {e}")

def load_data():
    """Load all data from txt files"""
    doctors = []
    patients = []
    discharged_patients = []
    admin = None
    
    # Load doctors
    try:
        with open('doctors.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    doctors.append(Doctor(parts[0], parts[1], parts[2]))
        print(f"Loaded {len(doctors)} doctors.")
    except FileNotFoundError:
        print("No doctors file found. Using defaults.")
        doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    
    # Load patients
    try:
        with open('patient.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 5:
                    pat = Patient(parts[0], parts[1], int(parts[2]), parts[3], parts[4])
                    if len(parts) >= 6 and parts[5] != 'None':
                        pat.link(parts[5])
                    patients.append(pat)
        print(f"Loaded {len(patients)} patients.")
    except FileNotFoundError:
        print("No patients file found. Using defaults.")
        patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    
    # Load discharged patients
    try:
        with open('discharged_patients.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 5:
                    pat = Patient(parts[0], parts[1], int(parts[2]), parts[3], parts[4])
                    if len(parts) >= 6 and parts[5] != 'None':
                        pat.link(parts[5])
                    discharged_patients.append(pat)
        print(f"Loaded {len(discharged_patients)} discharged patients.")
    except FileNotFoundError:
        discharged_patients = []
    
    # Load admin
    try:
        with open('admin.txt', 'r') as f:
            line = f.readline()
            if line:
                    parts = line.strip().split(',')
                    if len(parts) >= 3:
                        admin = Admin(*parts[:3])
                        print("Admin loaded.")

    except FileNotFoundError:
        print("No admin file found. Using defaults.")
        admin = Admin('admin', '123', 'B1 1AB')
    
    if admin is None:
        admin = Admin('admin', '123', 'B1 1AB')
    
    return admin, doctors, patients, discharged_patients

def main():
    """The main function to be ran when the program runs"""
    
    # Load data from files
    admin, doctors, patients, discharged_patients = load_data()

    # Admin login loop
    while True:
        if admin.login():
            break
        else:
            print('Incorrect username or password.')
            retry = input('Try again? (Y/N): ').lower()
            if retry != 'y' and retry != 'yes':
                print('Goodbye!')
                return

    # Main menu loop
    running = True
    while running:
        print('\n--- Admin Menu ---')
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- Relocate patient to another doctor')
        print(' 7- View management report')
        print(' 8- Group patients by family')
        print(' 9- Save data')
        print('10- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)
          
        elif op == '2':
            # 2- View or discharge patients
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin details
            admin.update_details()

        elif op == '6':
            # 6 - Relocate patient
            admin.relocate_patient(patients, doctors)
        
        elif op == '7':
            # 7- View management report
            admin.management_report(doctors, patients)

        elif op == '8':
            # 8- Group patients by family
            admin.group_by_family(patients)

        elif op == '9':
            save_data(admin, doctors, patients, discharged_patients)
        elif op == '10':
            save_data(admin, doctors, patients, discharged_patients)
            print('Goodbye!')
            running = False
        
        else:
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
