import weakref
import Base_Person


class MedicalSpecialist(Base_Person):
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
