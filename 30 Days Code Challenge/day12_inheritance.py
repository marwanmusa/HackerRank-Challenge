class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    """
    Task:
    You are given two classes, Person and Student, where Person is the base class
    and Student is the derived class. Completed code for Person and a declaration
    for Student are provided for you in the editor.
    Observe that Student inherits all the properties of Person.

    Complete the Student class by writing the following:
        - A Student class constructor, which has  parameters:
            1. A string, firstName.
            2. A string, lastName.
            3. An integer, idNumber.
            4. An integer array (or vector) of test scores, scores.
        - A char calculate() method that calculates a Student object's average
        and returns the grade character representative of their calculated average.
    """
    #   Class Constructor

    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    def calculate(self):
        avg_scores = sum(self.scores)/len(self.scores)
        if 90 <= avg_scores <= 100:
            return "O"
        elif 80 <= avg_scores < 90:
            return "E"
        elif 70 <= avg_scores < 80:
            return "A"
        elif 55 <= avg_scores < 70:
            return "P"
        elif 40 <= avg_scores < 55:
            return "D"
        else:
            return "T"

