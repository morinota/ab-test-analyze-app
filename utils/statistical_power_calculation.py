from utils.alternative_hypothesis_type import AlternativeHypothesisType
from utils.normal_distribution import ProbabilityDistribution
from typing import Optional


def calculate_statistical_power(
    null_distribution: ProbabilityDistribution,
    alternative_distribution: ProbabilityDistribution,
    acceptable_false_positive_rate: float = 0.05,
    alternative_hypothesis_type: AlternativeHypothesisType = AlternativeHypothesisType.GREATER_THAN,
) -> float:
    left_critical_value, right_critical_value = get_rejection_region(
        null_distribution, acceptable_false_positive_rate, alternative_hypothesis_type
    )

    # 対立分布のうちrejection regionに含まれる部分の面積を算出
    true_positive_area = 0
    if left_critical_value:
        true_positive_area += alternative_distribution.cdf(left_critical_value)
    if right_critical_value:
        true_positive_area += 1 - alternative_distribution.cdf(right_critical_value)
    return true_positive_area / 1


def get_rejection_region(
    null_distribution: ProbabilityDistribution,
    acceptable_false_positive_rate: float,
    alternative_type: AlternativeHypothesisType,
) -> tuple[Optional[float], Optional[float]]:
    """critical valueのタプルを返す
    - 片側検定の場合は片方のみの値が入る
    """
    assert 0 < acceptable_false_positive_rate < 1

    has_left_rejection_region = alternative_type.has_left_rejection_region
    has_right_rejection_region = alternative_type.has_right_rejection_region

    if has_left_rejection_region and has_right_rejection_region:
        return (
            null_distribution.ppf(acceptable_false_positive_rate / 2),
            null_distribution.ppf(1 - acceptable_false_positive_rate / 2),
        )

    if has_left_rejection_region:
        return (null_distribution.ppf(acceptable_false_positive_rate), None)

    return (None, null_distribution.ppf(1 - acceptable_false_positive_rate))
