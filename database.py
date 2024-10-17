import mysql.connector 
from dotenv import load_dotenv 
import os 

load_dotenv() 

class Database: 
  def __init__(self):
    self.db = mysql.connector.connect(host='localhost', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database='university')
    self.cursor = self.db.cursor()

