def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    res=[]
    count=0
    while count+len(weights) <= len(values):
        tmp = values[count:count+len(weights)]
        wma = sum(list(map(lambda x,y: x*y, tmp, weights))) / sum(weights)
        res.append(wma)
        count+=1
    return res