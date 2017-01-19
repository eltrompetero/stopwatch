# Simple stopwatch with shortcut commands.
# Author: Edward D. Lee
# Email: edl56@cornell.edu

from __future__ import division
import sys,os,time,subprocess
import numpy as np

def convert_to_hms(dt):
    h=dt//3600
    dt-=h*3600
    m=dt//60
    dt-=m*60
    s=dt//1
    return h,m,s

if __name__=='__main__':
    assert len(sys.argv)>1, "Must pass in at least one argument."
    if not os.path.isfile('record.txt'):
        subprocess.call('touch record.txt',shell=True)

    if sys.argv[1]=='start':
        with open('record.txt','r') as f:
            lines=f.readlines()
            if len(lines)>0:
                n=len(lines[-1].split(' '))
                assert n==2 or n==0, "Already started stopwatch."
        subprocess.call('echo %s>>record.txt'%str(time.time()),shell=True)
    elif sys.argv[1]=='stop':
        with open('record.txt','r') as f:
            lines=f.readlines()
        
        assert len(lines)>0, "Cannot stop if not started."
        assert len(lines[-1].split(' '))==1, "Cannot stop if not started."
        lines[-1]=lines[-1][:-2]
        lines[-1] += ' %f\n'%time.time()

        with open('record.txt','w') as f:
            for L in lines:
                f.write(L)
    elif sys.argv[1]=='sum':
        with open('record.txt','r') as f:
            lines=f.readlines()
        dt=0
        for L in lines:
            start,stop=[float(i) for i in L[:-2].split(' ')]
            dt+=stop-start
        hours,minutes,seconds=convert_to_hms(dt)
        print 'You have worked for %d hours, %d minutes, and %d seconds.'%(hours,minutes,seconds)
    elif sys.argv[1]=='clear':
        open('record.txt','w').close()
    else:
        raise Exception("Invalid option.")

