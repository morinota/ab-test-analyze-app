import numpy as np
from alternative_hypothesis_type import (
    AlternativeHypothesisType,
)
from normal_distribution import ProbabilityDistribution
from statistical_power_calculation import calculate_statistical_power


def test_calculate_statistical_power() -> None:
    # Arrange
    n = 100

    null_distribution = ProbabilityDistribution(
        mean=0.5,
        std=np.sqrt(0.5 * (1 - 0.5) / n),
    )
    alternative_distribution = ProbabilityDistribution(
        mean=0.64,
        std=np.sqrt(0.64 * (1 - 0.64) / n),
    )

    acceptable_false_positive_rate = 0.05
    alternative_type = AlternativeHypothesisType.GREATER_THAN

    # Act
    actual_statistical_power = calculate_statistical_power(
        null_distribution,
        alternative_distribution,
        acceptable_false_positive_rate,
        alternative_type,
    )

    # Assert
    expected_statistical_power = 0.886
    assert np.isclose(actual_statistical_power, expected_statistical_power, atol=0.01)


if __name__ == "__main__":
    n = 10000
    control_OEC_mean = 0.05
    control_OEC_std = np.sqrt(control_OEC_mean * (1 - control_OEC_mean) / n)
    treatment_OEC_mean = control_OEC_mean * (1 + 0.05)
    treatment_OEC_std = np.sqrt(treatment_OEC_mean * (1 - treatment_OEC_mean) / n)

    null_dist = ProbabilityDistribution(mean=0.0, std=np.sqrt(2 * 0.05 * (1 - 0.05) / n))
    alternative_dist = ProbabilityDistribution(
        mean=treatment_OEC_mean - control_OEC_mean,
        std=np.sqrt(control_OEC_mean * (1 - control_OEC_mean) / n + treatment_OEC_mean * (1 - treatment_OEC_mean) / n),
    )

    print(
        calculate_statistical_power(
            null_dist,
            alternative_dist,
            0.05,
            AlternativeHypothesisType.GREATER_THAN,
        )
    )
