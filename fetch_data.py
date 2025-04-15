def fetch_data (DesiredVariables, Path):
    
    """
    Gathers the necessary LIR files similar to ESPERs
    """

    from scipy.io import loadmat
    import numpy as np
    import pandas as pd

    AAIndsCs, GridCoords, Cs = {}, {}, {}

    for v in DesiredVariables:               
        P = Path
        fname = f"{P}/Mat_fullgrid/LIR_files_{v}_full2024.mat"
        name = f"LIR_files_{v}_full.mat"
        LIRs = loadmat(fname)
        UncGrid = LIRs["UncGrid"][0][0] 
        GridCoodata, Csdata, AAInds = np.array(LIRs["GridCoords"]), np.array(LIRs["Cs"]), np.array(LIRs["AAIndsM"]) 
        AAIndsCs[v] = pd.DataFrame(data=AAInds)
        GridCoords[v] = pd.DataFrame(data=GridCoodata[:, :])
        Cs[v] = [pd.DataFrame(data=Csdata[:, :, i]) for i in range(16)]
      
    LIR_data = [GridCoords, Cs, AAIndsCs, UncGrid]
    return LIR_data
