import numpy as np
import pandas as pd
import string
import patsy
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as stats
import statsmodels.formula.api as sm
from matplotlib.ticker import FuncFormatter






import warnings
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn #ignore annoying warning (from sklearn and seaborn)


def corr_heatmap(data, method = "pearson",annot=True):
    # Set the default matplotlib figure size:
    mean_corr = data.corr(method = method)
    
    # Generate a mask for the upper triangle (taken from seaborn example gallery)
    mask = np.zeros_like( mean_corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    
    # Plot the heatmap with seaborn.
    # Assign the matplotlib axis the function returns. This will let us resize the labels.
    fig, ax = plt.subplots(figsize=(15,10))
    ax = sns.heatmap(mean_corr, ax=ax,  square = True, mask=mask, linecolor='white', annot = annot , cmap='RdBu', vmin=-1, vmax=1, fmt = '.2f')

    # Resize the labels.
    ax.set_xticklabels(ax.xaxis.get_ticklabels(), fontsize=14, rotation=90)
    ax.set_yticklabels(ax.yaxis.get_ticklabels(), fontsize=14, rotation=0)

    plt.show()
    
    
    

