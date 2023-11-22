import streamlit as st

def main():
    st.title('Data Science')

    col1, col2 = st.columns(2)

    with col1:
        st.image('Data_Science.png')

    with col2:
        st.write("""Data science is an essential part of many industries today, given the massive amounts of data 
                   that are produced. It's one of the most debated topics in IT circles. Its popularity has grown over the years, 
                   and companies have started implementing data science techniques to grow their business and increase customer satisfaction.""")
