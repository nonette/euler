## don't understand shell arguments
#  popen fails if args split up

import re
import subprocess
import sys

FILENAME = 'times'

def time(N):
    p = 'p'+str(N).zfill(3)
    cmd = ['time python -c "import p.%s; print p.%s.%s()"' % (p, p, p)]
    job = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    answer, raw = job.communicate()
    answer = answer.strip()
    if raw.find('Traceback') >= 0:
        print 'Error for %s, %s' % (p, raw)
        return (None, None)
    runningtime = re.search('\d+\.\d+', raw).group()
    return (answer, runningtime)
    
def rewrite(l):
    with open(FILENAME) as f:
        raw = f.read()
    data = {}
    for line in raw.splitlines():
        line = line.split()
        data[line[0]] = (line[1], line[2], ' '.join(line[3:]))

    for n in l:
        a,t = time(n)

        if t:
            key = 'p'+str(n).zfill(3)
            data[key] = (t, a, data[key][2] if key in data else '')

    
    widths = [max(len(data[key][i]) for key in data.keys()) for i in range(3)]
    with open(FILENAME,'w') as f:
        for key in sorted(data.keys()):
            data[key] = tuple(data[key][i].ljust(widths[i]) for i in range(3))
            f.write('\t'.join((key,)+data[key])+'\n')

if __name__=='__main__':
    try:
        n = int(sys.argv[1])
    except Exception as e:
        print "usage: python speedrun.py n"
        print "n: the number of the problem" 
    rewrite([n])
