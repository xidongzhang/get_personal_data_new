#coding=utf8
import sys
import os
import time
import json

if __name__ == '__main__':
    input_file = os.environ['map_input_file']
    arr=input_file.split("/")
    inputPath=arr[len(arr)-2]

    for line in sys.stdin:
        line=line.strip()
        if(line==""):
            continue
        if(inputPath=="user_goods_info"):
            ll=line.split("\t")
            tid=ll[3]
            try:
                if(int(tid)>2061202555):
                    print tid+"\t2\t"+"\t".join(ll)
            except:
                pass
        elif(inputPath=="cluster"):
            ll=line.split(" : ")
            try:
                if(len(ll) == 2):
                    print "%s\t1\t%s"%(ll[0],ll[1])
            except:
                pass
