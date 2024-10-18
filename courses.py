class Course: 
  def __init__(self, db, course_name, professor_id):
    self.db_connection = db 
    self.course_name = course_name 

  def add_course(self):
    query='INSERT INTO courses (course_name) VALUES (%s)'
    self.db_connection.execute.cursor(query, self.course_name,)
    self.db.commit()
    print(f'Added course {self.course_name} to DB')


