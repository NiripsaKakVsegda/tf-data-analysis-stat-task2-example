import pandas as pd
import numpy as np

from scipy import stats


chat_id = 440047378

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mean = np.mean(x)
    std = np.std(x, ddof=1) / np.sqrt(n) 
    alpha = 1 - p
    t_score = abs(stats.t.ppf(alpha / 2, n - 1))
    left_bound = mean - t_score * std
    right_bound = mean + t_score * std
    return left_bound, right_bound
