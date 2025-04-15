def adjust_pH_DIC(DesiredVariables, VerboseTF, Dates, Est_pre={}, PredictorMeasurements={}, OutputCoordinates={}, **kwargs):

    """
    Adjusting pH and DIC for anthropogenic carbon.
    """

    import numpy as np
    import math    
    from simplecantestimatelr import simplecantestimatelr
    
    YouHaveBeenWarnedCanth = False

    Cant_adjusted={}
    combos2 = list(Est_pre.keys())
    values2 = list(Est_pre.values())
    values2 = np.array(values2).T
    if "EstDates" in kwargs and ("DIC" in DesiredVariables or "pH" in DesiredVariables):      
        if not YouHaveBeenWarnedCanth:
            if VerboseTF:
                print("Estimating anthropogenic carbon for PyESPER_NN.")
            longitude = np.mod(OutputCoordinates["longitude"], 360)
            latitude = np.array(OutputCoordinates["latitude"])
            depth = np.array(OutputCoordinates["depth"])
            Cant, Cant2002 = simplecantestimatelr(Dates, longitude, latitude, depth)
            YouHaveBeenWarnedCanth = True
       
        for combo, a in zip(combos2, values2):
            dic = []
            if combo.startswith("DIC"):

                for vala, Canta, Cant2002a in zip(a, Cant, Cant2002):
                    if math.isnan(vala): 
                        dic.append("nan")
                    else:
                        dic.append(vala + Canta - Cant2002a)
            else:
                dic = list(a)
            Cant_adjusted[combo] = dic

    return Cant_adjusted, Cant, Cant2002
