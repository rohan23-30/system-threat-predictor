# 🛡️ System Threat Predictor

This project predicts whether a computer system is at risk based on hardware and usage features.

## 📦 Components

- `train_model.py` → trains a Random Forest model on provided data.
- `app.py` → Streamlit web app to make predictions interactively.
- `Detection.py` → includes exploratory data analysis and evaluation (confusion matrix, ROC curve, etc.).

## 📊 Data

- `train (1).csv` → training data.
- `test (1).csv` → test data.
- `threat_model.pkl` → trained model.
- `feature_names.pkl` → saved feature names.

## 🚀 How to run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Train the model (if needed):

```bash
python train_model.py
```

3. Run the web app:

```bash
streamlit run app.py
```

## ✅ Features used

- Total Physical RAM (MB)
- Processor Core Count
- Chassis Type
- Is System Protected
- Is Gamer
- Power Platform Role

## 📌 License

MIT License (or your choice)

📷 Screenshots

### ✅ Prediction - Safe System
![Safe prediction screenshot](Images/output2.png)

### ⚠️ Prediction - High Risk System
![High risk prediction screenshot](Images/output1.png)

