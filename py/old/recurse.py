from sys import*
setrecursionlimit(~-2**31)
def printList(myList):
   for element in myList:
      if isinstance(element, list):
         printList(myList)
      else:
         print(element)

a=[]
a.append(a)
printList(a)
