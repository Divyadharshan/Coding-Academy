
def ma(a,r,c):

     sum=0
     for i in range(r):
          for j in range(c):
               if i==0 or i==(r-1) or j==0 or j==(c-1):
                    sum+=a[i][j]
     return sum

m=[[1,1,1],
   [1,1,1],
   [1,1,3]]
print(ma(m,len(m),len(m[0])))
     
