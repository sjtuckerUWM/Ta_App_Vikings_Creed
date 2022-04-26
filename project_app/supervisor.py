from project_app.user import User


class Supervisor(User):
  def __init__(self, id, email, password, name, address, phoneNum):
    User.__init__(self, id, email, password, name, address, phoneNum)
