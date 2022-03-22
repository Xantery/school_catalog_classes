class School:
  def __init__(self, name, level, numberOfStudents):
    self.level = level
    self.name = name
    self.numberOfStudents = numberOfStudents
  
  def __repr__(self):
      return '{self.level} school named {self.name} has {self.numberOfStudents} students'.format(self=self)
    
    

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, number):
    self.numberOfStudents = number
    return self.numberOfStudents


class PrimarySchool(School):
  def __init__(self, name, level, numberOfStudents, pickupPolicy):
    self.pickupPolicy = pickupPolicy
    super().__init__(name, 'Primary', numberOfStudents)
  

  def get_pickupPolicy(self):
    return self.pickupPolicy


class HighSchool(School):
    def __init__(self, name, level, numberOfStudents, pickupPolicy):
        self.pickupPolicy = pickupPolicy
        super().__init__(name, 'High', numberOfStudents)
         
         
    def get_pickupPolicy(self):
      return self.pickupPolicy




new_school = School("89", "all", 400)
print(new_school)

primary_school = PrimarySchool("Brain", 'Parimary', 90, "With parents")
print(primary_school)
print(primary_school.get_name())
print(primary_school.get_numberOfStudents())
print(primary_school.get_level())
print(primary_school.get_pickupPolicy())


high_school = HighSchool("Step", 'scs', 450, "Free")
print(high_school)
print("School name is %s" % high_school.get_name())
print("The number of students is: %s" % high_school.get_numberOfStudents())
print("The school level is %s" % high_school.get_level())
print("The pickup policy is %s" % high_school.get_pickupPolicy())