def split_m(m):
    n=len(m)
    mid=n//2
    a11=[row[:mid] for row in m[:mid]]
    a12=[row[mid:] for row in m[:mid]]
    a21=[row[:mid] for row in m[mid:]]
    a22=[row[mid:] for row in m[mid:]]
    return a11,a12,a21,a22
def add_m(m1,m2):
    return [[m1[i][j]+m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
def sub_m(m1,m2):
    return [[m1[i][j]-m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
def strassen(m1,m2):
    if len(m1)==1:
        return [[m1[0][0]*m2[0][0]]]
    a11,a12,a21,a22=split_m(m1)
    b11,b12,b21,b22=split_m(m2)
    m1=strassen(add_m(a11,a22),add_m(b11,b22))
    m2=strassen(add_m(a21,a22),b11)
    m3=strassen(a11,sub_m(b12,b22))
    m4=strassen(a22,sub_m(b21,b11))
    m5=strassen(add_m(a11,a12),b22)
    m6=strassen(sub_m(a21,a11),add_m(b11,b12))
    m7=strassen(sub_m(a12,a22),add_m(b21,b22))
    c11=add_m(sub_m(add_m(m1,m4),m5),m7)
    c12=add_m(m3,m5)
    c21=add_m(m2,m4)
    c22=add_m(sub_m(add_m(m1,m3),m2),m6)
    result=[]
    for i in range(len(c11)):
        result.append(c11[i]+c12[i])
    for i in range(len(c21)):
        result.append(c21[i]+c22[i])
    return result
m1=[[5,9,2,7],
    [-4,7,7,4],
    [1,2,-3,3],
    [8,1,3,5]]
m2=[[5,2,3,2],
    [7,1,5,4],
    [3,-5,2,2],
    [2,4,2,7]]
result=strassen(m1,m2)
for row in result:
    print(row)