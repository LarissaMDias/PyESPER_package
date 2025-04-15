def pH_adjcalc(DesiredVariables, VerboseTF, Est_pre={}, Cant_adjusted={}, **kwargs):

    """
    Calculating pH adjustment if units are not in molal format
    """

    combos2 = list(Est_pre.keys())
    values2 = list(Est_pre.values())

    if kwargs.get("pHCalcTF") == True and "pH" in DesiredVariables:
        if VerboseTF == True:
            print("Recalculating the pH to be appropriate for pH values calculated from TA and DIC.")  
