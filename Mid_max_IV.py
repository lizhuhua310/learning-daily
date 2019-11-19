import itertools
#导入多项式生成文件
#导入最终时刻关于中间时刻的文件
class reduction:
    def __init__(self,I,varpoly):
        self.I=I
        self.varpoly=varpoly
    
    def vector_sort(self,u):
        """
        将每个状态的每个单项从小到达进行排序
        以及删除参数1的影响
        """
        u.sort()
        par_1=[285,286,287]
        u2=[]
        for i in range(len(u)):
            count=0
            for j in range(len(par_1)):
                if u[i] != par_1[j]:
                    count=count+1
            if count==len(par_1):
                u2.append(u[i])
        # print("oc")
        return u2
    
    def vector_rep0(self,u):
        """
        考虑中间时刻状态表达式中参数0带入的影响
        """
        addr0=[i for i in range(288)]
        key=[i for i in range(80)]
        # print(I)
        addr1=[285,286,287]
        for i in range(len(key)):
            addr0.remove(key[i])
        for i in range(len(self.I)):
            addr0.remove(self.I[i])
        for i in range(len(addr1)):
            addr0.remove(addr1[i])
        # print(addr0)
        for i in range(len(u)):
            if u[i] in addr0:
                return 1
        # print("没有0")
        return 0
    
    def Statevar_poly(self,U):
        """
        考虑的是中间时刻的一个状态变量的多项式表达式
        """
        re=[]
        for i in range(len(U)):
            # print(U[i])
            if reduction.vector_rep0(self,U[i]) == 0:
                # print(U[i])
                temp=reduction.vector_sort(self,U[i])
                # print(temp)
                re.append(temp)
        #re存放的是带入参数0 且考虑参数1后排序表达式
        #处理重复单项
        # print(re)
        re1=[]
        for i in range(len(re)):
            if re.count(re[i])%2==1:
                re1.append(re[i])
        #re1中存放的是移除偶数次数重复的单项
        return re1
    
    def Split_mon_v_key(self,v):
        #分离每个单项的公共变量和私密变量
        #格式 [] ->[[],[]]
        IV=[]
        key=[]
        for i in range(len(v)):
            if v[i] <80:
                key.append(v[i])
            else:
                IV.append(v[i])
        re=[]
        re.append(key)
        re.append(IV)
        return re
    
    def Count_mon_v(self,VI):
        """
        统计每个状态变量中
        """
        temp=[0 for i in range(len(VI))]
        for i in range(len(VI)):
            for j in range(len(VI[i])):
                if temp[i] < len(VI[i][j]):
                    temp[i]=len(VI[i][j])
        return temp
    
    def Mid_monoment_state_poly(self):
        #V是中间时刻所有状态位置的单项表示
        #格式[[[],[]],[[],[]]]
        # print(self.varpoly)
        V=[0 for i in range(len(self.varpoly))]
        # print(V)
        for i in range(len(self.varpoly)):
            # print(self.varpoly[i])
            V[i]=reduction.Statevar_poly(self,self.varpoly[i])
        # print(V)
        return V
    
    def Split_Mid_monoment_state_poly_v_key(self,V):
        #分离中间时刻的所有状态变量的多项式表达式中的公共变量和私密变量
        #格式 [[[[],[]],[[],[]]],,,,]
        for i in range(len(V)):
            for j in range(len(V[i])):
                V[i][j]=reduction.Split_mon_v_key(self,V[i][j])
        
        VI=[]
        for i in range(len(V)):
            temp=[]
            for j in range(len(V[i])):
                if V[i][j][1] !=[]:
                    temp.append(V[i][j][1])
            VI.append(temp)
        #VI格式[,,,[[],[]],,,]
        MAX_VI=[]
        #MAX_VI[]中存放的是每个状态变量中IV达到最高次组合的项
        MAX=reduction.Count_mon_v(self,VI)
        for i in range(len(VI)):
            temp=[]
            for j in range(len(VI[i])):
                if len(VI[i][j]) == MAX[i]:
                    temp.append(VI[i][j])
            MAX_VI.append(temp)
        
        #MAX_VI -> 每个中间时刻的状态变量次数达到最大的IV表示
        return MAX_VI,V
    
    def Mid_monoment_main(self):
        """
           中间时刻状态变量--> iv最高次表示式 ，iv以及key分离表达式
        """
        V=reduction.Mid_monoment_state_poly(self)
        # print(V)
        # print("t")
        MAX_VI, V2=reduction.Split_Mid_monoment_state_poly_v_key(self,V)
        return MAX_VI,V2

    
    




        

        



