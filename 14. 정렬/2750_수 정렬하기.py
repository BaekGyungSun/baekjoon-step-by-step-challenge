n=int(input())
n_list=[]

for i in range(n):
    n_list+=[int(input())]

n_list.sort()

for i in n_list:
    print (i)
