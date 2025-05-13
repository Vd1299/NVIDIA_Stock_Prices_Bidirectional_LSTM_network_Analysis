# Time Series Forecasting for Nividia Stock Price with Bidirectional LSTMs
This repository contains a dual-model approach to time series analysis and prediction using Bidirectional Long Short-Term Memory (LSTM) neural networks implemented in TensorFlow/Keras.

## Project Overview
This project implements two complementary deep learning models for time series analysis:

Regression Model: Predicts continuous values for the next 10 time steps (minutes)
Classification Model: Categorizes future movement direction into three classes (up, same, down)

Both models leverage bidirectional LSTM architectures to capture temporal patterns from historical time series data, providing both precise numerical forecasts and actionable directional insights.
Features
Bidirectional LSTM networks for capturing patterns in both forward and backward directions
Dual prediction approach (regression + classification)
Dropout layers for regularization to prevent overfitting
Early stopping and adaptive learning rate reduction during training
Comprehensive evaluation metrics for model performance assessment

## Evaluation
The regression model is evaluated using Mean Squared Error (MSE) and Mean Absolute Error (MAE), while the classification model is assessed using accuracy, precision, recall, and F1-score metrics.

## Data Preparation
Data is extracted from Polygon.io using the api for past 180 days at minute level interval for Nvidia stock. Time series data is preprocessed using sliding windows to create input-output pairs for training. For the classification model, continuous targets are converted to categorical labels (up, same, down) based on directional movement.

## License
[MIT](https://choosealicense.com/licenses/mit/)
