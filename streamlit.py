import numpy as np
import streamlit as st

def calculate_range(data):
    min_val = np.min(data)
    max_val = np.max(data)
    r_data = min_val-max_val
    return r_dtaa

def main():
    st.title('Range Generator')
    
    st.write('Enter the numbers seperated by commas to find the range of them')
    
    x_input = st.text_input('Numbers')
    
    if st.button('Generate Range'):
        X = np.array([float(x) for x in x_input.split(',')])
        data = calculate_range(X)
        st.write(f'The range of the set of numbers is {data}')
if __name__ == '__main__':
    main()
