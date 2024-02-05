#!/usr/bin/env python
# coding: utf-8

# # PENCIL SKETCH

# In[1]:


# pip install opencv-python


# In[1]:

pip install opencv-python
import cv2
import streamlit as st
import numpy as np

st.title('MAKE ANY IMAGE INTO PENCIL SKETCH')

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Read the image
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display original image
    st.image(rgb_image, caption='Original Image', use_column_width=True)

    # Convert to grayscale
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #st.image(grey_image, caption='Grayscale Image', use_column_width=True)

    # Invert the image
    inverted_image = 255 - grey_image
    #st.image(inverted_image, caption='Inverted Image', use_column_width=True)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred

    # Create pencil sketch
    pencil_sketch = cv2.divide(grey_image, inverted_blurred, scale=256.0)
    st.image(pencil_sketch, caption='Pencil Sketch', use_column_width=True)


# In[ ]:




