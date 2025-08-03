import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Hello Streamlit!")
st.write("これはテストアプリです。")
st.write("これは簡単なアプリです。")

# タイトル
st.title("サンプルグラフ - 折れ線グラフ")

# サンプルデータ（DataFrame）
data = {
    "日付": pd.date_range("2025-08-01", periods=7, freq='D'),
    "売上": [120, 150, 170, 130, 180, 200, 210]
}
df = pd.DataFrame(data)

# 表の表示
st.write("📅 売上データ")
st.dataframe(df)

# 折れ線グラフの表示
fig, ax = plt.subplots()
ax.plot(df["日付"], df["売上"], marker='o')
ax.set_title("日別売上")
ax.set_xlabel("日付")
ax.set_ylabel("売上")
plt.xticks(rotation=45)
st.pyplot(fig)