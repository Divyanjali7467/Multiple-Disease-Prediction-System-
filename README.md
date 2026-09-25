# 🏥 Multiple Disease Prediction System using Machine Learning

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn">
<img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/NumPy-2.0.2-013243?style=for-the-badge&logo=numpy">
<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas">

</p>

<p align="center">

### 🩺 An Interactive Machine Learning Web Application for Multiple Disease Prediction

</p>

---

## 🌟 Project Overview

**Multiple Disease Prediction System** is a Machine Learning based web application that predicts the possibility of three diseases:

🩸 **Diabetes**  
❤️ **Heart Disease**  
🧠 **Parkinson's Disease**

The application provides a simple and interactive interface where users enter disease-specific medical parameters and receive a Machine Learning based prediction.

The project integrates **Python, Scikit-learn, NumPy, Pandas and Streamlit** into a single healthcare-oriented application.

> ⚠️ **Disclaimer:** This project is intended for educational and demonstration purposes only. Predictions should not be considered professional medical diagnosis or medical advice.

---

# ✨ Key Features

| Feature | Description |
|---|---|
| 🩸 Diabetes Prediction | Predicts diabetes based on medical parameters |
| ❤️ Heart Disease Prediction | Predicts the possibility of heart disease |
| 🧠 Parkinson's Prediction | Uses biomedical voice measurements |
| 🎛️ Interactive Navigation | Sidebar-based disease selection |
| 🤖 ML Models | Separate trained model for each disease |
| ⚡ Real-Time Prediction | Generates predictions from user inputs |
| 🌐 Web Interface | Built using Streamlit |
| ☁️ Deployment Ready | Can be deployed using Streamlit Community Cloud |

---

# 🏗️ System Architecture

