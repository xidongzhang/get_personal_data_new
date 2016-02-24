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
        ll=line.split(" : ")
        try:
            if(len(ll) == 2):
                print "%s\t1\t%s"%(ll[0],ll[1])
        except:
            pass
