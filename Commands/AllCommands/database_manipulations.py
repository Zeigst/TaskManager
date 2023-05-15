from dataclasses import dataclass
from Classes.todo_list import *
import pickle
import os
import zipfile

@dataclass
class SaveData:
  todo_list: TodoList

  def execute(self):
    with open("todo_list.pkl", "wb") as f:
      pickle.dump(self.todo_list.get_data(), f, pickle.HIGHEST_PROTOCOL)
    with zipfile.ZipFile('database.dat', 'w', compression=zipfile.ZIP_DEFLATED) as zip:        
      zip.write('todo_list.pkl')
    os.remove("todo_list.pkl")

@dataclass
class LoadData:
  todo_list: TodoList
  
  def execute(self):
    if os.path.exists('database.dat'):
      with zipfile.ZipFile('database.dat', 'r') as zip:
        zip.extractall()
      os.remove("database.dat")
      if(os.path.exists("todo_list.pkl")):
        with open("todo_list.pkl", "rb") as f:
          saved_list = pickle.load(f)
          self.todo_list.set_data(saved_list)
