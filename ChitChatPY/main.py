class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
class TestCase:
  def __init__(self, name, function):
    self.name = name 
    self.data = function
  def expectToBe(self, value = None):
    if (value == self.data):
      print(f"{style.GREEN}✅  {self.name} passed!{style.RESET}")
    else:
      print(f"{style.RED}❌  {self.name} failed\nExpected: \n{style.RESET}{style.CYAN}  {value}\n{style.RESET}{style.RED}But recieved:\n{style.RESET}{style.CYAN}  {self.data}\n{style.RESET}")


    