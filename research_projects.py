class Research_Project:
  def __init__(self, db, project_name):
    self.db_connection = db 
    self.project_name = project_name 

  def add_research_project(self):
    query = 'INSERT INTO research_projects (project_name) VALUES (%s)'
    self.db_connection.cursor.execute(query, (self.project_name,))
    self.db_connection.db.commit()
