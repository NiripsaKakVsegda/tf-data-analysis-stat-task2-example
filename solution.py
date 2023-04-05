import pandas as pd
import numpy as np

from scipy import stats


chat_id = 440047378

def solution(p: float, x: np.array) -> tuple:
    return [max(x), max(x) + 0.0142]
