import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

model_file = 'rf_model.joblib'
model = joblib.load(model_file)

mappings = {
    'manufacturer': {'ford': 0, 'honda': 1, 'dodge': 2, 'chrysler': 3, 'toyota': 4, 'chevrolet': 5, 'jeep': 6, 'lexus': 7, 'bmw': 8, 'gmc': 9, 'mercedes-benz': 10, 'mazda': 11, 'rover': 12, 'ram': 13, 'nissan': 14, 'ferrari': 15, 'audi': 16, 'mitsubishi': 17, 'infiniti': 18, 'volkswagen': 19, 'kia': 20, 'hyundai': 21, 'fiat': 22, 'acura': 23, 'cadillac': 24, 'lincoln': 25, 'jaguar': 26, 'saturn': 27, 'volvo': 28, 'alfa-romeo': 29, 'buick': 30, 'subaru': 31, 'mini': 32, 'pontiac': 33, 'porsche': 34, 'harley-davidson': 35, 'tesla': 36, 'mercury': 37, 'datsun': 38, 'land rover': 39, 'aston-martin': 40},
    'condition': {'excellent': 0, 'good': 1, 'like new': 2, 'new': 3, 'fair': 4, 'salvage': 5},
    'cylinders': {'6 cylinders': 0, '8 cylinders': 1, '4 cylinders': 2, '5 cylinders': 3, '10 cylinders': 4, '3 cylinders': 5, 'other': 6, '12 cylinders': 7},
    'fuel': {'gas': 0, 'diesel': 1, 'hybrid': 2, 'electric': 3, 'other': 4},
    'transmission': {'automatic': 0, 'manual': 1, 'other': 2},
    'drive': {'rwd': 0, '4wd': 1, 'fwd': 2},
    'size': {'full-size': 0, 'mid-size': 1, 'compact': 2, 'sub-compact': 3},
    'type': {'truck': 0, 'pickup': 1, 'mini-van': 2, 'sedan': 3, 'offroad': 4, 'van': 5, 'SUV': 6, 'convertible': 7, 'coupe': 8, 'hatchback': 9, 'wagon': 10, 'other': 11, 'bus': 12},
    'paint_color': {'black': 0, 'blue': 1, 'silver': 2, 'white': 3, 'grey': 4, 'yellow': 5, 'red': 6, 'green': 7, 'brown': 8, 'custom': 9, 'purple': 10, 'orange': 11},
    'state': {'al': 0, 'ak': 1, 'az': 2, 'ar': 3, 'ca': 4, 'co': 5, 'ct': 6, 'dc': 7, 'de': 8, 'fl': 9, 'ga': 10, 'hi': 11, 'id': 12, 'il': 13, 'in': 14, 'ia': 15, 'ks': 16, 'ky': 17, 'la': 18, 'me': 19, 'md': 20, 'ma': 21, 'mi': 22, 'mn': 23, 'ms': 24, 'mo': 25, 'mt': 26, 'nc': 27, 'ne': 28, 'nv': 29, 'nj': 30, 'nm': 31, 'ny': 32, 'nh': 33, 'nd': 34, 'oh': 35, 'ok': 36, 'or': 37, 'pa': 38, 'ri': 39, 'sc': 40, 'sd': 41, 'tn': 42, 'tx': 43, 'ut': 44, 'vt': 45, 'va': 46, 'wa': 47, 'wv': 48, 'wi': 49, 'wy': 50}
}

# Define the home page content
def home_page():
    st.title("Welcome to the Used Car Price Prediction App")
    
    st.write("""
    This app is designed to help you predict the price of used cars based on machine learning models.
    Whether you're planning to buy or sell a used car, our app can provide valuable insights.
    """)
    
    st.image("car_image.jpeg", caption="Car Image", use_column_width=True)
    
    st.write("""
    **Key Features:**
    - Accurate price predictions
    - User-friendly interface
    - Visualizations for better understanding
    """)

    # Call-to-Action Button
    if st.button("Get Started"):
        st.sidebar.selectbox("Select a page", ["Prediction"])

