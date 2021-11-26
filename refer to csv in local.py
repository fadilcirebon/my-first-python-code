import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv(r"C:\Users\fadil\Downloads\123.csv")

x_label= table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.show()