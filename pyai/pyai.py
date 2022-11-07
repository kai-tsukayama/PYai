from responder import *
from dictionary import*

class Pyai:
  def __init__(self,name):
    self.name=name
    self.dictionary=Dictionary()

    self.res_random=RandomResponder("Random",self.dictionary)
    self.res_what=RepeatResponder("Repeat?",self.dictionary)
    self.res_pattern=PatternResponder("Pattern",self.dictionary)

  def dialogue(self,input):
    x=random.randint(0,100)
    if x<=60:
      self.responder=self.res_pattern
    elif 61<=x<=90:
      self.responder=self.res_random
    else:
      self.responder=self.res_what
    return self.responder.response(input)
