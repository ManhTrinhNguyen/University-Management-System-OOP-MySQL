
class Person:
  def __init__(self, db, name, email, deparment_id, role):
    self.db_connection = db 
    self.name = name 
    self.email = email 
    self.department_id = deparment_id
    self.role = role 

  def add_to_db(self):
    query = 'INSERT INTO people(name, email, role, department_id) VALUES (%s, %s, %s, %s)'
    self.db_connection.cursor.execute(query, (self.name, self.email, self.role, self.department_id))
    self.db_connection.db.commit()
    print(f'Added {self.name} role: {self.role} to DB')

  def remove_from_db(self, person_id):
    query = 'DELETE FROM people WHERE person_id=%s'
    self.db_connection.cursor.execute(query, (person_id,))
    self.db_connection.db.commit()
    print(f'Added {self.name} role: {self.role} from DB')


  