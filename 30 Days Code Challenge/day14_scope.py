class Difference:
    """
    Task:
    Complete the Difference class by writing the following:
    - A class constructor that takes an array of integers as a parameter and
      saves it to the `__elements` instance variable.
    - A computeDifference method that finds the maximum absolute difference
      between any 2 numbers in __elements and stores it in the
      `maximumDifference` instance variable.
    """
    def __init__(self, a):
        self.__elements = a

    maximumDifference = int()

    def get_elements(self):
        return self.__elements

    def computeDifference(self):
        array = self.get_elements()
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i] != array[j] and\
                    Difference.maximumDifference <= abs(array[i] - array[j]):
                    Difference.maximumDifference = abs(array[i] - array[j])
                else: pass

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
