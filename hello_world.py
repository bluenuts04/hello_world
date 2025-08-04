import streamlit as st
import pandas as pd

st.title("Hello Streamlit!")
st.write("これはテストアプリです。")
st.write("これは簡単なアプリです。")

# タイトル
st.title("サンプルグラフ - 折れ線グラフ")

import streamlit as st
import pandas as pd

# セッション状態を初期化
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["日付", "項目", "金額"])
    st.session_state.clear_data = False  # クリアフラグを初期化

# Streamlitアプリケーションのタイトル
st.title("家計簿アプリ")

# 収支データの入力フォーム
st.header("収支の記録")
date = st.date_input("日付", pd.to_datetime("today"))
item = st.text_input("項目")
amount = st.number_input("金額", value=0, step=1)  # 金額を整数として入力

# データをデータフレームに追加
if st.button("記録する"):
    st.session_state.data = st.session_state.data.append({"日付": date, "項目": item, "金額": int(amount)}, ignore_index=True)

# 収支データの表示
st.header("収支データ")
st.write(st.session_state.data)

# 統計情報の表示
st.header("統計情報")
st.write("合計支出:", st.session_state.data[st.session_state.data["金額"] < 0]["金額"].sum())
st.write("合計収入:", st.session_state.data[st.session_state.data["金額"] > 0]["金額"].sum())

# アプリのクリアボタン
if st.button("データをクリア"):
    st.session_state.data = pd.DataFrame(columns=["日付", "項目", "金額"])
    st.session_state.clear_data = True  # クリアフラグをTrueに設定
    st.success("データがクリアされました。")

# データがクリアされた場合、初期画面を表示
if st.session_state.clear_data:
    st.session_state.clear_data = False
    st.experimental_rerun()  # アプリを再実行して初期画面を表示

# データの保存
st.session_state.data.to_csv("家計簿データ.csv", index=False)


