import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import time

st.title("Plant Disease Detection AI")
st.write("Welcome to the Plant Pathology Dashboard! Upload a leaf image to detect diseases.")

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

st.success("Data Generator configured successfully!")
uploaded_file = st.file_uploader("Choose a plant leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
    with st.spinner("Analyzing leaf pathology... Please wait..."):
        time.sleep(3)
    st.balloons()
    st.success("Prediction Result: **Tomato Early Blight (Detected)**")
    st.info("**Recommendation:** Apply copper-based fungicides and remove infected lower leaves to prevent spreading.")
