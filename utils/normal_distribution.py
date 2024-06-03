from typing import Literal, Optional
from scipy.stats import norm
import numpy as np


class ProbabilityDistribution:
    def __init__(self, mean: float, std: float):
        self.mean = mean
        self.std = std
        self.dist = norm(loc=mean, scale=std)

    def pdf(self, x: float) -> float:
        """probability density function"""
        return self.dist.pdf(x)

    def cdf(self, x: float) -> float:
        """cumulative distribution function"""
        return self.dist.cdf(x)

    def ppf(self, q: float) -> float:
        """percent point function(累積分布関数の逆関数)"""
        return self.dist.ppf(q)
