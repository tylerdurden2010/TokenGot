import os,re
Another = open("C:\\result.txt","w")
test = re.compile(r'token')
RootPath = "c:\\test\\"
for i,j,k in os.walk("c:\\test\\"):
    for t in k:
        file = RootPath+t
        try:
            FileHandle = open(file,"r")
        except Exception,e:
            print Exception,":",e
        line = FileHandle.readline()
        while line:
            line = str(line)
            Match = re.search(test,line)
            if Match:
                try:
                    Another.write(line)
                except Exception,e:
                    print Exception,":",e
                Another.flush()
            line = FileHandle.readline()