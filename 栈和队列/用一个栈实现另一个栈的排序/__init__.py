def sortStackByStack(stack):
    help = []
    while(len(stack) != 0):
        cur = stack.pop()
        while(len(help) != 0 and help[len(help) - 1] < cur):
            stack.append(help.pop())
        help.append(cur)
    while(len(help) != 0):
        stack.append(help.pop())
    print(stack)
sortStackByStack([-3, 4, 1, 2, 3, 0, -6, 2, 3])