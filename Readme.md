# Sentiment-Analysis
# End-to-End Sentiment Analysis System Using NLP & Machine Learning

## Project Overview

This project implements an end-to-end sentiment analysis system using Natural Language Processing (NLP) and Machine Learning techniques. The system classifies movie reviews as either Positive or Negative based on the textual content of the review.

The project demonstrates the complete machine learning workflow including:

* Data ingestion and exploration
* Text preprocessing
* Feature engineering
* Model training and evaluation
* Hyperparameter tuning
* Sentiment prediction on new text
* Model comparison and selection

---

## Dataset Description

Dataset: IMDb Movie Reviews Dataset

Source:
https://huggingface.co/datasets/imdb

Dataset Characteristics:

* Approximately 50,000 movie reviews
* Binary sentiment classification
* Positive and Negative sentiment labels
* Balanced dataset

Target Variable:

* 1 = Positive Review
* 0 = Negative Review

---

## Project Workflow

### 1. Data Ingestion and Understanding

* Loaded IMDb review dataset
* Examined dataset structure
* Checked for missing values
* Verified class distribution
* Analyzed review lengths

### 2. Exploratory Data Analysis (EDA)

Performed:

* Sentiment distribution analysis
* Review length distribution analysis
* Word frequency analysis
* Word cloud visualization

Key Findings:

* Dataset is balanced between positive and negative reviews.
* Review lengths vary significantly.
* Common sentiment-related words appear frequently within each class.

---

## Text Preprocessing

The following NLP preprocessing steps were applied:

* Lowercasing
* Tokenization
* Stopword removal
* Punctuation removal
* Text cleaning
* Lemmatization

Purpose:

These steps reduce noise, standardize the text, and improve model performance.

---

## Feature Engineering

Two feature extraction techniques were implemented:

### Bag of Words (BoW)

Converts text into numerical vectors based on word occurrence frequencies.

### TF-IDF

Term Frequency–Inverse Document Frequency was used to assign importance scores to words while reducing the impact of commonly occurring terms.

TF-IDF was selected as the primary feature representation because it produced stronger model performance.

---

## Models Trained

The following machine learning models were trained and compared:

### Logistic Regression

* Best Performing Model

### Naive Bayes

* Fast baseline model for text classification

### Random Forest

* Ensemble tree-based classifier

---

## Model Evaluation

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Cross Validation

### Results

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 88.42%   | 87.34%    | 89.70% | 88.51%   |
| Naive Bayes         | 85.32%   | 84.81%    | 85.84% | 85.32%   |
| Random Forest       | 85.00%   | 85.08%    | 84.67% | 84.87%   |

### Cross Validation

Mean Cross Validation Accuracy:

86.24%

---

## Hyperparameter Tuning

GridSearchCV was used to optimize Logistic Regression.

Best Parameter:

C = 1

The tuned model achieved the highest validation performance and was selected as the final model.

---

## Final Model Selection

Logistic Regression was selected because:

* Highest overall accuracy
* Strong precision and recall balance
* High interpretability
* Efficient training time
* Consistent cross-validation performance

---

## Inference Pipeline

The project includes a reusable prediction pipeline.

Example:

```python
predict_sentiment("This movie was fantastic!")
```

Output:

```text
Positive
```

Example:

```python
predict_sentiment("I hated this movie.")
```

Output:

```text
Negative
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Matplotlib
* Seaborn
* WordCloud
* Jupyter Notebook

---

## Project Structure

```text
Sentiment-Analysis-NLP-ML/
│
├── data/
├── models/
├── notebooks/
│   └── eda_and_modeling.ipynb
│
├── README.md
├── Requirements.txt
└── app.py
```

---

## How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/Trumplican47/Sentiment-Analysis.git
```

2. Install dependencies

```bash
pip install -r Requirements.txt
```

3. Launch Jupyter Notebook

```bash
jupyter notebook
```

4. Open:

```text
notebooks/eda_and_modeling.ipynb
```

5. Run all cells from top to bottom.

---

## Author

Patrick Malhotra

Career Amend Data Science Program

End-to-End Sentiment Analysis Project
