# root directoryをpythonのpathに追加する
import sys
from pathlib import Path

root_dir = str(Path(__file__).parent.parent)
print(root_dir)
sys.path.append(root_dir)

import streamlit as st
from app.pages import binary_metric_page, non_binary_metric_page


# タイトルの設定()
st.title("under-poweredなABテストを避けるための適切なサンプルサイズ計算")

METRIC_TYPE_QUESTION_TEXT = "計算したいメトリクスの種類を選択してください"
BINARY_METRIC_TEXT = "二値メトリクス(ex. CTR, 解約率, 課金率)"
NON_BINARY_METRIC_TEXT = "非二値メトリクス(ex. ユーザ一人当たり売上金額, 商品購入数)"

# metricのタイプを選択するためのドロップダウンをメインページに配置。
option = st.selectbox(
    METRIC_TYPE_QUESTION_TEXT,
    (BINARY_METRIC_TEXT, NON_BINARY_METRIC_TEXT),
)

if option == BINARY_METRIC_TEXT:
    binary_metric_page.display()
else:
    non_binary_metric_page.display()
