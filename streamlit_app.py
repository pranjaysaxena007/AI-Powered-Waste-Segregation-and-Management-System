import streamlit as st
import tensorflow as tf
import numpy as np

def model_prediction(test_image):
  model = tf.keras.models.load_model("garbage_classification_model.keras")
  image = tf.keras.preprocessing.image.load_img(test_image,target_size=(224,224))
  input_arr = tf.keras.preprocessing.image.img_to_array(image)
  predictions = model.predict(input_arr)
  return np.argmax(predictions)  #returns index of maximum element

#SIDEBAR
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",['Home','About','Waste Segregation'])

#HOME PAGE
if(app_mode =='Home'):
  st.header('EcoSmart: AI-Based Waste Segregation and Management Solution')
  image_path ='hpimg.jpeg'
  st.image(image_path,use_column_width=True)
  st.markdown("""<div style="text-align: justify";>
AI-Driven Waste Segregation: Revolutionizing Waste Management

In today's world, effective waste management is crucial for maintaining a sustainable environment. Our **AI-Powered Waste Segregation and Management System** is designed to address this challenge by integrating cutting-edge Deep Learning technologies to automate waste sorting and streamline recycling processes.

The system uses a robust Deep Learning classification model that can accurately identify and segregate different types of waste, such as plastics, metals, glass, and organic material. By reducing human error and speeding up the sorting process, our AI-driven solution significantly enhances the efficiency of waste processing facilities and promotes more sustainable practices.

Key Features:
- **Accurate Waste Classification:** Our Deep Learning model is trained on a vast dataset to identify various types of waste with high precision.
- **Real-Time Segregation:** The system processes images of waste in real-time, ensuring quick and efficient segregation, reducing manual sorting efforts.
- **Sustainability at the Core:** By automating waste sorting, we help reduce contamination in recycling processes, leading to higher recycling rates and less environmental impact.
- **Scalable and Adaptable:** The model is designed to be adaptable to different environments, whether it’s for household waste, industrial refuse, or large-scale municipal waste management.

With our AI-powered waste segregation system, we are taking a significant step toward smarter, greener, and more sustainable waste management. Join us in making a positive environmental impact through technology!
    </div>""", unsafe_allow_html=True
    )

#About Project
elif(app_mode == 'About'):
  st.header('About')
  st.markdown("""<div style="text-align: justify";>.
**About Dataset**.
This dataset has 15,150 images from 12 different classes of household garbage; paper, cardboard, biological, metal, plastic, green-glass, brown-glass, white-glass, clothes, shoes, batteries, and trash.

Garbage Recycling is a key aspect of preserving our environment. To make the recycling process possible/easier, the garbage must be sorted to groups that have similar recycling process. I found that most available data sets classify garbage into a few classes (2 to 6 classes at most). Having the ability to sort the household garbage into more classes can result in dramatically increasing the percentage of the recycled garbage.


####Content
An ideal setting for data collection would be to place a camera above a conveyor where the garbage comes one by one, so that the camera can capture real garbage images. But since such a setup is not feasible at the moment I collected most of the images in this dataset by web scraping, I tried to get images close to garbage images whenever possible, for example in biological garbage category I searched for rotten vegetables, rotten fruits and food remains, etc. However, for some classes such as clothes or shoes it was more difficult to get images of clothes or shoes from the garbage, so mostly it was images of normal clothes. Nevertheless, being able to classify the images of this data set to 12 classes can be a big step towards improving the recycling process.
</div>""", unsafe_allow_html=True)

elif(app_mode == 'Waste Segregation'):
  st.header('Waste Segregation')
  test_image = st.file_uploader('Choose an image:')
  #Show Image Button
  if(st.button('Show Image')):
    try:
      st.image(test_image,use_column_width=True)   
    except:
      print("Enter image to view")
  #Predict button
  if(st.button('Predict')):
    try:
      with st.spinner("Wait for it..."):
        st.markdown("""#### Our prediction""")
        result_index = model_prediction(test_image)
        # Define Class
        class_name = ['Battery','Biological','Brown-Glass','CardBoard','Clothes','Green-Glass','Metal','Paper','Plastic','Shoes','Trash','White-glass']
        st.success(f'''Model is Predicting it's a  ""{class_name[result_index]}"" ''')
        st.snow()
    except:
      st.write("Please INSERT an Image for Prediction")
  
