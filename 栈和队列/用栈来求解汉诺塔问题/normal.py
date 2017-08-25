'正常汉诺塔'
def hanoiProblem1(num, left:str, mid:str, right:str):
    if(num < 1):
        return 0
    return process(num, left, mid, right, left, right)
def process(num, left:str, mid:str, right:str, myfrom:str, to:str):
    if(num == 1):
        print("move 1 from " + myfrom + " to " + to)
        return 1
    else:
        another = right if (myfrom is left or to is left) else left
        part1 = process(num - 1, left, mid, right, myfrom, another)
        part2 = 1
        print("move " + str(num) + " from " + myfrom + " to " + to)
        part3 = process(num - 1, left, mid, right, another, to)
        return part1 + part2 + part3