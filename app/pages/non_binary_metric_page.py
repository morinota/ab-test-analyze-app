import streamlit as st
from utils.desirable_sample_size_calculation import (
    DesirableSampleSizeSimulatorWithNonBinaryMetric,
)


def display() -> None:
    st.header("非二値メトリクスの場合の理想的なサンプルサイズ計算")
    acceptable_false_positive_rate = st.number_input(
        "許容する誤陽性率(α)", min_value=0.0, max_value=1.0, value=0.05
    )
    acceptable_false_negative_rate = st.number_input(
        "許容する誤陰性率(β)", min_value=0.0, max_value=1.0, value=0.2
    )
    control_metric_mean = st.number_input(
        "コントロールグループのメトリクスの平均値", min_value=0.0, value=10.0
    )
    treatment_metric_mean = st.number_input(
        "トリートメントグループに期待するメトリクスの平均値", min_value=0.0, value=12.0
    )
    assumed_metric_std = st.number_input(
        "メトリクスの変動性(標準偏差)", min_value=0.0, value=1.0
    )

    if st.button("計算"):
        simulator = DesirableSampleSizeSimulatorWithNonBinaryMetric(
            significance_level=acceptable_false_positive_rate,
            desirable_power=1.0 - acceptable_false_negative_rate,
        )

        assumed_metric_variance = assumed_metric_std**2
        desirable_sample_size = simulator.calculate(
            control_metric_mean,
            treatment_metric_mean,
            metric_variance=assumed_metric_variance,
        )
        st.success(
            f"""
            treatmentに期待する効果量 +{treatment_metric_mean - control_metric_mean} が実際に存在する場合に、
            それを検出力 {1.0 - acceptable_false_negative_rate} で検出するためには、
            各ユーザグループのサンプルサイズは少なくとも {desirable_sample_size} 人が必要です。
            """
        )
