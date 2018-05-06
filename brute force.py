import random
BoX={}
Const_BoX={}
def ij_into_key(i,j):
    return (str(i)+str(j))
def matrix_output(BoX):
    for i in range(0,9):
        temp = ''
        for j in range(0,9):
            if(j == 3 or j == 6):
                temp+='  '+str(BoX[ij_into_key(i,j)])
            else:
                temp+=' '+str(BoX[ij_into_key(i,j)])
        print(temp)
        if i == 2 or i == 5:
            print()


def create_an_empty_matrix(BoX):
    for i in range(0,9):
        for j in range(0,9):
            if( not (ij_into_key(i,j) in BoX.keys())):
                BoX[ij_into_key(i,j)]='-'
    return BoX

def Checking_the_horizontal_line(i,BoX):   	
    Temp=set()
    for j in range(0,9):
        Temp.add(BoX[ij_into_key(i,j)])
    if len(Temp) == 9:
        return True
    else:
        return False

def Checking_the_vertical_line(j,BoX):
    Temp=set()
    for i in range(0,9):
        Temp.add(BoX[ij_into_key(i,j)])
    if len(Temp) == 9:
        return True
    else:
        return False

def matrix_filling(temp_box,firsArr,secondArr,Const_BoX):
    numbers = []
    for temp in [1,2,3,4,5,6,7,8,9]:
        flag = False
        for i in firsArr:
            for j in secondArr:
                if ij_into_key(i,j) in Const_BoX.keys():
                    if temp == Const_BoX[ij_into_key(i,j)]:
                        flag = True
        if(flag==False):
            numbers+=[temp]    
    random.shuffle(numbers)
    for i in firsArr:
        for j in secondArr:
            if ij_into_key(i,j) in Const_BoX.keys():
                temp_box[ij_into_key(i,j)]=Const_BoX[ij_into_key(i,j)]
            else:
                temp_box[ij_into_key(i,j)]=random.choice(numbers)
                numbers.remove(temp_box[ij_into_key(i,j)])
                random.shuffle(numbers)
    return temp_box
        
        
                    
    
  
def Check_All_SB(BoX):
    flag = True
    for temp in [0,1,2,3,4,5,6,7,8]:    
        if (not Checking_the_vertical_line(temp,BoX)):
            flag = False
        if (not Checking_the_horizontal_line(temp,BoX)):
            flag = False
    return flag          
  
    
Const_BoX={'00':2,'01':3,'02':8,'10':7,'11':5,'12':9,'20':4,'21':1,'22':6,
           '03':9,'04':6,'05':5,'13':4,'14':1,'15':3,'23':2,'24':7,'25':8,
           '06':7,'07':1,'08':4,'16':6,'17':8,'18':2,'26':9,'27':5,'28':3,
           '30':9,'31':4,'32':5,'40':6,'41':8,'42':7,'50':3,'51':2,'52':1,
           '33':1,'34':3,'35':6,'43':5,'44':2,'45':4,'53':8,'54':9,'55':7,
           '36':2,'37':7,'38':8,'46':1,'47':3,'48':9,'56':4,'57':6,'58':5,
           '60':1,'61':6,'62':2,'70':5,'71':7,'72':4,#'80':8,'81':9,'82':3,
           '63':3,'64':5,'65':9,'73':6,'74':8,'75':2,#'83':7,'84':4,'85':1,
           '66':8,'67':4,'68':7,'76':3,'77':9,'78':1}
number_of_walls= len(Const_BoX.keys())
for i in Const_BoX.keys():
    BoX[i]=Const_BoX[i]




    
Empty_BoX = create_an_empty_matrix(BoX)
matrix_output(BoX)
print()
print('<----->')
print()

step = 0
Flag = True
while(Flag):
    BoX = Empty_BoX
    #first
    BoX = matrix_filling(BoX,[0,1,2],[0,1,2],Const_BoX)
    BoX = matrix_filling(BoX,[0,1,2],[3,4,5],Const_BoX)
    BoX = matrix_filling(BoX,[0,1,2],[6,7,8],Const_BoX)
    #second
    BoX = matrix_filling(BoX,[3,4,5],[0,1,2],Const_BoX)
    BoX = matrix_filling(BoX,[3,4,5],[3,4,5],Const_BoX)
    BoX = matrix_filling(BoX,[3,4,5],[6,7,8],Const_BoX)
    #third
    BoX = matrix_filling(BoX,[6,7,8],[0,1,2],Const_BoX)
    BoX = matrix_filling(BoX,[6,7,8],[3,4,5],Const_BoX)
    BoX = matrix_filling(BoX,[6,7,8],[6,7,8],Const_BoX)
    #print(step)
    step+=1       
    Flag = not Check_All_SB(BoX)

            
matrix_output(BoX)
