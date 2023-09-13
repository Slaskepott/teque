import collections
import sys

left = collections.deque()
right = collections.deque()

def push_front(x):
    left.appendleft(x)
    balance()

def push_back(x):
    right.append(x)
    balance()

def push_middle(x):
    left.append(x)
    balance()

def get(i):
    if(i<len(left)):
        return left[i]
    return right[i-len(left)]

def balance():
    if(len(left)>len(right)+1):
        right.appendleft(left.pop())
    elif(len(right)>len(left)):
        left.append(right.popleft())

amountOp = int(sys.stdin.readline())
for i in range(0,amountOp):
    op = sys.stdin.readline().strip().split(" ")
    command = int(op[1])

    if(op[0]=="push_back"):
        push_back(command)
    elif(op[0]=="push_front"):
        push_front(command)
    elif(op[0]=="push_middle"):
        push_middle(command)
    else:
        print(get(command))