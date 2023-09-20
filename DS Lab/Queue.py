#---------- Enqueue / insertion in queue -----------
Max=5
def enqueue(Q,val):
  if len(Q) == Max:
    print("queue is full")
    return
  else:
    Q.append(val)

Q =[]
enqueue(Q,5)
enqueue(Q,15)
enqueue(Q,25)
enqueue(Q,35)
enqueue(Q,45)
print("After insertion",Q)

#------------- Dequeue/Dletion in queue -------------
def dequeue(Q):
  if len(Q) == 0:
    print("Queue is empty")
  else:
    item=Q.pop(0)
    print("deleted data is: ",item)
    print("After deletion: ",Q)

Q =[]
enqueue(Q,5)
enqueue(Q,15)
enqueue(Q,25)
enqueue(Q,35)
enqueue(Q,45)
dequeue(Q)

# ------------------- Prioroty queue with out function --------- 
Q=[]
Q.append((4,'A'))
Q.append((1,'B'))
Q.append((2,'C'))
Q.append((3,'D'))
Q.sort(reverse=True)

while Q:
 print(Q.pop(0))

#------------- Prioroty queue using function ------- 
def pr_Q(Q,val):
  Q.append(val)
  Q.sort(reverse=True)
Q=[]
pr_Q(Q,(4,'A'))
pr_Q(Q,(1,'D'))
pr_Q(Q,(2,'C'))
pr_Q(Q,(3,'B'))

while Q:
  print(Q.pop(0))
