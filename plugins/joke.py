import re

class Plugin:
    def loadPlugin(self):
     print "plugin joke loaded"

    def handle_KnockKnock(self, text, output):
      output.send("Knock Knock")
      output.setState("knockknock")

    def handle_WhosThere(self, text, output):
      output.send("Orange")
      output.setState("whosthere")

    def priority_WhosThere(self):
      return 2

    def handle_Who(self, text, output):
        output.send("Orange you going to let me in?")
        output.setState("")

    def isValid(self, text, input):
      if bool(re.match(r'(?:tell(?: me)?(?: a)? )?\bjoke\b', text, re.IGNORECASE)):
        return "KnockKnock"
      if bool(re.match(r"who(?:(?:')?s)? there\b", text, re.IGNORECASE)) and input.getState() == "knockknock":
        return "WhosThere"
      if bool(re.match(r'orange who\b', text, re.IGNORECASE)) and input.getState() == "whosthere":
        return "Who"
