import subprocess

child1 = subprocess.Popen(["dir.exe"], stdout=subprocess.PIPE,
  shell = True)
#child1.wait()
while True:
  line = child1.stdout.readline()
  if line != '':
    #the real code does filtering here
    print "test:", line.decode('cp936').encode('utf-8').rstrip()
  else:
    break
