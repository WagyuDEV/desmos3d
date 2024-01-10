import re

f = open("./files/output.stl", "r").read()

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

nf = open("output.txt", "w")
nf.write(tristr)