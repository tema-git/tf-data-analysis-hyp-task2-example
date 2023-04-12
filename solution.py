import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp
chat_id = 401141478

def solution(x: np.array, y: np.array) -> bool:
    sl = 0.02
    pval = anderson_ksamp([x, y])[2]

    return pval < sl
