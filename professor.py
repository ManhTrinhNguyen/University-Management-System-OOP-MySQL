from person import Person 
from database import Database

class Professor(Person): 
  def __init__(self, db, name, email, deparment_id):
    super().__init__(db, name, email, deparment_id, role='professor')

  def get_professor_id(self):
    query='SELECT person_id FROM people WHERE name=%s and role="professor"'
    self.db_connection.cursor.execute(query, (self.name, ))
    return self.db_connection.cursor.fetchone()[0]
  
  def assign_to_course(self, course_id):
    query = 'UPDATE courses SET professor_id=% WHERE course_id=%s'
    self.db_connection.cursor.execute(query, (self.get_professor_id(), course_id))

  