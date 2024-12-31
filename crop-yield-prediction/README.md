# Crop-Yield Prediction

## Overview
This project aims to predict crop yields using machine learning techniques. Accurate crop yield predictions can help farmers make informed decisions about planting, irrigation, and harvesting, ultimately improving agricultural productivity and sustainability.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crop-yield-prediction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd crop-yield-prediction
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Model Metrics
- **Mean Squared Error (MSE):** 0.0816
- **R2 Score:** 0.999996

## Detailed Description
The Crop-Yield Prediction project involves several steps including data preprocessing, feature engineering, model training, and evaluation. The dataset used contains various features such as rainfall, soil quality index, farm size, sunlight hours, and fertilizer used. These features are used to predict the crop yield.

### Data Preprocessing
The data is first cleaned and preprocessed to handle any missing values and outliers. The features are then scaled using StandardScaler to ensure that they are on the same scale.

### Feature Engineering
Feature engineering involves creating new features or modifying existing ones to improve the performance of the model. In this project, the features are selected based on their correlation with the target variable, crop yield.

### Model Training
Several machine learning models are trained and evaluated to find the best performing model. The models used include:
- **Linear Regression**
- **Lasso Regression**
- **Ridge Regression**
- **K-Nearest Neighbors (KNN)**
- **Support Vector Machine (SVM)**
- **Decision Tree Regressor**
- **Random Forest Regressor**

### Model Evaluation
The models are evaluated using metrics such as Mean Squared Error (MSE) and R2 Score. The best performing model is selected based on these metrics. In this project, the Ridge Regression model with an alpha value of 0.1 was found to be the best performing model.

### Flask Web Application
A Flask web application is created to provide a user interface for making predictions. The user can input the values for the features, and the application will return the predicted crop yield.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
