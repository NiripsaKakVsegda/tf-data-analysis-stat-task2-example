import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 440047378

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    
    n = len(x)
    k = int(n * alpha / 2)
    sorted_levels = sorted(x)
    b_min = sorted_levels[k]
    b_max = sorted_levels[n-k-1]
    return (b_min, b_max)
