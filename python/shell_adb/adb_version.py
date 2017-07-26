#disable standby
import subprocess

cmd = "cmd.exe"
#ip = raw_input("input ip:")
ip = "192.168.199.116"
connect = "adb connect "+str(ip)
disconnect = "adb disconnect"

def exec_cmd(str):
    print str
    child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    child.stdin.write(str + "\n")
    child.stdin.close()
    child.wait()

exec_cmd(disconnect)
exec_cmd(connect)

print "well done1"
child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
print "adb shell getprop"
child.stdin.write("adb shell getprop" + "\n")
child.stdin.close()
child.wait()
print "well done2"
for line in child.stdout.readlines():
    if line != '':
        if line.find("ro.build.version.sdk") > 0:
            print "%s\n" % line.rstrip()
    else:
        break


print "well done3"