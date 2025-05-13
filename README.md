Time Series Forecasting for Nividia Stock Price with Bidirectional LSTMs
This repository contains a dual-model approach to time series analysis and prediction using Bidirectional Long Short-Term Memory (LSTM) neural networks implemented in TensorFlow/Keras.

Project Overview
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
