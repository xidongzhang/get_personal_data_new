#coding=utf8
import sys
import os
import time
import json

if __name__ == '__main__':
    for line in sys.stdin:
        line=line.strip()
        if(line==""):
            continue
        ll=line.split("\t")
        tid=ll[3]
        try:
            if(int(tid)>2061202555):
                print tid+"\t2\t"+"\t".join(ll)
        except:
            pass
