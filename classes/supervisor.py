from classes.user import User

# constructor
class Supervisor(User):
  def __init__(self, id, email, password, name, address, phoneNum):
    User.__init__(self, id, email, password, name, address, phoneNum)
