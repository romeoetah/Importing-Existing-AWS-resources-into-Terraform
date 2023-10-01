#!/usr/bin/python3
import json
import argparse
import common
import fixtf2


def fixtf(ttft):

    print(ttft+" fixtf")  
    rf=ttft+"_resources.out"
    tf2=ttft+".tf"
    print("rw tf")
    try:
        f1 = open(rf, 'r')
    except:
        print("no "+rf)
        return
    Lines = f1.readlines()
    with open(tf2, "w") as f2:
        skip=0
        flag1=False
        flag2=False
        f2.write("##START,"+ttft+"\n")
        for t1 in Lines:
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip()
            except:
                tt2=""
            getfn = getattr(fixtf2, ttft)
            
            skip,t1,flag1,flag2=getfn(t1,tt1,tt2,flag1,flag2)
            if skip == 0:
                f2.write(t1)
                
    with open(tf2, "a") as f2:
        f2.write("##END,"+ttft+"\n")










