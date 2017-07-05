import os


#acquire necessary info from user

#mdlog file#
print("Please enter MD log file number.")
mdNum = str(raw_input())

#get struct number to access
print("Enter data struct number to access.")
struct = int(raw_input())

#print("Would you like velocity data? y/n")
#vds = str(raw_input())

#if(vds == "y"):
 #   vds = True
#else:
 #   vds = False

#************************************************************************

#begin searching for struct in specified file


#possible method to check if struct number exists in file
#get number of structs in mdfile
#str(os.popen("grep -n 't=' mdlog." + mdNum + " | wc" ).read().split("    ")[1])


#get starting line of  specified struct
lineNum = int(os.popen("grep -n 't=' mdlog." + mdNum).read().split("\n")[struct].split(":")[0])


#begin writing struct coords to external file

out = file("out.md","w")

with open("mdlog."+mdNum,"r") as md:



    #move to start of specified struct in file


    for x in range(lineNum):
        md.next()



    for line in md:
        
        #ifs to check if line is for pos,
        #if yes, add to out
        #else quit loop
#        if(line.split(" ")[0] == ""): 
#            out.write(line)
        
#       elif(line.split("-")[0] == ""):
#            out.write(line)

#       else:
#            md.close()
#            break
            

        if(len(filter(None, line.split(" "))) != 4):
            break
        out.write(line)

        print("Loading Struct...")


print("Data outputed to out.md")


