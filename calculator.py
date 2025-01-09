# import math
# a =int(input("enter the first number :"))
# b= int(input("enter the second number")
# )
# opt = str(input("\nenter the oprator"))
# print("first number:",a)
# print("second number:",b)
# print("oprator:",opt)

# if opt == '+':
#     print(a+b)
    
# elif opt == '-':
#     print(a-b)
    
# elif opt== '*':
#     print(a*b)
    
# elif opt== '/':
#     print(a/b)
    
# else:
#     print("oprator invalid")




import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the numbers
a = st.number_input("Enter the first number", format="%d", step=1)
b = st.number_input("Enter the second number", format="%d", step=1)

# Input field for the operator
opt = st.selectbox("Select an operator", ['+', '-', '*', '/'])

# Calculate the result
if st.button("Calculate"):
    st.write("### Inputs:")
    st.write(f"**First Number:** {a}")
    st.write(f"**Second Number:** {b}")
    st.write(f"**Operator:** {opt}")

    if opt == '+':
        result = a + b
        st.write(f"**Result:** {result}")
    elif opt == '-':
        result = a - b
        st.write(f"**Result:** {result}")
    elif opt == '*':
        result = a * b
        st.write(f"**Result:** {result}")
    elif opt == '/':
        if b != 0:
            result = a / b
            st.write(f"**Result:** {result}")
        else:
            st.error("Division by zero is not allowed.")
    else:
        st.error("Invalid operator.")
