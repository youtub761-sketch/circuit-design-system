import streamlit as st
import circuit_generator  # 匯入你的繪圖模組

# 1. 介面設定
st.set_page_config(page_title="數位邏輯電路設計系統")
st.title("數位邏輯電路設計系統")
st.markdown("### 期末專題：Sequential Circuit Design System")
st.write("**學生姓名：** 林柏翰 | **學號：** 1120546") # 題目要求 (c)

# 2. 方程式輸入區
st.sidebar.header("請輸入邏輯方程式")
eqs = {
    'J1': st.sidebar.text_input("J1 方程式", "Q0 & X"),
    'K1': st.sidebar.text_input("K1 方程式", "Q0 | ~X"),
    'J0': st.sidebar.text_input("J0 方程式", "Q1 & X"),
    'K0': st.sidebar.text_input("K0 方程式", "X")
}

# 3. 繪圖觸發
if st.button("計算並產生電路圖"):
    with st.spinner('正在繪製電路圖...'):
        try:
            d = circuit_generator.get_circuit_drawing(eqs)
            st.pyplot(d.draw())
            st.success("繪圖成功！")
        except Exception as e:
            st.error(f"繪圖發生錯誤: {e}")
