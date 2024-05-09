import streamlit as st
import pickle

model = pickle.load(open('C:/Users/amanj/Downloads/model (2).pkl','rb'))

# st.header('Similar Words')
#
# q1 = st.text_input('Enter word')
# # q2 = st.text_input('Enter question 2')
# result=[]
# if st.button('Find'):
#     result = model.most_similar(q1)
#
# for i in range(0, len(result)):
#     st.header(result[i][0])

input_data = 'man'


result = model.most_similar(input_data)

for i in range(0, len(result)):
    print(result[i][0])


