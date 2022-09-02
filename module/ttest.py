import numpy as np
from scipy import stats

def new_welch_test(A, B):
  result = stats.ttest_ind(A, B, equal_var=False)
  print('p-value: ', result.pvalue)