### Author: Arkadiusz Modzelewski
# Microeconometrics Project - Big Data: New Tricks for Econometrics 

This notebook replicates results from [the article](https://www.aeaweb.org/articles?id=10.1257/jep.28.2.3):
Varian, Hal R. 2014. "Big Data: New Tricks for Econometrics." Journal of Economic Perspectives, 28 (2): 3-28.

Project to grade: [Project by Arkadiusz Modzelewski](https://github.com/HumanCapitalAnalysis/student-project-ArcadiusM/blob/master/Student_Project_n.ipynb)

[![Build Status](https://travis-ci.com/ArcadiusM/Big-Data-New-Tricks-for-Econometrics.svg?branch=master)](https://travis-ci.com/ArcadiusM/student-project-ArcadiusM)

Problems with nbviewer: Please take into account that when I tried to view my project with nbviewer not always whole project appeared. The end of the project is part with References. 
<a href="https://nbviewer.jupyter.org/github/ArcadiusM/student-project-ArcadiusM/blob/master/Student_Project_n.ipynb" 
   target="_parent">
   <img align="center"
  src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.png"
      width="109" height="20">
</a>

## Abstract

The aim of the project is the replication of most of the content of the scientific article „Big Data: New Tricks for Econometrics” written by Hal R. Varian. The author for his results and implementation used RStudio with R programming language. This project is done in Python language using Jupyter Notebook which is one of the most popular tool for Data Scientists. The article by Varian introduces the main and basic machine learning methods and explains its importance in econometrics and economics. It gives also examples of using mentioned machine learning methods in a real problems.

## Replication part

Firstly, the classification tree was replicated, whose task was to check whether on the basis of other available data we are able to predict with high accuracy who survived the Titanic disaster and who did not. Classifification based on two other variables can also be ilustrated in the partition plot, which shows how the tree divides up the space into rectangular regions. This partition plot was shown in this project Then in the article the decision tree was compared with logistic regression, so the logistic regression was also replicated. Secondly, Varian in the programming language R compared 4 methods once again using Titanic data. This part was also replicated in the project. Then the decision trees, logistic regression and random forest were used for the mortgage data in Boston. In this section Varian quoted a problem which Munnell, Tootell, Browne, and McEneaney tried to solve (1996). They examined mortgage lending in Boston to see if race played a signifificant role in determining who was approved for a mortgage. In the last part, Varian presented methods that can be used to select a model, such as Lasso. Final replicated part, as in the article, includes LassoCV and also variables selection in time series.

## Additional part

In the additional part I briefly present three methods which were not implemented by Varian and which can also be useful and are used in economics. In every part of the addition new method is compared in case of preddiction accuracy to method presented in chosen article. Brief introductions to other methods are based mostly on two common books: G. James, D. Witten, T. Hastie and R. Tibshirani: An Introduction to Statistical Learning with Applications in R and T. Hastie, R. Tibshirani J. Friedman: The Elements of Statistical Learning: Data Mining, Inference, and Prediction.

As one of the aims of the article written by Varian was to show that it is worth for Econometricians and Economists to know and use basic machine learning methods, in my addition I will also focus mostly on basic and commonly used datasets. The reason is to show an importance of these methods and make it easily understandable.

Other methods that I have chosen and used:

1. KNN Classifier:
KNN Classifier was used to predict the class of unknown plant for Iris dataset.
KNN Classifier was compared to Decision Tree Classifier
2. Ridge Regression:
Ridge Regression was used to predict price of sold house with given features.
Ridge Regression was compared to Lasso
3. Gradient Boosting Classifier:
Gradient Boosting Classifier was used to predict if a candy is chocolate or not based on its other features.
Gradient Boosting Classifier was compared to Random Forest Classifier and both methods were pruned in order to get more accurate prediction and to deal with overfittnig



[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/HumanCapitalAnalysis/student-project-ArcadiusM/blob/master/LICENSE)
