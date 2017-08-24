class MyStack1 :
    '压入时省空间 但是弹出操作费时间'
    __stackData = []
    __stackMin = []
    def push(self, num):
        if(len(MyStack1.__stackMin) == 0):
            MyStack1.__stackMin.append(num)
        elif(num <= MyStack1.getmin()):
            MyStack1.__stackMin.append(num)
        MyStack1.__stackData.append(num)
    def pop(self):
        if (len(MyStack1.__stackData) == 0):
            raise Exception("Your stack is empty")
        value = MyStack1.__stackData.pop()
        if (value == MyStack1.getmin()):
            MyStack1.__stackMin.pop()
        return value
    def getmin(*args):
        if(len(MyStack1.__stackMin) == 0):
            raise Exception("Your stack is empty")
        # print(MyStack1.__stackMin)
        # print(MyStack1.__stackData)
        return MyStack1.__stackMin[-1]
def a():
    sta = MyStack1()
    sta.push(4)
    sta.push(2)
    sta.push(3)
    sta.push(1)
    sta.push(4)
    sta.pop()
    sta.pop()
    # sta.pop()
    # sta.pop()
    print(sta.getmin())
a()