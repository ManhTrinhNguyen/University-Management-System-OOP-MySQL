from person import Person
class Student(Person):
  def __init__(self, db, name, email, deparment_id):
    super().__init__(db, name, email, deparment_id, role='student')
  
  def get_student_id(self):
    query='Select person_id FROM people WHERE name=%s, role="student"'
    self.db_connection.cursor.execute(query, (self.name, ))
    return self.db_connection.cursor.fetchone()[0]
  
  def enroll_to_course(self, course_id):
    # Insert student course 
    query='INSERT INTO students_courses (student_id, course_id) VALUES (%s, %s)'
    self.db_connection.cursor.execute(query, (self.get_student_id(), course_id))
    
    # Get Course name
    query_select_course_name = 'SELECT course_name WHERE course_id = %s'
    self.db_connection.cursor.execute(query_select_course_name, (course_id, ))
    course_name = self.db_connection.cursor.fetchone()[0]

    self.db_connection.db.commit()
    print(f'Enrolled student: {self.name} to course  {course_name}')

  def join_project(self, project_id):
    query='INSERT INTO projects_students (student_id, project_id) VALUES (%s, %s)'
    self.db_connection.cursor.execute(query, (self.get_student_id(), project_id))
    self.db_connection.db.commit()