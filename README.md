# MachineLearning

Some fundamental machine learning and data analysis techniques are revisited here through practical projects. <br>
Almost every project has been worked in Jupyter notebooks. The notebooks have also been converted into clean pdf files.

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
4. [kMeans Clustering](#kMeans-Clustering): Image compression
5. [Neural Nets](#neural-nets): Autism Spectrum Disorder predictor
6. [Deep neural nets](#deep-neural-nets): Banks' Customer exit predictor

<br><br>
<hr>

# Logistic Regression

**Nudging customers to payed products by utilizing data produced by apps.** <br>
Companies often provide free premium product/services in an attempt to transition their customers to premium membership. In this case study, the services offered by a mobile app are examined. Customers have a 24 hour frame of free premium membership.
Our goal is to determine which users are less likely to subscribe to the paid membership. In this way they can be targeted for further marketing.


# Random Forests
Our goal is to predict the quality of wines given a bunch of features (acidity, density, pH etc.). The original [paper](https://www.sciencedirect.com/science/article/pii/S0167923609001377?via%3Dihub) uses SVN, NN, and MR(multiple regression). A model with random forests is here investigated which achieves a *97.31%* accuracy.

# SVN
We explore a scikit-learn [dataset](https://scikit-learn.org/stable/datasets/index.html#breast-cancer-dataset) concerning malignant and begnin breast cancers. Our dataset consists of a feature vector of 30 features and 1 class describing whether the cancer is malignant or benign.
Our goal is to train a machine learning algorithm to classify unseen samples.

SVM achieves the best result with *98.25%*, followed by Logistic regression (lasso) with *97.37%* and Random Forests with *95.61%*. SVM in particular outperforms even the SVM model in [this](https://www.sciencedirect.com/science/article/pii/S1877050916302575) paper. This is probably due to the state-of-the-art algorithms of [scikit-learn](https://scikit-learn.org/stable/index.html) as a library but also due to the choice of a different kernel from the one used in the paper as a result of hyperparameter tuning.

# kMeans Clustering
KMeans clustering belongs to a category called prototype-based clustering because each cluster is represented by a prototype, which is usually a centroid. It belongs to the class of unsupervised Machine Learning algorithms where the purpose is to scout for latent properties in the data. More information on the algorithm can be found [here](https://towardsdatascience.com/k-means-clustering-with-scikit-learn-6b47a369a83c).

## KMeans clustering and image compresion
The idea is that you can find n (32 for instance) clusters in the image and basically reduce all the 256^3 combinations of colors by creating a new image where the true input color is replaced by the color of the closest cluster. This is very feasible to apply since an image can just be thought of as a numpy array with a length equal to the height of the image and where each element is another array with length equal to the width of the image. Of course the width arrays just contain the RGB properties of the element (which is just a single pixel). The immediate downside of this approach is that the compresion comes at the cost of reducing the image quality.

# Neural Nets
The task is to build an NN model which can predict autism. The model achieves a 99% acuracy rate on the testing set.

# Deep Neural Nets
