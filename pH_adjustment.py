def pH_adjustment(
    DesiredVariables,
    EstDates 
#    Cant, 
#    Cant2002, 
#    combos2={}, 
#    values2={}, 
#    PredictorMeasurements={}, 
#    OutputCoordinates={}, 
#    C={}, 
#    PM_pH={}, 
#    Uncertainties_pre={}, 3
#    DUncertainties_pre={}
):

    """
    Adjusting pH for anthropogenic carbon
    """

    import numpy as np
    import seawater as sw
    import PyCO2SYS as pyco2

