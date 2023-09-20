#---------- Stack Push & Pop -------------
def Push(val,S):
    S.append(val)
def pop(S):
    S_size=len(S)
    if S_size==0:
        print("stake is empty")
    else:
         item=S.pop()
         print("Delete item:",item)
stack=[]
Push(5,stack)
Push(10,stack)
Push(20,stack)
print("print push operation:  ",stack)
pop(stack)
print("after pop operation:  ",stack)

#-------------- Stack  Infix to Postfix ------------
output = []
operator = []
pr = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
Ex = input("Enter the Expression: ")
for i in Ex:
  if i == '(':
    operator.append(i)
  elif i == ')':
    while operator[-1] != '(':
      Element = operator.pop()
      output.append(Element)
    operator.pop()
  elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
    if len(operator) > 0:
      while pr[operator[-1]] >= pr[i]:
        Element = operator.pop()
        output.append(Element)
        if len(operator) == 0:
          break
    operator.append(i)
  else:
    output.append(i)

while len(operator) != 0:
  element = operator.pop()
  output.append(element)
print("postfix expression is:", ''.join(output))

# --------------- Evaluation of Postfix ------------

operator = ['+', '-', '*', '/', '^']

opn = []
Ex = input('Enter the postfix expression: ')
Exp = Ex.split()

for i in Exp:
    if i not in operator:
        opn.append(i)
    else:
        n1 = eval(opn.pop())
        n2 = eval(opn.pop())

        if i == '+':
            ans = n2 + n1
        elif i == '-':
            ans = n2 - n1
        elif i == '*':  # Corrected this line
            ans = n2 * n1
        elif i == '/':
            ans = n2 / n1
        elif i == '^':
            ans = n2 ** n1
        opn.append(str(ans))

print("Answer is:", opn[0])
