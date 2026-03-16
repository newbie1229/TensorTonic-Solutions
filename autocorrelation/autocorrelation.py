def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    res=[1]
    mean_value = sum(series) / len(series)
    variance=0
    for i in range(len(series)):
       variance += (series[i] - mean_value) ** 2 
    if variance==0:
        while len(res) !=3:
            res.append(0)
        return res
    
    for k in range(1,max_lag+1):
        numerator=0
        for i in range(k, len(series)):
            if i-k!=0:
                numerator += (series[i] - mean_value) * (series[i-k] - mean_value)
            else:
                numerator += (series[i] - mean_value) * (series[0] - mean_value)
        res.append(numerator/variance)
    if len(res)==max_lag+1:
        return res
            