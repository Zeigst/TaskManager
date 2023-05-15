from dataclasses import dataclass

@dataclass
class UserCommand:
  user_input: str = ""
  user_choice: str = ""
  menu_status: int = 1
  main_command_menu: str = "\nCOMMANDS:\n----------\n1. Create new task to manage\n2. Select task to edit/delete\n3. Undo\n4. Redo\n5. End Program"
  item_command_menu: str = "\nCOMMANDS:\n----------\n1. Toggle Status\n2. Edit Informations\n3. Delete\n4. Go back"

  def requestUserInputs(self) -> str:
    if self.menu_status == 1:
      print(self.main_command_menu)
      self.user_input = input("Enter 1 - 6 to choose: ")
      return self.user_input
    elif self.menu_status == 2:
      self.user_input = input("\nEnter task name to select task: ")
      return self.user_input
    elif self.menu_status == 3:
      print(self.item_command_menu)
      self.user_input = input("Enter 1 - 4 to choose: ")
      return self.user_input
    

  def setMenuStatus(self, status: int) -> None:
    self.menu_status = status

  def setUserChoice(self, user_choice: str) -> None:
    self.user_choice = user_choice

  def resetUserChoice(self) -> None:
    self.user_choice = ""

  def resetUserInput(self) -> None:
    self.user_input = ""