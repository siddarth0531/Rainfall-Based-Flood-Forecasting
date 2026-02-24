Flood Prediction System 🌊
Overview
This project is an AI-driven solution designed to predict the probability of floods based on meteorological data. Using the XGBoost Classifier, the system achieves a high accuracy of 96.55%. The project features a user-friendly web interface built with Flask, allowing users to receive instant risk assessments (Chance/No Chance).

🚀 Key Features
Machine Learning Engine: Powered by XGBoost for high-speed and accurate classification.

Web Interface: Interactive Flask application for real-time data entry and results.

Performance Visuals: Includes Confusion Matrix and Accuracy metrics for scientific validation.

🛠️ Tech Stack
Language: Python 3.10

ML Frameworks: Scikit-Learn, XGBoost

Data Handling: Pandas, NumPy 
Web: Flask, HTML, CSS

Environment: Google Colab & VS Code

📁 Project Structure
This repository is organized into 8 core phases:

1_Ideation_Phase: Empathy maps and user personas.

2_Requirement_Analysis: Technical requirements and Data Flow Diagrams.

3_Project_Design: System architecture and UI mockups.

4_Project_Planning: Timeline and task management.

5_Development_Phase: Python scripts, model files (.save), and HTML templates.

6_Performance_Testing: Accuracy scores and Confusion Matrix.

7_Doc_and_Demo: Final report and result screenshots.

📊 Performance Summary

Model Type: XGBoost (Extreme Gradient Boosting)
•  Test Samples: 23 total (20 Safe, 3 Flood)
•  Accuracy: 100%
•  Result: The model successfully identified all flood risks and safe conditions without any False Positives or False Negatives.
Why XGBoost won:
1.	Gradient Boosting: It builds trees sequentially, where each new tree corrects the errors of the previous ones.
2.	Regularization: It has built-in $L1$ and $L2$ regularization, which prevents the model from "memorizing" the data (overfitting).
3.	Handling Sparsity: It is highly efficient at handling missing values or varied weather scales (like Rainfall vs. Temperature).
exection demo is in this link https://drive.google.com/file/d/13_NVVIo-Zd-7yF2WrA6RxaC6FchvitFN/view?usp=sharing
The application is fully IBM Cloud Ready. While the logic for IBM Watson Machine Learning has been developed and verified (see ibm_app_logic.py), the current live demonstration utilizes a local Flask deployment.

Note on Cloud Hosting: Due to the transition of IBM Cloud's Free Tier to a paid subscription model (billing-restricted), the model is currently served via a local environment to ensure 24/7 accessibility for reviewers without incurring cloud service costs. The backend code remains 100% compatible with the IBM Watson REST API
