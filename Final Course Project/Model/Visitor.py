import Base_Person
import weakref


class Visitor(Base_Person):
    # A Class variable to hold the instances count
    VISITOR_COUNT = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        # Increment the number of patients every time a new instance is created
        Visitor.VISITOR_COUNT += 1

    # def main():
    # Testing with instance variables
    # doc1.__str__()
    # doc1.__dict__()

    # Get all info for an instance
    # print(doctor1.__dict__)
    # print(MedicalSpecialist.__dict__)
    # Exploratory testing

    # To-DO Switch Case for checking user.physical_state for pain indicator patterns: "No", "chronic", "acute"
    # result = re.match("Chronic pain", self.get_Pain_State())
    # findAll -> returns a list of all matches