# Define the prediction page content
def prediction_page():
    html_temp="""
     <div style = "background-color:cyan;padding:16px">
     <h2 style="color:black;text-align:center;">Used Car Price Prediction</h2>
     </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
   
    st.markdown("##### Are you planning to buy a used car !?\n##### So let's try evaluating the price..")
    
    st.write('')
    st.write('')
    s1 = st.selectbox('What is the manufacturer of the car ?', list(mappings['manufacturer'].keys()))
    p1 = mappings['manufacturer'][s1]
    
    s2 = st.selectbox('What is the condition of the car ?', list(mappings['condition'].keys()))
    p2 = mappings['condition'][s2]
    
    s3 = st.selectbox('What is the number of cylinders in the car ?', list(mappings['cylinders'].keys()))
    p3 = mappings['cylinders'][s3]
    
    s4 = st.selectbox('What is the fuel type of the car ?', list(mappings['fuel'].keys()))
    p4 = mappings['fuel'][s4]

    # New input element for odometer reading
    p5 = st.slider('What is the odometer reading of the car?(Multiple of 5k)', 0.1, 50.0, step=0.1)   
    
    s5 = st.selectbox('What is the Transmission Type ?', list(mappings['transmission'].keys()))
    p6 = mappings['transmission'][s5]
    
    s6 = st.selectbox('What is the drive type of the car ?', list(mappings['drive'].keys()))
    p7 = mappings['drive'][s6]
    
    s7 = st.selectbox('What is the size of the car ?', list(mappings['size'].keys()))
    p8 = mappings['size'][s7]
    
    s8 = st.selectbox('What is the type of the car ?', list(mappings['type'].keys()))
    p9 = mappings['type'][s8]
    
    s9 = st.selectbox('What is the paint color of the car ?', list(mappings['paint_color'].keys()))
    p10 = mappings['paint_color'][s9]
    
    s10 = st.selectbox('What is the state of the car ?', list(mappings['state'].keys()))
    p11 = mappings['state'][s10]

    # Use the existing column for the age of the car
    p12 = st.number_input('What is the age of the car?', min_value=1, max_value=30, value=5, step=1)
    
    data_new = pd.DataFrame({
    'Manufacturer':p1,
    'Condition':p2,
    'Cylinders':p3,
    'Fuel_Type':p4,
    'Odometer':p5,
    'Transmission':p6,
    'Drive':p7,
    'Size':p8,
    'Type':p9,
    'Paint_Color':p10,
    'State':p11,
    'Age_of_Car':p12
},index=[0])
    try: 
        if st.button('Predict'):
            prediction = model.predict(data_new)
            if prediction>0:
                st.balloons()
                st.success('You can buy the car for {:.2f} Dollars'.format(prediction[0]))
            else:
                st.warning("You will be not able to sell this car !!")
    except:
        st.warning("Opps!! Something went wrong\nTry again")

# Define the about page content
def about_page():
    st.title("About Me")
    
    st.write("""
    Welcome to the About Me page! I'm passionate about making the process of buying and selling used cars easier.
    Here's a bit more about my journey behind this app.
    """)

    # Developer Information
    st.header("Meet me")
    st.image("vikas_photo.jpg",  use_column_width=True)
    

    # App Development Story
    st.header("App Development Story")
    st.write("""
    The journey of developing our used car price prediction application began with the meticulous collection of a diverse and extensive dataset encompassing various features such as
    manufacturer, condition, cylinders, fuel type, and more. This dataset served as the foundation for our project, offering a comprehensive snapshot of the used car market.To ensure
    the robustness of our models, a rigorous data cleaning process was implemented. This involved handling missing values, encoding categorical variables, and narrowing the
    odometer range to focus on the most relevant data points, laying the groundwork for accurate predictions.

    Once the data was prepared, we embarked on a thorough analysis with the aid of visualizations.This exploratory phase unveiled insights into the distribution of car prices,
    the influence of different features, and potential correlations. Visualizations, including scatter plots, histograms, and correlation matrices, played a pivotal role in
    comprehending the dataset's nuances and informed subsequent modeling decisions.

    The heart of our application lies in the trained machine learning models, with the Random Forest Regressor emerging as the primary predictive tool.The training phase involved
    splitting the dataset into training and testing sets, fine-tuning hyperparameters, and ensuring the models could generalize well to new data. Evaluation metrics such as
    Mean Absolute Error and R2 Score guided the optimization process, ensuring that our models exhibited robust performance.

    The culmination of these efforts led to the creation of an interactive and user-friendly web application using Streamlit. The application provides a seamless interface for
    users to input specific details about a used car, initiating a dynamic analysis that predicts the estimated price. The integration of Streamlit streamlines the deployment of
    complex machine learning models, making the technology accessible to a broader audience.

    In essence, our app development story is a narrative of meticulous data curation, insightful data analysis, and the seamless fusion of machine learning into a user-friendly
    application. This holistic approach ensures that our predictive tool not only leverages the power of data science but also serves as a practical and transparent solution
    for navigating the intricacies of the used car market.
    """)

    # Visual Timeline
    st.header("Development Timeline")

    st.write("""
    - **Started Development:** September 2023
    - **Model Training:** October 2023
    - **App Launch:** November 2023
    """)

    # Contact Information
    st.header("Contact Us")
    st.write("""
    We value your feedback! Feel free to contact us through the following channels:
    - Email: vikasn1@umbc.edu
    - Linkedin: [@CarPredictionApp](https://www.linkedin.com/in/vikasreddynagulapelly)
    """)

    # Acknowledgments
    st.header("Acknowledgments")
    st.write("""
    We would like to express our gratitude to the following:
    - Professor - Dr. Chaojie (Jay) Wang
    - [Car Dataset](https://www.craigslist.org/)
    - Streamlit for providing a fantastic platform
    """)

    # Interactive Elements
    st.header("Stay Connected")
    st.write("""
    Stay connected with us for updates and additional resources:
    - [Blog](https://blog.carpredictionapp.com)
    - [YouTube](https://www.youtube.com/c/CarPredictionApp)
    """)
    
    # Call-to-Action Button
    if st.button("Back to Home"):
        st.sidebar.selectbox("Select a page", ["Home"])
        
# Create a sidebar for navigation
selected_page = st.sidebar.selectbox("Select a page", ["Home", "Prediction", "About"])

# Display the selected page
if selected_page == "Home":
    home_page()
elif selected_page == "Prediction":
    prediction_page()
elif selected_page == "About":
    about_page()
