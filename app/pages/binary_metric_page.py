import streamlit as st

from utils.desirable_sample_size_calculation import (
    DesirableSampleSizeSimulatorWithBinaryMetric,
)

RELATIVE_EFFECT_SIZE_TEXT = "1. 期待する相対的な効果量(ex. コントロールと比較して+1.2倍の改善を期待する → 「20%」を入力)"
ABSORUTE_TREATMENT_EXPECTATION_TEXT = (
    "2. トリートメントグループに期待するメトリクスの平均値"
)


def display():
    st.header("二値メトリクスの場合、以下の設定を入力してください")
    acceptable_false_positive_rate = st.number_input(
        "今回のABテストで許容する誤陽性率(i.e. 有意水準)",
        min_value=0.0,
        max_value=1.0,
        value=0.05,
    )
    acceptable_false_negative_rate = st.number_input(
        "今回のABテストで許容する誤陰性率",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
    )
    control_metric_mean = (
        st.number_input(
            "コントロールグループのメトリクスの平均値 (%)",
            min_value=0.0,
            value=5.0,
        )
        / 100
    )

    # 期待する効果量 もしくは トリートメントグループに期待するメトリクスの平均値を入力する
    ## どちらか選択して、入力可能にする
    option = st.radio(
        "以下のうち、どちらか片方を入力してください。",
        (RELATIVE_EFFECT_SIZE_TEXT, ABSORUTE_TREATMENT_EXPECTATION_TEXT),
    )

    if option == RELATIVE_EFFECT_SIZE_TEXT:
        relative_effect_size = (
            st.number_input(RELATIVE_EFFECT_SIZE_TEXT, min_value=0.0, value=5.0) / 100
        )
        treatment_metric_mean = control_metric_mean * (1 + relative_effect_size)
    else:
        treatment_metric_mean = st.number_input(
            ABSORUTE_TREATMENT_EXPECTATION_TEXT, min_value=0.0, value=4.25
        )
        relative_effect_size = (
            (treatment_metric_mean - control_metric_mean) / control_metric_mean * 100
        )

    if st.button("計算"):
        simulator = DesirableSampleSizeSimulatorWithBinaryMetric(
            significance_level=acceptable_false_positive_rate,
            desirable_power=1.0 - acceptable_false_negative_rate,
        )
        desirable_sample_size = simulator.calculate(
            control_metric_mean=control_metric_mean,
            treatment_metric_mean=treatment_metric_mean,
        )

        st.success(
            f"""
            トリートメントに相対的な効果量 +{relative_effect_size * 100}% が実際に存在する場合に、
            それを検出力 {1.0 - acceptable_false_negative_rate} で検出するためには、
            各ユーザグループのサンプルサイズは少なくとも {desirable_sample_size} 人が必要です。
            """
        )
