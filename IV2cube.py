import itertools
class max_strategy:
    def __init__(self,I,MAX_VI, Object_mon):
        #
        self.I=I
        self.MAX_VI=MAX_VI
        self.Object_mon=Object_mon
    
    def Operation_AND(self,u):
        #多个立方表示相乘
        te=[u[0][i] for i in range(len(u[0]))]
        for i in range(len(u)-1):
            for j in range(len(u[i+1])):
                if u[i+1][j] not in te:
                    te.append(u[i+1][j])
        sum1=0
        for i in range(len(u)):
            sum1+=len(u[i])
        if len(te) < sum1:
            return 1
        else:
            return 0 

        
    def Remove_invalid_index(self,re,addr,value):
        result=[]
        for i in range(len(re)):
            count=0
            for j in range(len(addr)):
                if re[i][addr[j]]==value[j]:
                    count=count+1
            if count!=len(addr):
                result.append(re[i])
        return re
                
    def Process_1object_mon(self,object1mon):
        Mon_Max_VI=[]
        for i in range(len(object1mon)):
            Mon_Max_VI.append(self.MAX_VI[object1mon[i]])
        return Mon_Max_VI
    
    def MAX_VI_index(self,Mon_Max_VI):
        #建立iv表示的索引
        temp=[0 for i in range(len(Mon_Max_VI))]
        for i in range(len(temp)):
            temp[i]=len(Mon_Max_VI[i])
        
        t_index=[[i for i in range(temp[j])] for j in range(len(temp))]
        
        re=t_index[0]
        t2=t_index[1]
        for i in range(len(temp)-2):
            re=list(itertools.product(re,t2))
            for i in range(len(re)):
                re[i]=list(re[i])
            if i+2==len(temp):
                break
            t2=t_index[i+2]
        return t2
    
    def 
    


    

    

