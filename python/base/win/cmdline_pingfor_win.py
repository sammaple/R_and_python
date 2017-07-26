import subprocess
import re
p = subprocess.Popen(["ping.exe", 'google.com'],
  stdin = subprocess.PIPE,
  stdout = subprocess.PIPE,
  stderr = subprocess.PIPE,
  shell = True)
#out = p.stdout.read()
#regex = re.compile("Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms", re.IGNORECASE)
#print regex.findall(out)

while True:
  line = p.stdout.readline()
  if line != '':
    #the real code does filtering here
    print "test:", line.rstrip().decode('cp936').encode('utf-8')
  else:
    break