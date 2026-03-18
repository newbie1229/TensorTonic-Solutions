def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    res=[values[0]]
    for i in range(1,len(values)):
        ema = values[i]*alpha + res[i-1]*(1-alpha)
        res.append(ema)
    return res