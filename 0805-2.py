#陣列運算工具
import numpy as np
#繪圖工具
import matplotlib.pyplot as plt
#網頁建立工具
import streamlit as st

value = st.slider("三角函式",min_value=0,max_value=5)
t = np.arange(0.,5,0.05)
y1 = np.sin(np.random.randn() * value * np.pi * t)
y2 = np.cos(np.random.randn()* value * np.pi * t)

figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
st.write(figure1)
st.write(y1)
st.write(y2)
#終端機執行 streamlit run 0805-2.py，資料顯示在網頁上