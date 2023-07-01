import numpy as np 
import streamlit as st
import base64

def model1(x):
    x = np.array(x)
    coeff = np.array([-5.449e-06, 0.0044, 0.0133, -0.0489, -0.0569, 0.3272])
    y = 11.3940+(np.sum(np.multiply(x, coeff)))
    return round(np.exp(y),0)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('cars.png')


def run():
    luxury = 0
    st.title('Used Car Price Estimator ')
    st.write('BY- Karthik Raja B,Pragadishwaran K,Karthikeyan')
    #st.sidebar.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
    #from PIL import Image
    #image = Image.open('sunrise.jpg')
    #st.image(image, caption='Sunrise by the mountains',
    # use_column_width=True)
    mileage = st.slider('Max Mileage', 0, 80000, 0, 20)
    city_mpg = st.slider('City MPG', 11, 54, 11, 1)
    highway_mpg = st.slider('Highway MPG', 16, 50, 16, 1)
    year = st.slider('Model Year', 2014, 2020, 2014, 1)
    lux = st.checkbox('Luxury')
    st.markdown('<style>h1{color: magenta;}</style>', unsafe_allow_html=True)
   
   

    if lux:
        luxury = 1
    x = [mileage, city_mpg, highway_mpg, year, luxury]
    x.insert(1, 'replace me!')
    x[0] = int(x[0])
    x[1] = 1 if x[0] <= 7500 else 0
    x[2] = int(x[2])
    x[3] = int(x[3])
    x[4] = 2020 - int(x[4])
    x[5] = int(x[5])
    st.success('This is a success message!')
    st.write('Your Car is worth Approximately')
    st.write(model1(x))

if __name__ == '__main__':
    run()

