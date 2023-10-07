import requests
import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Bangalore House Price Prediction App", page_icon=":house:")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About"])

    if page == "Home":
        show_home()
    elif page == "About":
        show_about()


def show_home():
    st.title("Bangalore House Price Prediction App")

    total_sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1500)
    location = st.text_input("Location", value="Indira Nagar")
    bhk = st.number_input("BHK", min_value=1, max_value=5, value=3, step=1, format="%d")
    bath = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2, step=1, format="%d")

    if st.button("Predict Price"):
        estimated_price = predict_price(location, total_sqft, bhk, bath)
        estimated_price_display = format_price(abs(estimated_price))
        st.success(f"Estimated Price: {estimated_price_display}")

    st.markdown("## Instructions to Run the App")
    st.markdown("1. To run this app, download these files in your PC: [Download Files]("
                "https://drive.google.com/drive/folders/1frXr2-VZ9_HFOkIyuG1MRHMte6AmlzTl?usp=sharing)")

    st.markdown("2. Open the terminal and navigate to the downloaded folder.")

    st.markdown("3. Run the following command in the terminal:")
    st.code("python serv.py", language="python")


def format_price(price):
    if price > 100:
        return f"{price / 100:.2f} Crores INR"
    else:
        return f"{price} Lacks INR"


def show_about():
    st.title("About Bangalore House Price Prediction App")

    st.write(
        "Welcome to the Bangalore Price Prediction App! This app uses a Linear Regression model to predict house "
        "prices in Bangalore.")

    st.subheader("Model Information")
    st.write("The model used here is Linear Regression.")

    st.subheader("Dataset Information")
    st.write("The dataset used for training the model is the Bangalore house dataset.")

    st.subheader("Model Comparison")
    comparison_data = {
        'Model': ['Linear Regression', 'Lasso', 'Decision Tree'],
        'Best Score': ["81.90%", "68.74%", "71.58%"],
    }
    st.write(pd.DataFrame(comparison_data).set_index('Model'))


def predict_price(location, total_sqft, bhk, bath):
    payload = {
        'total_sqft': total_sqft,
        'location': location,
        'bhk': bhk,
        'bath': bath
    }

    response = requests.post("http://127.0.0.1:5000/predict_home_price", data=payload)
    data = response.json()
    return data['estimated_price']


if __name__ == '__main__':
    main()
