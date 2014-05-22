import re

class Plugin:
    def loadPlugin(self):
      print "plugin test loaded"

    def handle(self, text, output):
      output.send("im working")

    def isValid(self, text, input):
      return bool(re.match(r'\btest\b', text, re.IGNORECASE))
