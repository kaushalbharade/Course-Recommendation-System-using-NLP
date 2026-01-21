# 🎓 AI-Based Course Recommendation System using NLP

## 📌 Overview
This project is an **AI-powered Course Recommendation System** that suggests relevant online courses based on user input.  
It uses **Natural Language Processing (NLP)** techniques and **cosine similarity** to recommend courses that best match a learner’s interests.

The project demonstrates a **practical ML workflow** including data preprocessing, text vectorization, similarity computation, and inference.

---

## 🎯 Problem Statement
With thousands of online courses available, learners face difficulty identifying the most relevant ones.  
Traditional keyword searches are inefficient and inaccurate.

This system solves the problem by recommending courses based on **semantic similarity** rather than exact keyword matches.

---

## 🧠 Solution Approach
1. Preprocess and clean course descriptions  
2. Convert text data into numerical vectors  
3. Compute similarity using **Cosine Similarity**  
4. Recommend top-N most relevant courses  

---

## 🏗️ Project Structure
Ai-Course-Recommendation-System
│
├── app.py
├── Course_Recommendation_System.ipynb
├── Coursera.csv
├── models
│ └── (generated locally, not committed to GitHub)
├── requirements.txt
├── .gitignore
└── README.md


⚠️ **Important Note**  
Large trained model files (`.pkl`) are **generated locally** and intentionally excluded from GitHub to follow best practices and avoid bloated repositories.

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **NLP Techniques:** Text preprocessing & vectorization  
- **ML Technique:** Cosine Similarity  
- **Version Control:** Git & GitHub  

---

## 📊 Dataset
- File: `Coursera.csv`  
- Contains course titles and descriptions used for training and recommendations  

---

## 🚀 How the System Works

User provides a text query or area of interest

Input text is preprocessed and vectorized

Cosine similarity is calculated with course vectors

Top matching courses are returned as recommendations

## ✅ Key Features

NLP-based course recommendation

Simple, scalable, and explainable logic

Clean and professional repository structure

Suitable for resumes and interviews
