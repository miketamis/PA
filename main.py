import os
import sys

path = "plugins/"
plugins = {}



class Output:
  def send(self, text):
    print text
  def setState(self, text):
    inn.state = text

class Input:
  def __init__(self):
    self.state = ""
  def getState(self):
    return self.state

# Load plugins
sys.path.insert(0, path)
for f in os.listdir(path):
    fname, ext = os.path.splitext(f)
    if ext == '.py':
        mod = __import__(fname)
        plugins[fname] = mod.Plugin()
sys.path.pop(0)


#setup plugins
for plugin in plugins.values():
  plugin.loadPlugin()

output = Output()
inn = Input()
output.inn = inn;
inn.output = output;

# will run the givin comand
def handle_comand(comand):
  plugin, func = comand
  if(type(func) == type(True)):
    plugin.handle(rawInput, output)
  else:
    getattr(plugin, "handle_" + func)(rawInput, output)

# gets the priority of a comand
def get_priority(comand):
  plugin, func = comand

  try:
    if(type(func) == type(True)):
      return plugin.priority()
    else:
      return getattr(plugin, "priority_" + func)()

  except AttributeError:
    return 1

# gets input
while (1):
  rawInput = raw_input('--> ')
  valid = []

  #gets all the valid plugin
  for plugin in plugins.values():
    func = plugin.isValid(rawInput, inn)
    if(func):
      valid.append((plugin, func))

  #if there is only one valid plugin run that
  if(len(valid) == 1):
    handle_comand(valid[0])

  #if there is multiple valid plugin run the one with the highest
  # priority
  if(len(valid) > 1):
    top_priority = -10
    highest_priority = None
    for v in valid:
      temp = get_priority(v)
      if(temp > top_priority):
        highest_priority = v
        top_priority = temp

    handle_comand(highest_priority)

  #if theres no valid plugins say something
  if not valid:
    output.send("sorry i didn't get that")
