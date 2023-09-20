def LPS_table(P):
  N=len(P)
  lps=[0]*N
  i=0
  j=1

  while j<N:
    if P[i]==P[j]:
        lps[j]=i+1
        i+=1
        j+=1
    else:
        if i==0:
            lps[j]=0
            j+=1
        else:
          i=lps[i-1]
  return lps
"""P="ABCDABD"
print(LPS_table(P)) """
def KMP (T,P):
    M=len(T)
    N=len(P)
    lps=LPS_table(P)
    i=0
    j=0

    while i<M:
      if T[i]==P[j]:
        i+=1
        j+=1
      if j==N:
        print("pattern found at Loc: ",i-j)
        j=lps[j-1]

      elif T[i]!=P[j]:
          if j==0:
           i+=1
          else:
            j=lps[j-1]

T="ABCDABCDABE"
P="CDA"
KMP(T,P)
