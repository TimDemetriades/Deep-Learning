import numpy as np
import os
import pandas as pd

# "housing.csv" is posted on canvas Week 2
housing=pd.read_csv("housing.csv") 
housing.head()

import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
plt.show()


import tensorflow as tf
from keras.layers import Input, Dense
from keras.models import Model