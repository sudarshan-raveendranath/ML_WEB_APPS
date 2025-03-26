# 🩺 Diabetes Prediction API - FastAPI

This project provides a **FastAPI-based REST API** for predicting diabetes using a **Support Vector Machine (SVM) model** trained on the **Pima Indians Diabetes Dataset**.

## 🚀 Features
- **FastAPI-based REST API** for real-time predictions.
- **Machine Learning Model** trained using SVM.
- **Pickle-based model serialization** for storage.
- **JSON API requests** for easy integration.
- **Jupyter Notebook (`diabetes prediction.ipynb`)** for model training and experimentation.

## 📂 Project Structure
```
📂 diabetes prediction as FAST API
│── 📂 API
│   │── 📂 __pycache__
│   │── 📄 api_implementation.py      # Core API logic
│   │── 📄 ML_API.py                  # FastAPI main file
│   │── 📄 trained_model.sav          # Saved ML model (SVM)
│
│── 📂 dataset and models
│   │── 📄 diabetes prediction.ipynb  # Jupyter notebook for training
│   │── 📄 diabetes.csv               # Dataset used for training
│   │── 📄 trained_model.sav          # Serialized ML model
│
│── 📄 README.md                      # Project documentation
```

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/diabetes-prediction-api.git
cd diabetes-prediction-api
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install fastapi uvicorn numpy pandas scikit-learn requests
```

## 📊 Model Training & Storage
The machine learning model is trained using **Support Vector Machine (SVM)** in **Jupyter Notebook (`diabetes prediction.ipynb`)**:
1. Load the dataset `diabetes.csv`.
2. Split the features (`X`) and target (`Y`).
3. Train an **SVM classifier**.
4. Save the model as **`trained_model.sav`** using `pickle`.

## 🌍 Running the API
Navigate to the `API` folder and start the FastAPI server using **Uvicorn**:
```sh
cd API
uvicorn ML_API:app --reload
```
By default, the API will be accessible at:  
🔗 **http://127.0.0.1:8000**

### 📜 API Endpoints

| HTTP Method | Endpoint | Description |
|------------|---------|-------------|
| `POST` | `/diabetes_prediction` | Predicts diabetes based on input data |

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
You can manually send a request using `curl`:
```sh
curl -X 'POST' 'http://127.0.0.1:8000/diabetes_prediction' -H 'Content-Type: application/json' -d '{
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
}'
```
Or run a Python test script:
```python
import requests

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

## 📜 License
This project is licensed under the **MIT License**.

## 📧 Contact
For any questions or support, reach out to:  
📧 Email: [your-email@example.com](mailto:your-email@example.com)  
🔗 GitHub: [github.com/your-username](https://github.com/your-username)

---
