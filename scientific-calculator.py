import streamlit as st
import math

# Streamlit UI setup
st.title("Charming Scientific Calculator")

# Input display for the calculator
if 'expression' not in st.session_state:
    st.session_state.expression = ""

expression = st.session_state.expression

# Buttons layout
button_labels = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sin', 'cos', 'tan', 'log'],
    ['(', ')', 'C', 'sqrt'],
]

# Function to evaluate mathematical expressions
def evaluate_expression(expr):
    try:
        # Replace common math functions with Python's math module functions
        expr = expr.replace('sin', 'math.sin')
        expr = expr.replace('cos', 'math.cos')
        expr = expr.replace('tan', 'math.tan')
        expr = expr.replace('log', 'math.log')
        expr = expr.replace('sqrt', 'math.sqrt')
        expr = expr.replace('pi', 'math.pi')
        
        result = eval(expr)
        return result
    except Exception as e:
        return "Error"

# Function to handle button clicks
def button_click(label):
    if label == "=":
        st.session_state.expression = str(evaluate_expression(st.session_state.expression))
    elif label == "C":
        st.session_state.expression = ""
    else:
        st.session_state.expression += label

# Display buttons and capture clicks
for row in button_labels:
    columns = st.columns(4)
    for i, label in enumerate(row):
        if columns[i].button(label):
            button_click(label)
            st.experimental_rerun()  # Rerun the app to update the UI

# Display the current expression
st.text_input("Expression", value=st.session_state.expression, key="expression_display", disabled=True)
