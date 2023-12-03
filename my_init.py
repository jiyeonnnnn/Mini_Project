import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import my_function as mfn
from datetime import datetime

from matplotlib import font_manager

font_path = 'C:/Windows/Fonts/malgun.ttf'
plt.rcParams['font.family'] = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['axes.unicode_minus'] = False

pd.options.display.max_rows = 200
pd.options.display.max_columns = 40