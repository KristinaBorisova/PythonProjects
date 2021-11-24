import weakref
import Base_Person

class Patient(Base_Person):
    # A Class variable to hold the instances count
    PATIENTS_COUNT = 0
    PATIENT_TITLE = "Patient"
    # Create a set for keeping track of instances
    _instance = set()

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self._instance.add(weakref.ref(self))
        Patient.PATIENTS_COUNT += 1

    @overload
     def show_details(self):
        return print( "---Patient Details--- \n" "Name:", self.name, "\n" "Age:", self.age, "\n" "Gender:", self.gender, "\n"
        )