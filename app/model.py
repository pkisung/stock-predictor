import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import os

def get_stock_data(ticker):
    """Fetch stock price data from Yahoo Finance, including the latest price."""
    df = yf.download(ticker, period="1y", interval="1d")
    
    # 현재 가격 가져오기
    latest_price = df['Close'].iloc[-1]

    return df[['Close']], float(latest_price)  # 현재 가격을 float로 변환하여 반환

def save_prediction_plot(predictions, ticker):
    """Save the stock price prediction graph as an image."""
    import matplotlib.pyplot as plt

    # static 폴더가 없으면 생성
    static_path = "static"
    if not os.path.exists(static_path):
        os.makedirs(static_path)

    plt.figure(figsize=(8, 4))
    plt.plot(predictions, marker="o", linestyle="-", color="blue", label="Predicted Price")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.title(f"{ticker} Stock Price Prediction")
    plt.legend()
    
    # Flask에서 올바르게 접근할 수 있도록 경로 수정
    img_path = f"static/{ticker}_prediction.png"
    plt.savefig(img_path)
    plt.close()

    return img_path

def train_model(data):
    """Train an LSTM model on the given stock data."""
    if len(data) < 120:
        raise ValueError("Not enough data for training and validation.")

    train_size = int(len(data) * 0.8)
    train_data = data[:train_size]
    valid_data = data[train_size:]

    scaler = MinMaxScaler(feature_range=(0,1))
    train_scaled = scaler.fit_transform(train_data)
    valid_scaled = scaler.transform(valid_data)

    X_train, y_train = [], []
    for i in range(60, len(train_scaled)):
        X_train.append(train_scaled[i-60:i, 0])
        y_train.append(train_scaled[i, 0])

    X_train, y_train = np.array(X_train), np.array(y_train)

    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
        LSTM(50, return_sequences=False),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=1)

    return model, scaler

def predict_future(model, data, scaler):
    """Predict stock prices for the next 7 days."""
    last_60_days = data[-60:].values
    last_60_scaled = scaler.transform(last_60_days)
    X_test = np.reshape(last_60_scaled, (1, last_60_scaled.shape[0], 1))

    predictions = []
    for _ in range(7):
        pred = model.predict(X_test)[0][0]
        predictions.append(pred)
        X_test = np.roll(X_test, -1)
        X_test[0, -1, 0] = pred

    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    return predictions
