import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 440047378

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return 0.077 / (1 - alpha), max(x)
