class syntax():
  def __init__(self,path):
    self.path = path
    rfiletmp = open(path,'r')
    self.source = rfiletmp.read()
    rfiletmp.close()
    del rfiletmp
    self.lines = self.source.split('\n')
    self.wfile = open(self.path,'w')
  def decode(self):
    for line in range(len(self.lines)):
      source = self.lines[line]
      ## Work In Progress
