import json,pickle
import numpy as np
def predicted_value(loc,sqft,bath,size):
    loc_ind = __data_col.index(loc.lower())
    X = np.zeros(len(__data_col))
    X[0] = size
    X[1] = sqft
    X[2] = bath
    if loc_ind >= 0:
        X[loc_ind] = 1
    return round(__model.predict([X])[0],2)
def get_location_name():
    return __location
def load_saved_artifacts():
    print("loading....")
    global __data_col
    global __location
    with open("./artifacts/columns.json",'r') as f:
        __data_col=json.load(f)['data-col']
        __location=__data_col[3:]
    global __model
    with open("./artifacts/predict_land_price.pickle",'rb') as f:
        __model=pickle.load(f)
    print("loading...done")
if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_name())
    print(predicted_value('1st Phase JP Nagar',2000,3,3))