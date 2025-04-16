def final_formatting(Cant_adjusted={}, Est_pre={}):

    """
    Formatting the final bits.
    """
    
    import numpy as np

    combos2 = list(Est_pre.keys())
    values2 = list(Est_pre.values())

    combos3 = Cant_adjusted.keys()
    values3 = Cant_adjusted.values()
    
    Estimates={}
    k2 = list(combos2)
    v2 = list(values2)
    
    k3 = list(combos3)
    v3 = list(values3)
    v3 = v3[0]
    for keys2 in range(0, len(k2)):
        ar2 = np.array(v2[keys2])
        for keys3 in range(0, len(k3)):
            ar2[k2[keys2] == k3[keys3]] = v3[keys3]

        Estimates[k2[keys2]] = ar2
        Estimates = pd.DataFrame(Estimates)

    return Estimates
