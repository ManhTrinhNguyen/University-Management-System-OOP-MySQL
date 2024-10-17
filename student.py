from person import Person
class Student(Person):
  def __init__(self, db, name, email, deparment_id):
    super().__init__(db, name, email, deparment_id, role='student')
  
  def get_student_id(self):
    query='Select person_id FROM people WHERE name=%s, role="student"'
    self.db_connection.cursor.execute(query, (self.name, ))
    return self.db_connection.cursor.fetchone()[0]
  
  def enroll_to_course(self, course_id):
    query='INSERT INTO students_courses (student_id, course_id) VALUES (%s, %s)'
    self.db_connection.cursor.execute(query, (self.get_student_id(), course_id))
    self.db_connection.db.commit()