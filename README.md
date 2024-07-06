# Real Estate Price Prediction

This project aims to predict the prices of houses and flats using data collected from 99acres.com. The dataset contains around 4000 samples of properties from Gurgaon. The project involves data processing, feature engineering, exploratory data analysis (EDA), outlier detection, model training, and deployment on Streamlit.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Processing and Cleaning](#data-processing-and-cleaning)
- [Feature Engineering](#feature-engineering)
- [Exploratory Data Analysis](#exploratory-data-analysis)
  - [Univariate Analysis](#univariate-analysis)
  - [Multivariate Analysis](#multivariate-analysis)
- [Outlier Detection and Removal](#outlier-detection-and-removal)
- [Missing Value Imputation](#missing-value-imputation)
- [Feature Selection](#feature-selection)
- [Model Training and Selection](#model-training-and-selection)
- [Deployment](#deployment)
- [How to Run](#how-to-run)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The main objective of this project is to develop a machine learning model that can accurately predict the prices of real estate properties in Gurgaon. The project includes data processing, feature engineering, exploratory data analysis, outlier detection, model training, and deployment.

## Data Processing and Cleaning
1. **Loading the Data**: Import the dataset and check for initial anomalies.
2. **Data Cleaning**: Remove duplicates, handle incorrect data types, and standardize categorical variables.
3. **Data Normalization**: Normalize numerical features to ensure all features contribute equally to the model.

## Feature Engineering
1. **Feature Creation**: Create new features based on domain knowledge (e.g., price per square foot, age of the property).
2. **Feature Transformation**: Apply transformations to skewed features to normalize their distribution.

## Exploratory Data Analysis
### Univariate Analysis
1. **Distribution Plots**: histograms and density plots for numerical features.
2. **Box Plots**: Visualising the spread and identify outliers in numerical features.

### Multivariate Analysis
1. **Correlation Matrix**: Examining the relationships between numerical features.
2. **Pair Plots**: Visualizing relationships between pairs of numerical features.

## Outlier Detection and Removal
1. **Identifying Outliers**: Used statistical methods like IQR to detect outliers.
2. **Removing Outliers**

## Missing Value Imputation
1. **Identifying Missing Values**: Check for missing values in the dataset.
2. **Imputation Techniques**: Apply appropriate techniques (mean, median, mode, or model-based imputation) to fill missing values.

## Feature Selection
1. **Feature Importance**: Use algorithms like Random Forest or Lasso Regression to identify important features.
2. **Dimensionality Reduction**: Apply techniques like PCA if needed to reduce the feature space.

## Model Training and Selection
1. **Train-Test Split**: Split the data into training and testing sets.
2. **Model Selection**: Experiment with various algorithms (e.g., Linear Regression, Random Forest, XGBoost) and select the best model based on performance metrics.

## Deployment
1. **Model Serialization**: Save the trained model using joblib or pickle.
2. **Streamlit Application**: Develop a user-friendly interface using Streamlit for model deployment.

## How to Run
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/real-estate-price-prediction.git
    ```
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

## Results
- **Model Performance**: Random Forest Model performed the best with r2 score of 90% and MAE of 47 lacs

## Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
