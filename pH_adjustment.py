def pH_adjustment(
    Path,
    DesiredVariables,
    Dates, 
    Cant, 
    Cant2002,
    PerKgSwTF, 
    Cant_adjusted={},
    Est_pre={}, 
    PredictorMeasurements={}, 
    OutputCoordinates={}, 
    C={},  
    Uncertainties_pre={}, 
    DUncertainties_pre={},
    **kwargs
):

    """
    Adjusting pH for anthropogenic carbon
    """

    import numpy as np
    import seawater as sw
    import PyCO2SYS as pyco2
    from inputdata_organize import inputdata_organize
    from temperature_define import temperature_define
    from iterations import iterations
    from fetch_data import fetch_data

    combos2 = list(Est_pre.keys())
    values2 = list(Est_pre.values())

    if "EstDates" in kwargs and ("DIC" in DesiredVariables or "pH" in DesiredVariables):      
        if "pH" in DesiredVariables:
            print("pH is detected")
            warning = []
            for combo, values in zip(combos2, values2):
                if combo.startswith("pH"):
                    salinity = PredictorMeasurements["salinity"]
                    PM_pH = {"salinity": salinity}
                    eq = [16]            
                    InputAll = inputdata_organize(
                        Dates,
                        C,
                        PredictorMeasurements,
                        Uncertainties_pre
                    )
                    PredictorMeasurements, InputAll = temperature_define(
                        ["TA"],
                        PredictorMeasurements,
                        InputAll,
                        **kwargs
                    )
                    code, unc_combo_dict, dunc_combo_dict = iterations(
                        ["TA"], 
                        eq,
                        PerKgSwTF,
                        C,
                        PredictorMeasurements,
                        InputAll,
                        Uncertainties_pre,
                        DUncertainties_pre
                    )
                    LIR_data = fetch_data(["TA"], Path)
