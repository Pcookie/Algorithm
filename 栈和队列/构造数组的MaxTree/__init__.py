class Node :
    value = 0
    left = None
    right = None
    def __init__(self, data):
        self.value = data

def getMaxTree(arr:list):
    nArr = [Node] * len(arr)
    for i in range(0, len(arr)):
        # nArr[i] = Node.__init__(, arr[i])
        nArr[i] = Node(arr[i])
    stack = []
    lBigMap = {}
    rBigMap = {}
    for i in range(0, len(nArr)):
        curNode = nArr[i]
        while(len(stack) != 0 and stack[0].value < curNode.value):
            popStackSetMap(stack, lBigMap)
        stack.append(curNode)
    while(len(stack) != 0):
        popStackSetMap(stack, lBigMap)
    for i in range(-1, len(nArr) - 1)[::-1]:
        curNode = nArr[i]
        while(len(stack) != 0 and stack[0].value < curNode.value):
            popStackSetMap(stack, rBigMap)
        stack.append(curNode)
    while(len(stack) != 0):
        popStackSetMap(stack, rBigMap)
    head = None
    for i in range(0, len(nArr)):
        curNode = nArr[i]
        left = lBigMap.get(curNode)
        right = rBigMap.get(curNode)
        if(left == None and right == None):
            head = curNode
        elif(left == None):
            if(right.left == None):
                right.left = curNode
            else:
                right.right = curNode
        elif(right == None):
            if(left.left == None):
                left.left = curNode
            else:
                left.right = curNode
        else:
            parent = left if(left.value < right.value) else right
            if(parent.left == None):
                parent.left = curNode
            else:
                parent.right = curNode
    return head
def popStackSetMap(stack:list, map:dict):
    popNode = stack.pop()
    if(len(stack) == 0):
        map.setdefault(popNode, None)
    else:
        map.setdefault(popNode, stack[-1])

# print(getMaxTree([3, 1, 2]))
# a = getMaxTree([3, 1, 2])
print(getMaxTree([3, 4, 5, 1, 2]))
# print(getMaxTree([3, 4, 5, 1, 2, 1, 3, 6]))
# print(getMaxTree([3, 4, 5, 1, 2]).value)
# print(getMaxTree([3, 4, 5, 1, 2]).left.value)
# print(getMaxTree([3, 4, 5, 1, 2]).left.left.value)
# print(getMaxTree([3, 4, 5, 1, 2]).left.right.value)
# print(getMaxTree([3, 4, 5, 1, 2]).right.value)
# print(getMaxTree([3, 4, 5, 1, 2]).right.left.value)
# print(getMaxTree([3, 4, 5, 1, 2]).right.right.value)