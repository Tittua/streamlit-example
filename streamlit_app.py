import streamlit as st
from PIL import Image
#from ultralytics import YOLO
import time

st.title('Aloe Vera Plant Disease Analyser')

col1,col2=st.columns(2)
upload_stat=0
with col1:
    
    input_image=st.file_uploader('Upload The Image File Here',type=['jpg','png'])
    
    confirmation=st.button('Submit')
    if confirmation==True:
        st.image(input_image)
        upload_stat=1
        
with col2:
    st.subheader('Detection:')
    
        
