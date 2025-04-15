def lir(DesiredVariables, Path, OutputCoordinates={}, PredictorMeasurements={}, **kwargs):
    
    """
    Locally Interpolated Regressions (LIRs) for Empirical Seawater Property Estimation
    """

    import pandas as pd
    import time
    from errors import errors
    from defaults import defaults
    from lir_uncertainties import measurement_uncertainty_defaults
    from inputdata_organize import inputdata_organize
    from temperature_define import temperature_define
    from iterations import iterations
    from fetch_data import fetch_data
    from input_AAinds import input_AAinds
    from coefs_AAinds import coefs_AAinds
    from interpolate import interpolate
    from organize_data import organize_data
    from emlr_estimate import emlr_estimate
    from adjust_pH_DIC import adjust_pH_DIC
    from pH_adjustment import pH_adjustment

    # Starting the timer
    tic = time.perf_counter() 
    
    # Function that provides custom error messages for erroneous input
    errors(OutputCoordinates, PredictorMeasurements)

    # Function which calculates default measurement uncertainties
    Equations, n, e, p, VerboseTF, EstDates, C, PerKgSwTF, MeasUncerts = defaults(
        DesiredVariables, 
        OutputCoordinates, 
        **kwargs
    )
    
    # Function that processes the input values and default uncertainties and makes sense of it
    Uncertainties_pre, DUncertainties_pre  = measurement_uncertainty_defaults(
        n, 
        PredictorMeasurements, 
        MeasUncerts
    )
    
    # Creating a pandas DataFrame of input data
    InputAll  = inputdata_organize(
        EstDates, 
        C, 
        PredictorMeasurements, 
        Uncertainties_pre
    )

    PredictorMeasurements, InputAll = temperature_define(
        DesiredVariables,
        PredictorMeasurements,
        InputAll,
        **kwargs
    )

    code, unc_combo_dict, dunc_combo_dict = iterations(
        DesiredVariables, 
        Equations, 
        PerKgSwTF,
        C,
        PredictorMeasurements, 
        InputAll,
        Uncertainties_pre,
        DUncertainties_pre
    )

    # Loading the data
    LIR_data = fetch_data(DesiredVariables, Path)

    # Separating user-defined coordinates into Atlantic and Arctic or other regions
    AAdata, Elsedata = input_AAinds(C, code)

    # Separating ESPER pre-defined coefficients into Atlantic and Arctic or other regions
    Gdf, CsDesired = coefs_AAinds(Equations, LIR_data)

    # Interpolate
    aaLCs, aaInterpolants_pre, elLCs, elInterpolants_pre = interpolate(Gdf, AAdata, Elsedata)
 
    # Organize data and compute estimates
    Estimate, CoefficientsUsed = organize_data(
        aaLCs, 
        elLCs, 
        aaInterpolants_pre, 
        elInterpolants_pre, 
        Gdf, 
        AAdata,
        Elsedata
    )

    EMLR = emlr_estimate(
        Equations, 
        DesiredVariables, 
        Path,
        OutputCoordinates, 
        PredictorMeasurements, 
        unc_combo_dict, 
        dunc_combo_dict,
        Coefficients=CoefficientsUsed)
   
    Cant_adjusted, Cant, Cant2002 = adjust_pH_DIC(
        DesiredVariables,
        VerboseTF,
        EstDates,
        Estimate,
        PredictorMeasurements,
        OutputCoordinates,
        **kwargs)

    Cant_adjusted = pH_adjustment(
        Path,
        DesiredVariables, 
        EstDates, 
        Cant,
        Cant2002, 
        PerKgSwTF,
        Cant_adjusted, 
        Estimate,
        PredictorMeasurements,
        OutputCoordinates,
        C,
        Uncertainties_pre,
        DUncertainties_pre,
        **kwargs)

     # Stopping the timer
    toc = time.perf_counter()
    print(f"PyESPER_LIR took {toc - tic:0.4f} seconds, or {(toc-tic)/60:0.4f} minutes to run")    

    # DEBUG 
#    print(Cant2002)
