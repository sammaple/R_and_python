import re
import sys

def get_smap(line):
    info = re.split(r'\s+', line)
    mem_range = re.split('-', info[0])
    mem_size = int(mem_range[1], 16) - int(mem_range[0], 16)
    key = "blank"
    if len(info) >= 6:
        key = info[5]
        if len(info) >= 7:
            key = key + info[6]
    return key, 0;##mem_size

def get_smap_pss(line):
    info = re.split(r'\s+', line)
    ##print info
    return info[1]

def stat_smap(file_path):
    smaps = dict()
    
    with open(file_path, 'r') as lines:
        g_key = ""
        for line in lines:
            if re.match(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{8}', line):
                ##print("in sections");
                key, mem_size = get_smap(line)
                if key in smaps:
                    smaps[key] = smaps[key] + mem_size
                else:
                    smaps[key] = mem_size
                g_key = key
            if re.match(r'^Rss', line):
                ##print("in RSS")
                size_pss = int(get_smap_pss(line))
                ##print size_pss
                ##print g_key
                if g_key in smaps:
                    smaps[g_key] = smaps[g_key] + size_pss
                else:
                    smaps[g_key] = size_pss
                ##print smaps[g_key]

    
    return smaps

def print_stat(smaps):
    total_pss = 0;
    smaps = sorted(smaps.items(), key=lambda x: x[1])
    for key, value in smaps:
        total_pss += value
        print "{0}:{1}KB".format(key, value)
        print "total pss:{0}".format(total_pss)

        
if  __name__ =='__main__':
    smaps = stat_smap(sys.argv[1])
    print_stat(smaps)