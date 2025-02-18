import streamlit as st

st.header('Ai Literary Chatbot')
with st.expander('Instruction how to use :smile:'):
    st.write('please upload your book through sidebar or use example books')
st.divider()
upload=st.sidebar.file_uploader('upload file',type=['pdf','txt'])
chat=st.chat_input("Ask anything")
book_list=['The Adventures of Sherlock Holmes']
book_selection=st.sidebar.selectbox('select example book to see demo',book_list,index=0)
selectbox_options=['RNN','tansformer']

selectbox_var=st.sidebar.selectbox('model selection ',selectbox_options,index=1)
if selectbox_var:

    st.sidebar.success('90 percent accuracy')


if chat:
    st.write(st.text_area())




