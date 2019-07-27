with open("read.txt", "r") as f:
  mylist = list(map(int, f.readline().split()))
x = int(input())
print(mylist)
def find(start, stop):
    if start > stop:
        return False
    mijloc =(start + stop) // 2 
    if x > mylist[mijloc]:
        print(mylist[mijloc + 1 : stop])
        find(mijloc+1, stop)
    elif x < mylist[mijloc]:
        print(mylist[start : mijloc - 1])
        find(start, mijloc-1)
    return True
    
print(find(0, len(mylist)))
