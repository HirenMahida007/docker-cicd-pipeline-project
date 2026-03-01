import streamlit as st


def add(a: float, b: float) -> float:
    return a + b


st.set_page_config(page_title="CI/CD Demo App", page_icon=":rocket:", layout="centered")

st.title("CI/CD Pipeline Demo")
st.caption("Python + Streamlit frontend for your Node.js demo project")

st.subheader("Calculator Demo")
st.write("This reproduces your app's core logic: `add(a, b)`.")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("First number", value=2.0, step=1.0)
with col2:
    b = st.number_input("Second number", value=3.0, step=1.0)

result = add(a, b)
st.success(f"Result: {result}")

st.divider()
st.subheader("Status")
st.markdown("- Node app message: `App is running inside Docker`")
st.markdown("- CI test expectation: `add(2, 3) == 5`")
