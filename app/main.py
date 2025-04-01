from flask import Flask, render_template, request, jsonify
from model import get_stock_data, train_model, predict_future, save_prediction_plot
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    ticker = "AAPL"  # 기본값 설정
    if request.method == "POST":
        ticker = request.form.get("ticker", "AAPL")  # 사용자가 입력한 값이 있으면 변경
    return render_template("index.html", ticker=ticker)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        ticker = data.get("ticker")

        # 데이터 가져오기
        stock_data, current_price = get_stock_data(ticker)
        model, scaler = train_model(stock_data)

        # 미래 예측
        predictions = predict_future(model, stock_data, scaler)
        max_pred = max(predictions)
        min_pred = min(predictions)
        volatility = max_pred - min_pred  # 최대값 - 최소값 차이 계산

        # 그래프 저장
        img_path = save_prediction_plot(predictions, ticker)

        return jsonify({
            "ticker": ticker,
            "predictions": predictions.tolist(),
            "volatility": float(volatility),  # volatility 값을 float로 변환하여 반환
            "current_price": current_price,
            "graph": img_path
        })
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
