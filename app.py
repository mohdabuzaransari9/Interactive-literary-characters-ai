#importing all libraries
import streamlit as st


#header defining
st.header('Ai Literary Chatbot')

#expander defining
with st.expander('Instruction how to use :smile:'):
    st.write('please upload your book through sidebar or use example books')

#placing divider
st.divider()

#sidebar
# sidebar uploader
upload=st.sidebar.file_uploader('upload file',type=['pdf','txt'])


#sidebar book example selectbox
book_list=['The Adventures of Sherlock Holmes']
book_selection=st.sidebar.selectbox('select example book to see demo',book_list,index=0)

#sidebar model selectbox

selectbox_options=['RNN','transformer']

selectbox_var=st.sidebar.selectbox('model selection ',selectbox_options,index=1)
if selectbox_var:

    st.sidebar.success('90 percent accuracy')

#main content
#placing prompt chat input
prompt=st.chat_input('Ask anything')
if prompt:
    st.write('user prompt:')
    st.write(f'{prompt}')




