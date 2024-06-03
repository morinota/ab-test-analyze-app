import streamlit as st
from streamlit import selectbox
from app.pages import binary_metric_page, non_binary_metric_page

# タイトルの設定()
st.title("ABテストの適切なサンプルサイズ計算アプリ")


# metricのタイプを選択するためのドロップダウンをメインページに配置。
option = st.selectbox(
    "計算したいメトリクスの種類を選択してください",
    ("二値メトリクス(ex. CTR, 解約率)", "非二値メトリクス(ex. 購入数、売上)"),
)

if option == "二値メトリクス(ex. CTR, 解約率)":
    binary_metric_page.display()
else:
    non_binary_metric_page.display()
