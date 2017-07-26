# -*- coding: CP936 -*-
import subprocess
cmd="cmd.exe"
begin=101
end=110
while begin<end:
    #reload(sys)
    #sys.setdefaultencoding('CP936')
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    p.stdin.write("echo 你好."+str(begin)+"\n")
    p.stdin.close()
    p.wait()
    print "excution result:\n"
    pout=''.join(p.stdout.readlines())
    output=pout.decode('cp936').encode('utf-8')
    print "%s\n" % output
    begin=begin+1