import streamlit as st
import pandas as pd

def main():
    st.title("Interactive Dashboard")
    st.write("This is a simple interactive dashboard created with Streamlit.")

    # Load sample data
    data = pd.DataFrame({
        'x': [1, 2, 3, 4],
        'y': [10, 20, 30, 40]
    })

    # Create a line chart
    st.line_chart(data)

    # Create a selectbox to choose the data column to display
    column = st.selectbox('Select a column to display', ['x', 'y'])

    # Display the selected column data
    st.write('You selected:', column)
    st.write('Data:', data[column])

if __name__ == '__main__':
    main()
