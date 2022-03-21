class School:
  def __init__(self, name, level, numberOfStudents):
    self.level = level
    self.name = name
    self.numberOfStudents = numberOfStudents
  
  def __repr__(School):
    print("A {level} school named {name} with {numberOfStudents} students")
    

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



new_school = School("89", "all", 400)
#print(new_school)
#print(new_school.get_name())
#print(new_school.get_numberOfStudents())
#print(new_school.get_level())
new_school.set_numberOfStudents(500)
#print(new_school.get_numberOfStudents())

primary_school = PrimarySchool("Brain", 'Parimary', 90, "With parents")
print(primary_school.get_name())
print(primary_school.get_numberOfStudents())
print(primary_school.get_level())
print(primary_school.get_pickupPolicy())



