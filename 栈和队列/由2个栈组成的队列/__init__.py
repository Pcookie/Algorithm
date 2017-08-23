class TwoStacksQueue:
    __stackPush = []
    __stackPop = []
    def add(self, pushInt):
        TwoStacksQueue.__stackPush.append(pushInt)
    def poll(self):
        if((len(TwoStacksQueue.__stackPop) == 0) and (len(TwoStacksQueue.__stackPush) == 0)):
            print("Queue is empty")
        elif(len(TwoStacksQueue.__stackPop) == 0):
            while (len(TwoStacksQueue.__stackPush) != 0):
                TwoStacksQueue.__stackPop.append(TwoStacksQueue.__stackPush.pop())
        return TwoStacksQueue.__stackPop.pop()
    def peek(self):
        if(len(TwoStacksQueue.__stackPop) == 0 and len(TwoStacksQueue.__stackPush) == 0):
            print("Queue is empty")
        elif(len(TwoStacksQueue.__stackPop) == 0):
            while(len(TwoStacksQueue.__stackPush) != 0):
                TwoStacksQueue.__stackPop.append(TwoStacksQueue.__stackPush.pop())
        return TwoStacksQueue.__stackPop[-1]
def a():
    twoSQ = TwoStacksQueue();
    twoSQ.add(1)
    twoSQ.add(3)
    twoSQ.add(2)
    twoSQ.add(4)
    print(twoSQ.peek())
    print(twoSQ.poll())
    print(twoSQ.poll())
    print(twoSQ.peek())
a()