def getAndRemoveLastElement(stack:list):
    result = stack.pop()
    if(len(stack) == 0):
        return result
    else:
        last = getAndRemoveLastElement(stack)
        stack.append(result)
        return last
print(getAndRemoveLastElement([1,2,3]))
def reverse(stack:list):
    if(len(stack) == 0):
        return
    i = getAndRemoveLastElement(stack)
    reverse(stack)
    stack.append(i)
    return stack
print(reverse([1,2,3]))