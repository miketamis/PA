import re

class Plugin:
    def loadPlugin(self):
      print "plugin whothere loaded"

    def handle(self, text, output):
      output.send("your PA")

    def isValid(self, text, input):
      return bool(re.match(r"who(?:(?:')?s)? there\b", text, re.IGNORECASE))
