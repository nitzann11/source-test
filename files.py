from pickle import dump,load


def save_data(filename:str="garage.pickle",data=[]):
    with open(filename,"wb") as f:
        dump(data,f)

def load_data(filename:str="garage.pickle"):
    try:
        with open(filename,"rb") as f:
            data=load(f)
            return data
    except:
            with open(filename,"wb") as f:
                dump([],f)
                return []