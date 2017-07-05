#6/22/17
#created by Gary Zeri

#script to create map of c-c bond lengths to PE in C2H4O

import os
import json

#number to add from start of struct to reach specified atom in struct
atoms = {"c1" : 1, "c2" : 2, "h1" : 3, "h3" : 4, "o" : 5, "h4" : 6} 

tripSur = []


#get number of md logs
def mdNum():
   return int(os.popen("ls mdlog* | wc --w").read())

#get number of lines in a md struct
def structNum(mdNum):
    return os.popen("grep -n 't=' 'mdlog.'" + mdNum).read().split("\n")


#get distance between two atoms
#uses struct of [x,y,z] type
def dist(X1,X2):
    return ((X1[0]-X2[0])**2 + (X1[1]-X2[1])**2 + (X1[2]-X2[2])**2)**0.5


#get atom position at specfied log and struct, return {x,y,z}
def getPos(md,lineNum,atom):
 
    line = os.popen("sed '" + str((lineNum + atom)) + "!d' 'mdlog." + str(md) + "'").read().split(" ")
    line = filter(str.strip,line)

    return [float(line[0]),float(line[1]),float(line[2])]




for md in range(mdNum()):
    
    #get line number starts for each struct in md
    structs = structNum(str((md + 1)))
    #remove last item from list, is empty
    structs = structs[:-1]
    


    #for each struct in mdlog
    for struct in structs:
        
        print(md)
        print(struct.split(":")[0])
        
        
        lineNum = int(struct.split(":")[0])
         
        #get positions of specified atoms 
        X1 = getPos(md+1,lineNum,atoms["c1"])
        X2 = getPos(md+1,lineNum,atoms["c2"])

    

        #append bond length to list, along with PE
        Dist = dist(X1,X2)
        pe = 0 
    
       
        tripSur.append([Dist,pe])
         
        #line = os.popen("sed '" + lineNum +"!d' 'mdlog.'" + str((md+1))).read().split(" ")
        #line = filter(str.strip, line)
     
        # [float(line[0]),float(line[1]),float(line[2])]

        #print(tripSur) 

        #print(X1)
        #print(X2)
        print("\n")

f = open("tripletSurface",'w')
json.dump(tripSur,f)


