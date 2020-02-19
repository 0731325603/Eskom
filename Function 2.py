#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Five number summary
def five_num_summary(items):

    mx = np.max(items)
    q2 = np.median(items)
    mn = np.min(items)
    q1 = np.percentile(items,25)
    q3 = np.percentile(items,75)
    dic =  {'max': mx, 'median': q2, 'min': mn, 'q1': q1, 'q3': q3}

    return dic

