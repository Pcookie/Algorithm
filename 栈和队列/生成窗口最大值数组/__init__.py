def detMaxWindow(arr:list, w):
    if(arr is None or w < 1 or len(arr) < w):
        return None
    qmax = []
    res = [1] * (len(arr) - w + 1)
    index = 0
    for i in range(0, len(arr)):
        while(len(qmax) != 0 and arr[qmax[-1]] <= arr[i]):
            qmax.pop()
        qmax.append(i)
        if(qmax[0] == i-w):
            qmax.pop(0)
        if(i >= w - 1):
            res[index] = arr[qmax[0]]
            index += 1
    return res
print(detMaxWindow([4, 3, 5, 4, 3, 3, 6, 7], 3))