from dataclasses import dataclass

@dataclass
class TodoItem:
  name: str
  description: str
  status: bool = False
  
  def __str__(self) -> str:
    return f"Task: {self.name} | Description: {self.description} | Finished: {self.status}"
  
  def setName(self, name: str):
    self.name = str(name)
  
  def setDescription(self, description: str):
    self.description = str(description)

  def toggleStatus(self):
    self.status = not self.status

  def setStatusFinished(self):
    self.status = True

  def setStatusUnfinished(self):
    self.status = False