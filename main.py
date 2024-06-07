from scipy.io import arff
import pandas as pd

data = arff.loadarff('TrainingDataset.arff')
df = pd.DataFrame(data[0])
as1 = df.head()
