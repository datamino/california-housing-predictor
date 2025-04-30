
# 🏠 California Housing Price Prediction

A complete end-to-end Machine Learning project that predicts housing prices in California using multiple regression models. The project includes Exploratory Data Analysis (EDA), preprocessing, model training (Linear, Ridge, Lasso, Random Forest, XGBoost), evaluation using MAE, RMSE, R², and a production-ready deployment using Flask.

---

## 📌 Table of Contents

- [🔍 Project Overview](#-project-overview)
- [📁 Directory Structure](#-directory-structure)
- [🧠 ML Workflow](#-ml-workflow)
- [📊 Model Evaluation](#-model-evaluation)
- [🚀 Deployment (Flask API)](#-deployment-flask-api)
- [⚙️ Setup Instructions](#-setup-instructions)
- [👨‍💻 Author](#-author)

---

## 🔍 Project Overview

- **Dataset**: Modified California Housing dataset (`housing.csv`)
- **Goal**: Predict `median_house_value` using features like rooms, population, income, etc.
- **Pipeline**:
  - Univariate & Bivariate EDA
  - Outlier Handling
  - Feature Preprocessing (scaling, encoding)
  - Regression Models: `Linear`, `Ridge`, `Lasso`, `Random Forest`, `XGBoost`
  - Performance comparison via `MAE`, `RMSE`, `R²`
- **Deployment**: Flask API for real-time price prediction

---

## 📁 Directory Structure

```
project-root/
│
├── data/                     # Contains housing.csv
│   └── housing.csv
│
├── models/                   # Trained .pkl model (small < 100MB)
│   └── house_price_predictor.pkl
│
├── src/                      # Notebook or scripts for EDA, modeling
│   └── notebook.ipynb
│
├── templates/                # HTML templates (Flask)
│   └── index.html
│
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
└── README.md                 # This documentation
```

---

## 🧠 ML Workflow

1. **EDA**
   - Visualized distributions, correlations, relationships
   - Detected skewed data and outliers

2. **Preprocessing**
   - Handled missing values
   - Applied scaling, one-hot encoding
   - Avoided log-transform due to cleaned data

3. **Modeling**
   - Trained and compared multiple regressors
   - Stored metrics in a Pandas DataFrame
   - Chose best model based on lowest RMSE

4. **Deployment**
   - Exported trained pipeline via `joblib`
   - Created `app.py` using Flask
   - Predicts house price from user input (via JSON or HTML form)

---

## 📊 Model Evaluation Summary

| Model          | MAE     | RMSE     | R²     |
|----------------|---------|----------|--------|
| Linear         | 49,534       | 68,174        | 0.6647     |
| Ridge          | 49,536       | 68,175       | 0.6647      |
| Lasso          | 49,534       | 68,174        | 0.6647      |
| Xgboost        | 35,405      | 51,962       | 0.8052      |
| **Random Forest**| 31,957 | 49,487  | 0.8233 |



---

## 🚀 Deployment (Flask API)

### 🖥️ Run Locally

```bash
git clone https://github.com/datamino/california-housing-predictor
cd california-housing-predictor
pip install -r requirements.txt
python app.py
```

Then open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 🧪 API Endpoint

- URL: `/predict`
- Method: `POST`
- Input: JSON with house features
- Output: Predicted price

```json
{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "ocean_proximity": "<1H OCEAN"
}
```

---

## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/datamino/california-housing-predictor
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run app:
   ```bash
   python app.py
   ```

---

## 👨‍💻 Author

**Muhammad Tayyab**  
BS Artificial Intelligence  
FAST-NUCES (Peshawar Campus)  
📧 `p229279@pwr.nu.edu.pk`  
🌐 GitHub: [@datamino](https://github.com/datamino)

---


> _Built with ❤️ and Python for real-world ML deployment._
