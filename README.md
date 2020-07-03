# MachineLearning

Some fundamental machine learning and data analysis techniques are revisited here through practical projects. <br>
Almost every project has been worked in Jupyter notebooks. All the notebooks can be found in a nice .pdf file, which also contains an attachement of the notebook itself.

## The Machine Learning Pipeline utilized for every project
1. Question and required data
2. Acquire the data
3. Data preprocessing
4. Prepare the data for the machine learning model
5. Train the model
6. Make predictions on the test data
7. Evaluate the model
8. If the performance is not satisfactory, adjust the model
9. Interpret the model and report results visually and numerically
<br>

## Table of Contents
1. [Logistic Regression](#logistic-regression): Nudging customers to payed products by utilizing data produced by an app 
2. [Random Forests](#random-forests): Wine quality predictor
3. [SVN](#sVN): Disease predictor

<br><br>
<hr>

# Logistic Regression

**Nudging customers to payed products by utilizing data produced by apps.** <br>
Companies often provide free premium product/services in an attempt to transition their customers to the premium membership. In this case study, the services offered by a mobile app are examined. Customers have a 24 hour frame of free premium membership.
Our goal is to determine which users are less likely to subscribe to the paid membership so that greater marketing offers can be directed at them in a bid to make them premium customers.


# Random Forests
Our goal is to predict the quality of wines given a bunch of features (acidity, density, pH etc.). The original [paper](https://www.sciencedirect.com/science/article/pii/S0167923609001377?via%3Dihub) uses SVN, NN, and MR(multiple regression). An approach of random forests is here investigated which achieves very good results, *97.31%*.

# SVN
We explore a scikit-learn [dataset](https://scikit-learn.org/stable/datasets/index.html#breast-cancer-dataset) concerning malignant and begnin breast cancers. Our dataset consists of a feature vector of 30 features and 1 class which can be 0 (Malignant) or 1 (Benign).
Our goal is to train a machine learning algorithm to classify -given the 30 features- unseen samples as either malignant or benign.

SVM achieves the best result with *98.25%*, followed by Logistic regression (lasso) with *97.37%* and Random Forests with *95.61%*. SVM in particular outperforms even the SVM model in [this](https://www.sciencedirect.com/science/article/pii/S1877050916302575) paper. This is probably due to the supremacy of [scikit-learn](https://scikit-learn.org/stable/index.html) as a library but also due to the choice of a different kernel as a result of hyperparameter tuning.

