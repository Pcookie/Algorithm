'非递归方法，用栈来模拟汉诺塔的三个塔'
from enum import Enum
import sys

class Actions(Enum):
    No = 'No'
    LToM = 'LToM'
    MToL = 'MToL'
    MToR = 'MToR'
    RToM = 'RToM'

def hanoiProblem2(num, left:str, mid:str, right:str):
    lS = []
    mS = []
    rS = []
    lS.append(sys.maxsize)
    mS.append(sys.maxsize)
    rS.append(sys.maxsize)
    for i in range(0, num)[::-1]:
        lS.append(i)
    record = [{Actions.No.value}]
    step = 0
    while (len(rS) != num + 1):
        print(step)
        step += fStackTotStack(record, Actions.MToL.value, Actions.LToM.value, lS, mS, left, mid)
        print(step)
        step += fStackTotStack(record, Actions.LToM.value, Actions.MToL.value, mS, lS, mid, left)
        print(step)
        step += fStackTotStack(record, Actions.RToM.value, Actions.MToR.value, mS, rS, mid, right)
        print(step)
        step += fStackTotStack(record, Actions.MToR.value, Actions.RToM.value, rS, mS, right, mid)
        print(step)
    return step
def fStackTotStack(record, preNoAct, nowAct, fStack, tStack, myfrom, to):
    if(record[0] != preNoAct and fStack[-1] < tStack[-1]):
        tStack.append(fStack.pop())
        print("move " + str(tStack[-1]) + " from " + myfrom + " to " + to)
        record[0] = nowAct
        return 1
    return 0
print(hanoiProblem2(4, 'a', 'b', 'c'))