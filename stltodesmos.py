import sys
import os
import re
import stl
from stl import mesh
import datetime

def make(file, binary):
    
    dt = ""
    if binary:
        dt = datetime.datetime.now()
        fn = "TEMPOUTPUT.stl"
        tempf = mesh.Mesh.from_file(file)
        tempf.save(fn, mode=stl.Mode.ASCII)
        fl = open(fn, "r")
        f = fl.read()
    else:
        fl = open(file, "r")
        f = fl.read()

    tristr = "\\triangle\\left("
    cnt = 0

    x = []
    y = []
    z = []

    for i in f.splitlines():
        if i.strip().__contains__("vertex"):
            if cnt == 0:
                x = i.replace("vertex ", "").strip().split(" ")
                for v in range(0, len(x)):
                    if x[v].__contains__("e"):
                        x[v]=x[v].split("e")[0] + "*10^{" + str(int(x[v].split("e")[1]))+"}"
            if cnt == 1:
                y = i.replace("vertex ", "").strip().split(" ")
                for v in range(0, len(y)):
                    if y[v].__contains__("e"):
                        y[v]=y[v].split("e")[0] + "*10^{" + str(int(y[v].split("e")[1]))+"}"
            if cnt == 2:
                z = i.replace("vertex ", "").strip().split(" ")
                for v in range(0, len(z)):
                    if z[v].__contains__("e"):
                        z[v]=z[v].split("e")[0] + "*10^{" + str(int(z[v].split("e")[1]))+"}"
            cnt+=1
            if cnt >= 3:
                tristr+="("+str(x)+"), ("+str(y)+"), ("+str(z)+")\\right)\n\\triangle\\left("
                cnt = 0

    tristr=tristr.replace("[", "").replace("]", "").replace("'", "")
    tristr=tristr[:len(tristr)-15]
                
    print(tristr)

    fl.close()

    if binary:
        os.remove(fn)

def main(args):
    binary = False
    for arg in args:
        if arg == "-b":
            binary = True
        if arg == "-h":
            print("""
                stltodesmos - convert stl files into Desmos 3D graphs

                stltodesmos <args> <input file>

                args:
                    -h : display this menu (if the -h flag is used, do not supply a source file)
                    -b : singal to the program that you are using a binary stl file
            """)
            return
    file = args[len(args)-1]
    make(file, binary)
    

if __name__ == "__main__":
   main(sys.argv)
