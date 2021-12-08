#TODO
#LNKO(numerikus),Fakt(numerikus),Fib(numerikus),Binker(out listával),Linker(out listával),
#powN(numerikus), sqr(numerikus),
#egyéb: Hanoi(void), Ackermann(numerikus) , Stack, Queue


def rek_lnko(x,y:int)->int:
    if(y == 0):
        return x
    else:
        return rek_lnko(y,x%y)
def rek_fakt(n:int)->int:
    if(n <= 1):
        return n
    else:
        return rek_fakt(n-1)*n
def rek_fib(n:int)->int:
    if(n<=1):
        return n
    else:
        return rek_fib(n-2)+rek_fib(n-1)
print(rek_fib(4))
def rek_Binker(A:list,n:any,e = None,u = None)->bool:
    if(e == None or u == None):
        e = 0
        u = len(A)-1
    if(e>u):
        return False
    k = (e+u)//2
    if(A[k]==n):
        return True,k
    else:
        if(A[k]>n):
            return rek_Binker(A,n,e,k-1)
        elif(A[k]<n):
            return rek_Binker(A,n,k+1,u)
print(rek_Binker([1,2,3,4],3))

def rek_linker(A:list,n:any,i:int = None)->bool:
    if(i == None):
        i = 0
    if(A[i] == n):
        return i
    else:
        return rek_linker(A,n,i+1)
print(rek_linker([1,2,3,4],3))
def rek_pow(a,n:int)->int:
    if(n == 0):
        return 1
    else:
        return rek_pow(a,n-1)*a
def rek_sqr(n:int)->int:
    if(n == 0):
        return 0
    else:
        return rek_sqr(n-1)+2*n-1
def Hanoi(n:int,A:str,B:str,C:str):#Alap, Segéd, Cél
    if(n>0):
        Hanoi(n-1,A,C,B)
        print(str(A) + "->" + str(C))
        Hanoi(n-1,B,A,C)
print(Hanoi(3,"A","B","C"))
"""
def Ackermann(m,n:int):
    if(m==0):
        return n+1
    if(m>0 and n==0):
        return Ackermann(m-1,1)
    if(m>0 and n>0):
        return Ackermann(m-1,Ackermann(m,n-1))

"""
