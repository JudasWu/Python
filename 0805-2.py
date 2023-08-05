#陣列運算工具
import numpy as np
#繪圖工具
import matplotlib.pyplot as plt
#網頁建立工具
import streamlit as st

t = np.arange(0.,1.0,0.05)
st.write(t)
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
st.write(y1)
st.write(y2)
figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
st.write(figure1)
#終端機執行 streamlit run 0805-2.py，資料顯示在網頁上