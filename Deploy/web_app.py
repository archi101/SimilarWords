import streamlit as st
import pickle

model = pickle.load(open('C:/Users/amanj/Downloads/model (2).pkl','rb'))

def find_similar(input_data):
    result = model.most_similar(input_data)
    return result

def main():
    st.title('Similar Words')

    input_data=st.text_input('Enter the word')

    result = []
    if st.button('Find'):
        result=find_similar(input_data)
        for i in range(0, len(result)):
            st.text(result[i][0])  # Use st.text() instead of print()

    # st.success(result)

if __name__ == '__main__':  # Corrected from '_main_'
    main()
