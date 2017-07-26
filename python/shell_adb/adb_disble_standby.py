#disable standby
import subprocess

cmd = "cmd.exe"
#ip = raw_input("input ip:")
ip = "192.168.199.116"
connect = "adb connect "+str(ip)
disconnect = "adb disconnect"

exec_arry =[
    "am start com.android.settings",
    "sleep 1",
    "input keyevent DPAD_RIGHT",
    "input keyevent DPAD_RIGHT",
    "input keyevent DPAD_CENTER",
    "sleep 1",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_CENTER",
    "sleep 1",
    "input keyevent DPAD_CENTER",
    "sleep 2",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_CENTER",
    "sleep 2",
    "input keyevent BACK",
    "sleep 2",
    "input keyevent BACK",
    "sleep 2",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_CENTER",
    "sleep 3",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_DOWN",
    "input keyevent DPAD_CENTER"
]

def exec_cmd(str):
    print str
    child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    child.stdin.write(str + "\n")
    child.stdin.close()
    child.wait()

exec_cmd(disconnect)
exec_cmd(connect)


for i in exec_arry:
    exec_cmd("adb shell "+i)

'''
am start com.android.settings
sleep 1
input keyevent DPAD_RIGHT
input keyevent DPAD_RIGHT
input keyevent DPAD_CENTER
sleep 1
input keyevent DPAD_DOWN
input keyevent DPAD_CENTER
sleep 1
input keyevent DPAD_CENTER
sleep 2
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_CENTER
sleep 2
input keyevent BACK
sleep 2
input keyevent BACK
sleep 2
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_CENTER
sleep 3
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_DOWN
input keyevent DPAD_CENTER
'''