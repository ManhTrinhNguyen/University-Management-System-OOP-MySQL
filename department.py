from database import Database 

class Department: 
  def __init__(self, db , department_name):
    self.db_connection = db 
    self.department_name = department_name 

  def add_department(self):
    query = 'INSERT INTO departments (department_name) VALUES (%s)'
    self.db_connection.cursor.execute(query, (self.department_name,))
    self.db_connection.db.commit()

# computer_science = Department(Database(), 'Computer Science')
# computer_science.add_department()
