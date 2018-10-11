#1
def panduan(x,best):
    n=int(x)
    if n>=best-10:
        return 'A'
    elif n>=best-20:
        return 'B'
    elif n>=best-30:
        return 'C'
    elif n>=best-40:
        return 'D'
    else:
        return 'F'

a=raw_input('Enter scores:')
l=a.split(' ')
for i in range(len(l)):
    l[i]=int(l[i])
m=int(max(l))
print m
for i in range(len(l)):
    print('Student '+str(i)+' score is '+str(l[i])+' and grade is '+str(panduan(l[i],m)))
#2
a=raw_input('Enter maths:')
s=a.split()
print(s)
s.reverse()
print(s)
#3

a=raw_input('Enter integers between 1 and 100:')
l=a.split()
print(l)
for i in range(101):
    if l.count(str(i))!=0:
        if l.count(str(i))==1:
            print(str(i)+' occurs '+str(l.count(str(i)))+' time')
        else:
print(str(i)+' occurs '+str(l.count(str(i)))+' times')
#4
def pinjun(n):
    sum_=0
    l=len(n)
    for i in n:
        sum_ += int(i)
    return sum_/(l*1.0)

def bijiao(n):
    big=0
    small=0
    for i in n:
        if int(i)>=pinjun(n):
            big += 1
        else:
            small +=1
    print('Big:'+str(big))
    print('Small:'+str(small))

if __name__ == '__main__':
    a = raw_input('Enter sorce:')
    s=a.split()
bijiao(s)
#5
import random
a=[0,0,0,0,0,0,0,0,0,0]
for i in range(1001):
    a[random.randint(0,9)] += 1
print(a)
#6
def indexOfSmallestElement(lst):
    m=min(l)
    print(m)
    for i in range(len(l)):
        if l[i]==m:
            print(str(i)+' ',end="")
    print()



if __name__ == '__main__':

    a=input('>>')
    l=a.split()
indexOfSmallestElement(l)
#7
import random
def shuffle(lst):
    l= len(lst)
    s=[]
    for i in range(len(lst)):
        n=random.randint(0,l-1)
        s.append(lst[n])
        lst.pop(n)
        l -= 1
    print(s)

if __name__ == '__main__':
    a=raw_input('>>')
    b=a.split()
    print(b)
shuffle(b)
#8
def eliminateDuplicates(lst):
    s=[]
    for i in lst:
        if i not in s:
            s.append(i)
    print(s)

if __name__ == '__main__':
    a=raw_input('Enter ten number:')
    l=a.split()
eliminateDuplicates(l)
#9
def isSorted(lst):
    flag=0
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        print('The list is not sorted')
    else:
        print('The list is already sorted')

if __name__ == '__main__':
    a = raw_input('Enter list:')
    s = a.split()
    for i in range(len(s)):
        s[i]=int(s[i])
isSorted(s)