```text
                         👤 USER
                           │
                           ▼
                ┌──────────────────────┐
                │    🌐 STREAMLIT UI   │
                │                      │
                │  Disease Selection   │
                └──────────┬───────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   🩸 Diabetes       ❤️ Heart Disease   🧠 Parkinson's
      Inputs              Inputs            Inputs
          │                │                │
          ▼                ▼                ▼
   ┌────────────┐   ┌────────────┐   ┌────────────┐
   │ Diabetes   │   │   Heart     │   │ Parkinson's│
   │ ML Model   │   │ Disease ML │   │ ML Model   │
   └──────┬─────┘   └──────┬─────┘   └──────┬─────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                  🤖 ML PREDICTION
                           │
                           ▼
                  📊 RESULT DISPLAY



#🔄 Application Workflow

 🚀 START
                            │
                            ▼
                  🌐 Open Web Application
                            │
                            ▼
                    🎛️ Select Disease
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        🩸 Diabetes     ❤️ Heart       🧠 Parkinson's
             │          Disease             │
             │              │               │
             ▼              ▼               ▼
        Enter Medical   Enter Medical   Enter Voice
        Parameters      Parameters      Features
             │              │               │
             └──────────────┼───────────────┘
                            │
                            ▼
                    🔢 Process Inputs
                            │
                            ▼
                    🤖 Load ML Model
                            │
                            ▼
                    🔮 Generate Prediction
                            │
                            ▼
                    📊 Display Result
                            │
                            ▼
                           🏁 END
#🤖 Machine Learning Workflow

                  📂 MEDICAL DATASET
                         │
                         ▼
                  🔍 DATA ANALYSIS
                         │
                         ▼
                 🧹 DATA PREPROCESSING
                         │
                         ▼
                  🎯 FEATURE SELECTION
                         │
                         ▼
                ✂️ TRAIN / TEST SPLIT
                         │
                         ▼
                 🤖 MODEL TRAINING
                         │
                         ▼
                 📈 MODEL EVALUATION
                         │
                         ▼
                💾 MODEL SERIALIZATION
                         │
                         ▼
                  📦 .SAV MODEL FILE
                         │
                         ▼
                 🌐 STREAMLIT APP
                         │
                         ▼
                  👤 USER INPUT
                         │
                         ▼
                 🔮 MODEL PREDICTION
                         │
                         ▼
                   📊 RESULT

#🛠️ Technology Stack
💻 Programming Language
Technology	Purpose
🐍 Python	Core programming language
🤖 Machine Learning
Technology	Purpose
Scikit-learn	Machine Learning model development and prediction
NumPy	Numerical computation and array operations
Pandas	Dataset handling and data processing
Pickle	Saving and loading trained ML models

🌐 Web Application
Technology	Purpose
Streamlit	Building the interactive web application
Streamlit Option Menu	Sidebar navigation between disease prediction modules

🧰 Development Tools
Tool	Purpose
🐍 Anaconda	Python environment management
🔬 Spyder	Python development and experimentation
💻 VS Code	Code editing
📓 Google Colab	Machine Learning experimentation/training
🌿 Git	Version control
🐙 GitHub	Source code and project hosting

📦 Project Dependencies
Python
│
├── NumPy
├── Pandas
├── Scikit-learn
├── Streamlit
├── Streamlit Option Menu
└── Pickle

📁 Project Structure
Multiple-Disease-Prediction-System/
│
├── 📄 multiple disease pred.py
│
├── 📄 requirements.txt
│
├── 🩸 diabetes_model.sav
│
├── ❤️ heart_disease_model.sav
│
├── 🧠 parkinsons_model.sav
│
└── 📄 README.md

🧩 Model Architecture

The application contains three independent trained Machine Learning models.

                    Multiple Disease System
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
       🩸 Diabetes       ❤️ Heart Disease   🧠 Parkinson's
          Model               Model             Model
             │                │                │
             ▼                ▼                ▼
       Medical Data       Medical Data      Voice Features
             │                │                │
             ▼                ▼                ▼
          Prediction        Prediction       Prediction

🎨 User Interface

The application provides a sidebar navigation menu:

╔══════════════════════════════════╗
║  🏥 Multiple Disease Prediction  ║
╠══════════════════════════════════╣
║                                  ║
║  🩸 Diabetes Prediction           ║
║                                  ║
║  ❤️ Heart Disease Prediction      ║
║                                  ║
║  🧠 Parkinsons Prediction         ║
║                                  ║
╚══════════════════════════════════╝

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Divyanjali7467/Multiple-Disease-Prediction-System.git

Move into the project directory:

cd Multiple-Disease-Prediction-System
2️⃣ Create a Virtual Environment

Using Conda:

conda create -n disease310 python=3.10

Activate it:

conda activate disease310
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
streamlit run "multiple disease pred.py"

The application will open in your browser.

Default local URL:

http://localhost:8501

📋 Requirements

The project uses:

streamlit
streamlit-option-menu
numpy==2.0.2
scikit-learn==1.7.2
pandas

These dependencies are listed in:

requirements.txt
☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

Deployment workflow
💻 Local Development
        │
        ▼
      🐙 Git
        │
        ▼
      GitHub
        │
        ▼
☁️ Streamlit Community Cloud
        │
        ▼
🌐 Live Web Application
🔐 Model Loading

The trained models are stored as serialized .sav files:

diabetes_model.sav
heart_disease_model.sav
parkinsons_model.sav

The application loads them using:

import pickle

model = pickle.load(open("model.sav", "rb"))

The loaded model then receives the user's input features and generates a prediction.

📊 Prediction Pipeline
User Input
    │
    ▼
Feature Collection
    │
    ▼
Numerical Input
    │
    ▼
Trained ML Model
    │
    ▼
Prediction
    │
    ├───────────────┐
    │               │
    ▼               ▼
Positive         Negative
Prediction       Prediction
    │               │
    ▼               ▼
Disease           No Disease
Detected          Detected
🎯 Project Objectives

The main objectives of this project are:

🩺 Build an interactive healthcare prediction application.
🤖 Apply Machine Learning to multiple disease prediction problems.
🧹 Process and handle medical datasets.
💾 Save and reuse trained Machine Learning models.
🌐 Build a user-friendly web interface using Streamlit.
🔀 Integrate multiple prediction models into one application.
🚀 Deploy the Machine Learning application as a web service.
📚 Demonstrate the practical application of Machine Learning in healthcare.
💡 Key Learning Outcomes

Through this project, the following concepts are demonstrated:

🐍 Python
Functions
Variables
Conditional statements
Lists and arrays
File handling
Exception handling
📊 Data Science
Dataset handling
Data preprocessing
Feature selection
Numerical data processing
🤖 Machine Learning
Model training
Model evaluation
Classification
Model serialization
Prediction
🌐 Deployment
Streamlit application development
Requirements management
Git and GitHub
Cloud deployment
🔮 Future Enhancements

Possible improvements include:

📈 Display prediction confidence/probability.
📊 Add model performance metrics.
📉 Add interactive data visualizations.
🎨 Improve UI/UX with custom styling.
🔐 Add user authentication.
🗄️ Add database support.
📋 Generate downloadable prediction reports.
📱 Improve mobile responsiveness.
☁️ Add scalable cloud deployment.
🧠 Experiment with additional Machine Learning models.
