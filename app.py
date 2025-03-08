

#importing all libraries
import streamlit as st


#header defining
st.header('Interactive literary characters ai')

#expander defining
with st.expander('Instruction how to use :smile:'):
    st.write('please upload your book through sidebar or use example books')

#placing divider
st.divider()

#sidebar
# sidebar uploader
upload=st.sidebar.file_uploader('upload file',type=['pdf','txt'])



#sidebar book example selectbox
book_list=['A Study in Scarlet',
           'The Sign of Four',
           'The Adventures of Sherlock Holmes',
           'The Memoirs of Sherlock Holmes',
           'The Return of Sherlock Holmes']


book_selection=st.sidebar.selectbox('select example book to see demo',book_list,index=0)

if book_selection:
    st.sidebar.success(f'{book_selection} is selected')


#sidebar model selectbox

selectbox_options=['Transformer']

selectbox_var=st.sidebar.selectbox('model selection ',selectbox_options,index=0)
if (selectbox_var=='RNN'):

    st.sidebar.success('78 percent accuracy')

if (selectbox_var=='Transformer'):
    st.sidebar.success('90 percent accuracy')



#main content
#placing prompt chat input
prompt=st.chat_input('Ask anything')
if prompt:
    st.write('prompt:')
    st.write(f'{prompt}')
