# -*- coding: utf-8 -*-
import subprocess
import sys

from functions.sum_jhy import *

print sum_jhy(5)
prefix = give_ip_prefix()
print prefix


def quotation_mark():
    """Parses a single log entry emitted by app_logging.AppLogsHandler.

    Parses a log entry of the form LOG <level> <timestamp> <message> where the
    level is in the range [0, 4]. If the entry is not of that form, ValueError is
    raised.

    Args:
      entry: The log entry to parse.
      clean_message: should the message be cleaned (i.e. \0 -> \n).

    Returns:
      A (timestamp, level, message, source_location) tuple, where source_location
      is None.

    Raises:
      ValueError: if the entry failed to be parsed.
    """


cmd = "cmd.exe"
begin = 36
end = 40
while begin < end:
    ##blow for windows shell chinese show##
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    # print "excution result start :\n"
    child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    print "ping -n 1 -w 100 " + prefix + "." + str(begin) + ""
    child.stdin.write("ping -n 1 -w 100 " + prefix + "." + str(begin) + "\n")
    child.stdin.close()
    child.wait()
    # print "excution result end:\n"
    begin += 1
    # print child.stdout.readlines()
    for line in child.stdout.readlines():
        ##blow for pycharm and cygwin show chinese#
        if line != '':
            output = line.decode('cp936').encode('utf-8')
            #print "%s\n" % output.rstrip()
            output_g = unicode(line, "gbk")
            if output_g.find(u"请求超时") >= 0:
                print "=====Ping it Error====="
                break
            elif output_g.find(u"的回复") >= 0:
                print "=====Ping it Success====="
                break
        else:
            break
