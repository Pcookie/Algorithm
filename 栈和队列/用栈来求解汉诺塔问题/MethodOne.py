'递归的方法'
def hanoiProblem1(num, left:str, mid:str, right:str):
    if(num < 1):
        return 0
    return process(num, left, mid, right, left, right)
def process(num, left:str, mid:str, right:str, myfrom:str, to:str):
    if(num == 1):
        if(myfrom is mid or to is mid):
            print("move 1 from " + myfrom + " to " + to)
            return 1
        else:
            print("move 1 from " + myfrom + " to " + mid)
            print("move 1 from " + mid + " to " + to)
            return 2
    if(myfrom is mid or to is mid):
        another = right if (myfrom is left or to is left) else left
        part1 = process(num - 1, left, mid, right, myfrom, another)
        part2 = 1
        print("move " + str(num) + " from " + myfrom + " to " + to)
        part3 = process(num - 1, left, mid, right, another, to)
        return part1 + part2 + part3
    else:
        part1 = process(num - 1, left, mid, right, myfrom, to)
        part2 = 1
        print("move " + str(num) + " from " + myfrom + " to " + mid)
        part3 = process(num - 1, left, mid, right, to, myfrom)
        part4 = 1
        print("move " + str(num) + " from " + mid + " to " + to)
        part5 = process(num - 1, left, mid, right, myfrom, to)
        return part1 + part2 + part3 + part4 + part5

print(hanoiProblem1(3, "a", "b", "c"))
