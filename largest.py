import streamlit as st
st.title('Web App to find largest among three numbers')
st.header('Enter your input here')
first_number = st.number_input('Enter First Number')
second_number = st.number_input('Enter Second Number')
third_number = st.number_input('Enter Third Number')

def find_largest_num(first_number,second_number,third_number):
  max = 0
  list = [first_number,second_number,third_number]
  max += max(list)
  return max

st.write(" This number is largest:" , find_largest_num(first_number, second_number,third_number))
  
