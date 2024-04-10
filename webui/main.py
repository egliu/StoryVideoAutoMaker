import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 页面标题与介绍文本
st.set_page_config(page_title="Streamlit Demo App", layout="wide")
st.title("Streamlit 演示应用")
st.write("这是一个使用 Streamlit 库创建的简单交互式数据可视化应用。")

# 2. 用户输入框
st.header("用户输入")
num_samples = st.slider(
    "选择数据样本数量：",
    min_value=10,
    max_value=100,
    value=50,
    step=10,
    help="调整滑块以改变生成的数据样本数量。",
)

# 3. 数据表格展示
st.subheader("随机生成数据表格")
data = {
    "Category": np.random.choice(["A", "B", "C"], num_samples),
    "Value": np.random.normal(0, 1, num_samples),
}
df = pd.DataFrame(data)
st.dataframe(df)

# 4. 可视化图表（柱状图）
st.subheader("柱状图展示")
category_counts = df["Category"].value_counts().sort_index()
plt.figure(figsize=(8, 4))
plt.bar(category_counts.index, category_counts.values)
st.pyplot()