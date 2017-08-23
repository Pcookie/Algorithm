class MyStack2 :
    '压入式费空间 但是弹出省时间'
    __stackData = []
    __stackMin = []
    def push(self, num):
        if(len(MyStack2.__stackMin) == 0):
            MyStack2.__stackMin.append(num)
        elif(num <= MyStack2.getmin()):
            MyStack2.__stackMin.append(num)
        else:
            newMin = MyStack2.__stackMin[-1]
            MyStack2.__stackMin.append(newMin)
        MyStack2.__stackData.append(num)
    def pop(self):
        if (len(MyStack2.__stackData) == 0):
            print("Your stack is empty")
        MyStack2.__stackMin.pop()
        return MyStack2.__stackData.pop()
    def getmin(*args):
        if(len(MyStack2.__stackMin) == 0):
            print("Your stack is empty")
        return MyStack2.__stackMin[-1]
def a():
    sta = MyStack2()
    sta.push(4)
    sta.push(2)
    sta.push(3)
    sta.push(1)
    sta.push(4)
    # sta.pop()
    # sta.pop()
    sta.pop()
    sta.pop()
    print(sta.getmin())
a()