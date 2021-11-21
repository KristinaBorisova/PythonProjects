# helps me to keep track of weak references and instances
import weakref

# Parent Class
class Person:
    # instance method
    def print_info_CSV_Format(self):
        return "{},{},{}".format(self.name, self.age, self.gender)

    _instance = set()

    # Initializer/constructor
    # self - a parameter that invokes the object itself
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        return print(
            "---Personal Details--- \n" "Name:", self.name, "\n" "Age:", self.age, "\n" "Gender:", self.gender, "\n"
        )

    @classmethod
    def get_instances(cls):
        dead = set()
        for ref in cls._instance:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instance -= dead


# a Method to  return the approximate waiting time for each type of person
# I need to define class attributes start, end
#   def calculate_Waiting_Time(self):
#      start_symbol = "["
#     end_symbol = "]"
#    return f"{start_symbol}{self.start}, {self.end}{end_symbol}"


class MedicalSpecialist(Person):
    # A class variable to hold the instances count
    MEDICAL_SPECIALISTS_COUNT = 0
    MEDICAL_SPECIALIST_TITLE = "Doctor"
    _instance = set()

    # TO-DO: Добави специализация за всеки лекар
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        # Increment the count every time a new instance is created
        self._instance.add(weakref.ref(self))
        MedicalSpecialist.MEDICAL_SPECIALISTS_COUNT += 1

    # /def get_title(self):
    # /  self.MEDICAL_SPECIALIST_TITLE = str(self.title)


class Patient(Person):
    # A Class variable to hold the instances count
    PATIENTS_COUNT = 0
    PATIENT_TITLE = "Patient"
    # Create a set for keeping track of instances
    _instance = set()

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self._instance.add(weakref.ref(self))
        Patient.PATIENTS_COUNT += 1


class Visitor(Person):
    # A Class variable to hold the instances count
    PATIENTS_COUNT = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        # Increment the number of patients every time a new instance is created
        Patient.PATIENTS_COUNT += 1

    # def main():
    # Testing with instance variables
    # doc1.__str__()
    # doc1.__dict__()

    # Get all info for an instance
    # print(doctor1.__dict__)
    # print(MedicalSpecialist.__dict__)

    doctor1 = MedicalSpecialist("Doc1", 31, "male")
    doctor1.show_details()

    doctor2 = MedicalSpecialist("Doc2", 30, "male")
    doctor2.show_details()

    patient1 = Patient("Martin", 25, "male")
    patient1.show_details()

    patient2 = Patient("Ivana", 35, "female")
    patient2.show_details()

    patient3 = Patient("Boyana", 29, "female")
    patient3.show_details()

    print("Number of Medical Specialists:", MedicalSpecialist.MEDICAL_SPECIALISTS_COUNT)
    for given_instance in MedicalSpecialist.get_instances():
        print(given_instance.print_info_CSV_Format())

    print("\n")

    print("Number of Patients:", Patient.PATIENTS_COUNT)
    for instance in Patient.get_instances():
        print(instance.print_info_CSV_Format())

    # Get all info for an instance
    # print(doctor1.__dict__)
    # print(MedicalSpecialist.__dict__)
