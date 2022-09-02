import numpy as np
from scipy import stats

# Welchのt検定
def welch_test(A, B):
  A_var = np.var(A, ddof=1)  # Aの不偏分散
  B_var = np.var(B, ddof=1)  # Bの不偏分散！！
  A_df = len(A) - 1  # Aの自由度
  B_df = len(B) - 1  # Bの自由度
  f = A_var / B_var  # F比の値
  one_sided_pval1 = stats.f.cdf(f, A_df, B_df)  # 片側検定のp値 1
  one_sided_pval2 = stats.f.sf(f, A_df, B_df)   # 片側検定のp値 2
  two_sided_pval = min(one_sided_pval1, one_sided_pval2) * 2  # 両側検定のp値

  print('F:       ', f)
  print('p-value: ', two_sided_pval)


def new_welch_test(A, B):
  result = stats.ttest_ind(A, B, equal_var=False)
  print('p-value: ', result.pvalue)