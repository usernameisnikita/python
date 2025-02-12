def pattern(n):
  
  for i in range(1,n+1):
    spaces=''*(n-i-1)
    star='*'* (2*i-1)
    space=''*(n-i-1)
    print(spaces+star+space)

n=int(input("enter level:"))
pattern(n)