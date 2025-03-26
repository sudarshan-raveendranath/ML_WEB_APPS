# 🩺 Diabetes Prediction API - FastAPI

This repository contains a **Machine Learning-based Diabetes Prediction API** built using **FastAPI**. The model is trained on the **Pima Indians Diabetes Dataset** using an **SVM classifier** and deployed as a REST API for easy accessibility.

## 🚀 Features
- **Machine Learning Model** trained on real-world diabetes data.
- **FastAPI-powered REST API** for real-time predictions.
- **Pickle Serialization** for model storage and retrieval.
- **JSON-based API requests** for easy integration.
- **Testing script using `requests` library** for seamless API interaction.

## 📂 Project Structure
```
📂 diabetes-prediction-api
│── 📄 diabetes.csv                   # Dataset used for training
│── 📄 trained_model.sav              # Saved ML model (SVM)
│── 📄 ML_API.py                       # FastAPI-based API implementation
│── 📄 test_api.py                     # Python script to test the API
│── 📄 README.md                       # Project documentation
│── 📄 requirements.txt                 # Dependencies list
```

## 🛠️ Setup & Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/diabetes-prediction-api.git
cd diabetes-prediction-api
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## 📊 Model Training & Storage
The machine learning model is trained using **Support Vector Machine (SVM)**:
1. The dataset `diabetes.csv` is loaded using Pandas.
2. The features (`X`) and target (`Y`) are split.
3. The dataset is divided into training and test sets.
4. A **Support Vector Machine (SVM) model** is trained.
5. The model is **saved as `trained_model.sav`** using `pickle`.

## 🌍 Running the API
Start the FastAPI server using **Uvicorn**:
```sh
uvicorn ML_API:app --reload
```
By default, the API will be accessible at:  
🔗 **http://127.0.0.1:8000**

### 📜 API Endpoints

| HTTP Method | Endpoint | Description |
|------------|---------|-------------|
| `POST` | `/diabetes_prediction` | Predicts if a person has diabetes based on input data |

### 📝 Sample JSON Request
```json
{
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
}
```

### 🔍 Example API Response
```json
"The person is diabetic"
```

## 🛠️ Testing the API
Run the `test_api.py` script to send a test request to the API:
```sh
python test_api.py
```

## 📜 Full Code Implementation
### 📌 `ML_API.py` - FastAPI Implementation
```python
from fastapi import FastAPI
import pickle
import numpy as np
import json

app = FastAPI()

# Load the trained model
model_filename = "trained_model.sav"
with open(model_filename, "rb") as model_file:
    classifier = pickle.load(model_file)

@app.post("/diabetes_prediction")
def predict_diabetes(data: dict):
    try:
        features = np.array([[
            data["Pregnancies"], data["Glucose"], data["BloodPressure"],
            data["SkinThickness"], data["Insulin"], data["BMI"],
            data["DiabetesPedigreeFunction"], data["Age"]
        ]])
        
        prediction = classifier.predict(features)
        result = "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
        return json.dumps(result)
    
    except Exception as e:
        return json.dumps({"error": str(e)})
```

### 📌 `test_api.py` - Testing Script
```python
import requests
import json

url = "http://127.0.0.1:8000/diabetes_prediction"

data = {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
}

response = requests.post(url, json=data)
print("API Response:", response.json())
```

## 📌 Troubleshooting
### ⚠️ "ModuleNotFoundError: No module named 'ML_API'"
- Ensure you are in the correct directory before running `uvicorn ML_API:app --reload`.

### ⚠️ "AttributeError: module 'ML_API' has no attribute 'app'"
- Verify that `ML_API.py` contains:
  ```python
  app = FastAPI()
  ```

### ⚠️ "UserWarning: X does not have valid feature names"
- Ensure the model is trained with **the same feature names** as the API input.

## 📜 License
This project is licensed under the **MIT License**.

## 🙌 Contributing
Feel free to open issues and submit pull requests. Contributions are welcome! 🎉

## 📧 Contact
For any questions or support, reach out to:  
📧 Email: [your-email@example.com](mailto:your-email@example.com)  
🔗 GitHub: [github.com/your-username](https://github.com/your-username)

---
