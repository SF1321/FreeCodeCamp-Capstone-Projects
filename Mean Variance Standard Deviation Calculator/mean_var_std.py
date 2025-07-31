import numpy as np

def calculate(input):
    if len(input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #converting in numpy array + reshaping
    calcs = np.array(input)
    calcs = calcs.reshape(3,3)
    
    #mean calculations
    meancalcs = [np.mean(calcs, axis = 0).tolist(),
                 np.mean(calcs, axis = 1).tolist(),
                 np.mean(calcs).tolist()]

    #variance calculations
    varcalcs = [np.var(calcs, axis = 0).tolist(),
                 np.var(calcs, axis = 1).tolist(),     
                 np.var(calcs).tolist()]

    
    #std deviation calculations
    sdcalcs = [np.std(calcs, axis = 0).tolist(),
                 np.std(calcs, axis = 1).tolist(),
                 np.std(calcs).tolist()]
    
    #max calculations
    maxcalcs = [np.max(calcs, axis = 0).tolist(),
                 np.max(calcs, axis = 1).tolist(),
                 np.max(calcs).tolist()]
    
    #min calculations  
    mincalcs = [np.min(calcs, axis = 0).tolist(),
                 np.min(calcs, axis = 1).tolist(),
                 np.min(calcs).tolist()]
    
    #sum calculation
    sumcalcs = [np.sum(calcs, axis = 0).tolist(),
                 np.sum(calcs, axis = 1).tolist(),
                 np.sum(calcs).tolist()]
    
    calculations = {'mean' : meancalcs, 'variance' : 
        varcalcs, 'standard deviation' : sdcalcs, 'max' : 
            maxcalcs, 'min' : mincalcs, 'sum' : sumcalcs}

    return calculations