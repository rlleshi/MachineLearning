import pandas as pd
import numpy as np
from scipy.io.arff import loadarff

if __name__ == '__main__':
    raw_data = loadarff('autism_adult_data.arff')
    data = pd.DataFrame(raw_data[0])
    
    for col in data.columns:
        if col in ['age', 'result']: continue
        try:
            # Map from bytes to string & convert to float
            data[col] = data[col].map(lambda x: x.decode('utf-8'))
            try: 
                data[col] = data[col].astype(np.float32)
            except ValueError: continue
        except AttributeError:
            # Map the rest of the attributes to string
            data[col] = data[col].map(lambda x: lambda y: str(y, 'utf-8'))
    
    data.to_csv('autism_adult.csv', index=False)