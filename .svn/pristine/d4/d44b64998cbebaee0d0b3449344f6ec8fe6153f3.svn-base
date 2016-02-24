#! /usr/bin/env python
#coding=utf-8

import sys

last_tid = None
last_cluster_id = None

if __name__ == "__main__":
    for line in sys.stdin:
        var = line.strip().split("\t")
        type = var[1]
        if type == '1' :
            tid = var[0]
            cluster_id = var[2]
            
            if last_tid != tid :
            	last_tid = tid
                last_cluster_id = cluster_id
        elif type == '2' :
            if var[0] == last_tid and last_tid:
            	print "\t".join(var[2:])+"\t"+last_cluster_id
            else:
            	print "\t".join(var[2:])+"\tNULL"
