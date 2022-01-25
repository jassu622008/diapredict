import pandas as pd

import streamlit as st

from sklearn import linear_model

def main():
    try:
        df = pd.read_csv('diabetes.csv')
        Glucose = st.text_input('Enter Blood Glucose Level: ')
        Age = st.text_input('Enter Your Age: ')

        pre = linear_model.LinearRegression()

        pre.fit(df[['Glucose', 'Insulin', 'Age']], df.Outcome)

        res = float(pre.predict([[Glucose,Age]]))

        if float(res) <= 0.0:
            st.title("It's Party Time,you doesn't have diabetes")

        if float(res) >= 1.0:
            st.title("Don't Worry You Have diabetes It Can Be cured or removed from you body by medicines")

    except ValueError:
        st.write('Please Enter Something Only Numbers')

st.write(main())
