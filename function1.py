
# Function for data metrics
def dictionary_of_metrics(items):
    
    return {'mean':round(np.mean(items),2),
            'median':np.median(items), 
            'var':round(np.var(items,ddof=1),2),
            'std':round(np.std(items,ddof=1),2),
            'min':np.min(items),
            'max':np.max(items)}

