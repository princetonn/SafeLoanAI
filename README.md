# SafeLoanAI

## Table of Contents
- [Overview](#overview)
- [Model Development](#model-development)
- [Dataset](#dataset)
## Overview 

Loans given to those who default has disasterous consquences to the loaner, the borrower, as well as society as a whole. Lenders suffer high financial loses and reduced trust, which harms the lending instituion. The borrower who default faces limited financial opportunites in the future due to their default, keeping them stuck in financial instability. On a societal level, mass defaults may cause financial crashes and economic instability. 

SafeLoanAI provides a quick and easy way for lenders and borrowers to check if their loan is considered "good" or "bad", based off how likely it is for the borrower to default.

This model was built through MATLAB's TreeBagger with 1,000 trees.

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Python(Flask)
- **Machine Learning**: MATLAB
- **Libraries & Tools**:
  - Flask
  - MATLAB Engine API
  - MATLAB Statistics and Machine Learning Toolbox

## Dataset

This project utilizes the [German Credit Dataset](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data) from the UCI Machine Learning Repository. The dataset consists of 1,000 datapoints with 20 attributes, which include both numerical and categorical variables, and a class variable indicating credit risk ("good" or "bad"). I split the dataset into training data(70%) and testing data(30%).

