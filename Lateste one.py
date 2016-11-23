'''First you should run the python file
Then you can use your command addroad allpoints startingpoint or calculatepath
Remember the startingpoint is necessary.
When input calculate the program is over.
So the command should obey this input order:addroad->startingpoint->calculatepath.
The nums 9999 means the way cannot be reached. So your input distance number should less than 9999.
If have some questions,please contact the author:anbangleo@gmail.com
'''
import copy
points=[]#remember all the points
h_x=[]
h_y=[]
h_dis=[]
re_x=[]
re_y=[]
re_dis=[]
listfrom=[]
listto=[]
listdis=[]
codeline=raw_input()
command=codeline.split(' ')
shortestline=''
shortestdis=0
temp=0
cc=0
savemin=0
flag=0#whether shortest way be or not
while 1:
    if command[0]=='addroad'or command[0]=='addRoad' or command[0]=='a':
        if command[1] not in points:
            points.append(command[1])
        if command[2] not in points:
            points.append(command[2])
        for i in range(len(listfrom)):
            if listfrom[i]==command[1] and listto[i]==command[2]:
                print("The line has defined before. The system will save the later one:")
                listfrom.pop(i)
                listto.pop(i)
                listdis.pop(i)
        listfrom.append(command[1])
        listto.append(command[2])
        listdis.append(command[3])
    elif command[0]=='startingPoint'or command[0]=='startingpoint' or command[0]=='s':
        if command[1] in points:
            start=command[1]
            shortestline=start+'-'
        else:
            print("The start point you selected doesn't exist. Please correct it:")
    elif command[0]=='allPoints'or command[0]=='allpoints':
        if len(listfrom) >0:
            for i in range(len(listfrom)):
                print ("%s-%s-%s" % (listfrom[i], listto[i], listdis[i]))
        else:
            print("No line has been inputed.")
    elif command[0]=='calculatePath'or command[0]=='calculatepath'or command[0]=='c':
        matrix = [[9999 for j in range(len(points))] for j in range(len(points))]
        points.sort()
        for i in range(len(listfrom)):
            matrix[points.index(listfrom[i])][points.index(listto[i])]=int(listdis[i])
        copy_matrix = copy.deepcopy(matrix)
        #calculate the shortest
        i=0
        j=0
        while i <len(listfrom):
            if listfrom[i]==start:
                cc=0
                savemin = min(copy_matrix[points.index(listfrom[i])])
                if savemin!=9999:
                    x = points.index(listfrom[i])
                    y = matrix[x].index(savemin)
                    if (x not in h_x) or (y not in h_y):
                        h_x.append(x)
                        h_y.append(y)
                        h_dis.append(savemin)
                    start=points[y]
                    shortestline=shortestline+start+'-'
                    shortestdis=shortestdis+savemin
                    for i in range(len(points)):
                        copy_matrix[i][y]=9999
                        copy_matrix[i][x]=9999
                    if len(shortestline)==2*len(points):
                        shortestline=shortestline+str(shortestdis)
                        print (shortestline)
                        flag=1
                        break
                    i=-1
                else:#have the line but it cannot be reached
                    t = len(h_x) - 1
                    while t >= 0:
                        shortestdis = shortestdis - h_dis[t]
                        for i in range(len(points)):
                            if matrix[h_x[t]][i] != 9999:
                                temp = temp + 1
                        if temp > 1:
                            matrix[h_x[t]][h_y[t]] = 9999
                            copy_matrix = copy.deepcopy(matrix)
                            start = points[h_x[t]]
                            shortestline.index(start)
                            shortestline = shortestline[0:(shortestline.index(start) + 2)]
                            if (h_x[- 1] not in re_x) and (len(re_x) != 0):
                                for i in range(len(re_x)):
                                    matrix[re_x[i]][re_y[i]] = re_dis[i]
                                    copy_matrix = copy.deepcopy(matrix)
                                    for j in range(t, len(h_x)):
                                        h_x.pop()
                                        h_y.pop()
                                        h_dis.pop()
                                    re_x = []
                                    re_y = []
                                    re_dis = []
                            else:
                                re_x.append(h_x[- 1])
                                re_y.append(h_y[- 1])
                                re_dis.append(h_dis[- 1])
                                h_x.pop()
                                h_y.pop()
                                h_dis.pop()
                            i = -1
                            if temp > 1:
                                temp = 0
                                break
                        t = t - 1
                        temp = 0

            else: #no the next line
                cc=cc+1
                if cc==len(listfrom):
                    cc=0
                    t=len(h_x)-1
                    while t>=0:
                        shortestdis = shortestdis - h_dis[t]
                        for i in range(len(points)):
                            if matrix[h_x[t]][i]!=9999:
                                temp=temp+1
                        if temp>1:
                            matrix[h_x[t]][h_y[t]] = 9999
                            copy_matrix=copy.deepcopy(matrix)
                            start=points[h_x[t]]
                            shortestline.index(start)
                            shortestline = shortestline[0:(shortestline.index(start)+2)]
                            if (h_x[-1] not in re_x) and (len(re_x)!=0):
                                for i in range(len(re_x)):
                                    matrix[re_x[i]][re_y[i]]=re_dis[i]
                                    copy_matrix = copy.deepcopy(matrix)
                                    for j in range(t,len(h_x)):
                                        h_x.pop()
                                        h_y.pop()
                                        h_dis.pop()
                                    re_x=[]
                                    re_y=[]
                                    re_dis=[]
                            else:
                                re_x.append(h_x[-1])
                                re_y.append(h_y[- 1])
                                re_dis.append(h_dis[- 1])
                                h_x.pop()
                                h_y.pop()
                                h_dis.pop()
                            i = -1
                            if temp>1:
                                temp = 0
                                break
                        t=t-1
                        temp=0
                else:
                    pass
            i=i+1
        if flag==0:
            print("Impossible to visit all points")
        break
    else:
        print ("Incorrect command!please correct it:")
    codeline = raw_input()
    command = codeline.split(' ')