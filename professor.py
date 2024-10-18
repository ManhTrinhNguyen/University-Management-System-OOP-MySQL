from person import Person 
from database import Database

class Professor(Person): 
  def __init__(self, db, name, email, deparment_id):
    super().__init__(db, name, email, deparment_id, role='professor')

  def get_professor_id(self):
    query='SELECT person_id FROM people WHERE name=%s and role="professor"'
    self.db_connection.cursor.execute(query, (self.name, ))
    return self.db_connection.cursor.fetchone()[0]
  
  def assign_to_course(self, course_name):
    query = 'UPDATE courses SET professor_id=%s WHERE course_name=%s'
    self.db_connection.cursor.execute(query, (self.get_professor_id(), course_name))
    self.db_connection.db.commit()
    print(f'Assign Professor {self.name} to a course {course_name}')

  def supervise_project(self, project_name):
    query = 'INSERT INTO research_projects (project_name, lead_professor_id) VALUES (%s, %s)'
    self.db_connection.cursor.execute(query, (self.get_professor_id(), project_name))
    self.db_connection.db.commit()
    print(f'Set Professor {self.name} to a project {project_name}')


  

  

  
