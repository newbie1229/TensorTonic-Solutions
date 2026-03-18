def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    res=[]
    count=0
    while count+window_size <= len(values):
        sma = sum(values[count:count+window_size]) / window_size
        res.append(sma)
        count+=1
    return res
            