from desirable_sample_size_calculation import (
    DesirableSampleSizeSimulatorWithBinaryMetric,
    DesirableSampleSizeSimulatorWithNonBinaryMetric,
)


def test_desirable_sample_size_calculation_with_binary_metric() -> None:
    # Arrange
    significance_level = 0.05  # i.e. acceptable false positive rate
    desirable_power = 0.8

    ## practice論文のsectin 3.2の例に従い、一人当たりconversion rateをOECとする
    control_metric_mean = 0.05
    ## ベルヌーイ試行のmetricの変動性(標準偏差)はsqrt(mean * (1 - mean))であるため、control_metric_mean=0.05の場合、標準偏差は0.217
    treatment_metric_mean = control_metric_mean * (1 + 0.05)  # OEC5%の増加を仮定

    sut = DesirableSampleSizeSimulatorWithBinaryMetric(
        significance_level,
        desirable_power,
    )

    # Act
    desirable_sample_size_actual = sut.calculate(
        control_metric_mean,
        treatment_metric_mean,
    )

    # Assert
    expected = 121599  # 公式より 16 * (0.05 *(1-0.05))**2/(0.05 * 0.05)^2
    assert expected - 1000 <= desirable_sample_size_actual <= expected + 1000


def test_desirable_sample_size_calculation_with_non_binary_metric() -> None:
    # Arrange
    significance_level = 0.05
    desirable_power = 0.8

    ## practice論文のsectin 3.2の例に従い、OECを一人当たりのconversion金額とする
    control_metric_mean = 3.75  # 一人あたり平均3.75ドル
    metric_variance = 30**2  # OECの変動性=標準偏差30ドル
    treatment_metric_mean = control_metric_mean * (1 + 0.05)  # OECの5%の増加を仮定

    sut = DesirableSampleSizeSimulatorWithNonBinaryMetric(
        significance_level,
        desirable_power,
    )

    # Act
    desirable_sample_size_actual = sut.calculate(
        control_metric_mean,
        treatment_metric_mean,
        metric_variance,
    )

    # Assert
    expected = 409600  # 公式より 16 * (30)^2/(3.75 * 0.05)^2
    assert expected - 1000 <= desirable_sample_size_actual <= expected + 1000
