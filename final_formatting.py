def final_formatting(Cant_adjusted={}, Est_pre={}):

    """
    Formatting the final bits.
    """
    
    import numpy as np
    import pandas as pd

    combos2 = list(Est_pre.keys())
    values2 = list(Est_pre.values())

    combos3 = list(Cant_adjusted.keys())
    values3 = list(Cant_adjusted.values())
    values2 = np.array(values2[0])
    values3 = np.array(values3[0])
    print(values2, values3)    
    Estimates={}
        
    return Estimates
