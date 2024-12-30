# User Carbon Emissions Prediction Using LSTM
This project implements a Long Short-Term Memory (LSTM) neural network to predict weekly carbon emissions based on historical data. The model is designed to help users forecast their emissions and make informed decisions to reduce their environmental impact.

# What is LSTM?
LSTM (Long Short-Term Memory) is a type of recurrent neural network (RNN) capable of learning and retaining long-term dependencies in sequential data. Unlike traditional RNNs, LSTMs use a gating mechanism to control the flow of information, making them particularly effective for time-series data, such as weekly carbon emissions.

Why Use LSTM?
- Captures Temporal Patterns: LSTMs are well-suited for modeling temporal relationships in data, essential for predicting emissions based on historical trends.
- Handles Long-Term Dependencies: With memory cells and forget gates, LSTMs retain relevant information over extended sequences.
- Reduces Vanishing Gradient Problems: The gating mechanism ensures efficient backpropagation, even in deep networks.

![image](https://github.com/user-attachments/assets/05816f84-c60f-48ee-a4de-127842bb9bf5)

# Features
1. Data Exploration and Visualization: Analyze and visualize weekly carbon emissions trends.
2. Data Normalization: Scale the data for efficient training using Min-Max scaling.
3. LSTM Model Implementation: Leverage a three-layer LSTM architecture for temporal sequence modeling.
4. Model Evaluation: Assess model performance using metrics like MAE, MSE, and RMSE.
5. Prediction: Forecast future carbon emissions based on user-provided weekly data.
6. Model Saving and Loading: Save the trained model for later use and load it for predictions.

# Workflow
1. Data Loading:
   - Load weekly carbon emissions data from a CSV file.
2. Data Visualization:
   - Plot weekly emissions for trend analysis.
3. Data Preprocessing:
   - Normalize the emissions data using Min-Max scaling.
   - Create sequences of data for training the LSTM model.
4. Model Development:
   - Build a three-layer LSTM network with dropout regularization.
   - Train the model using the training dataset.
5. Model Evaluation:
   - Plot training and validation loss.
   - Compute MAE, MSE, and RMSE metrics for test data.
6. Prediction:
   - Predict emissions for user-provided weekly data.
7. Model Saving:
   - Save the trained model for future use.

# Example Output
Training and Validation Loss

![image](https://github.com/user-attachments/assets/bf90587b-8c2b-4d2c-aea6-bc43baa16900)

Predicted vs. Actual Emissions

![image](https://github.com/user-attachments/assets/5f887a1d-754b-426e-b4d8-4288c2df2b93)

Sample Prediction

For input [84743, 93845, 87362, 85236], the model predicts:

Predicted emissions for the next week: [value]

# File Structure
- New Data.csv: Dataset containing weekly carbon emissions.
- (p)_weekly_carbon_emissions_prediction.py: Main script for training, evaluation, and prediction.
- prediksi_emisi_mingguan.h5: Saved LSTM model.

# Metrics Used
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
