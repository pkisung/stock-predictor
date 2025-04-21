# Stock Predictor API 

## Overview

This project is a stock price prediction application built using **LSTM (Long Short-Term Memory)** neural networks to predict stock prices based on historical data. The application fetches stock price data using the **Yahoo Finance API** and predicts future stock prices for the next 7 days. The predictions are returned along with visualized graphs for a more intuitive representation of the predicted price trends.

### Docker Environment
This application is containerized using **Docker** to ensure consistent development and deployment environments. Docker allows for the creation of isolated environments where all dependencies, including Python libraries and the Flask application, are packaged together. By using Docker, you can run the application on any machine without worrying about dependencies or setup issues.

To run this project, simply use Docker to build and run the container, which includes everything needed to run the application.

## Key Features
1. **Stock Price Prediction**: Predicts stock prices for the next 7 days based on historical data using LSTM.
2. **Prediction Graphs**: Visualize stock price predictions in graphical form.
3. **Price Volatility**: Displays the price volatility (difference between the highest and lowest predicted prices).
4. **Current Price Display**: Shows the latest price for the selected stock.
5. **Dockerized Application**: The entire application, including the machine learning model, is containerized using Docker for easy deployment and scalability.

## Requirements

- **Docker**: Ensure Docker is installed on your machine. The application runs within a Docker container for consistent development and deployment.
- **Python 3.9+**: The application uses Python and several libraries like `Flask`, `TensorFlow`, and `yfinance`.

## Docker Setup and Running the Application

1. **Clone the Repository**
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/stock-predictor.git
   cd stock-predictor
   
2. **Build the Docker Image** In the project directory, run the following command to build the Docker image:
   ```bash
   docker-compose build --no-cache
   
3. **Run the Application** Once the image is built, run the Docker container using:
   ```bash
   docker-compose up -d
This will start the application and make it accessible at http://127.0.0.1:5050/ on your local machine.


4.**Access the Application** Open your browser and navigate to: 
http://127.0.0.1:5050/

You should now see the stock predictor interface where you can input a stock ticker (e.g., AAPL, TSLA, AMZN) and receive predictions along with a graph.


## How It Works

**Data Collection**:
The application fetches historical stock price data for a given ticker symbol (e.g., AAPL, TSLA) using the Yahoo Finance API via the yfinance library. The data is fetched for the past year at daily intervals.

**Machine Learning Model**:
The core of the application is an LSTM (Long Short-Term Memory) model built using TensorFlow. The model is trained using the historical stock price data and then used to predict future prices for the next 7 days.

**Visualization**:
  + Graphical Output: After predictions are made, a graph is generated using Matplotlib to display the predicted stock prices over time.

  + Price Volatility: The application calculates the price volatility by finding the difference between the highest and lowest predicted values, and displays it to the user.

**Predicting Prices**:
The prediction results are returned in JSON format, which includes the predicted stock prices, the graph URL, the current price, and the volatility.

**Flask API**:
The application uses Flask as the web framework, where:

  + GET /: Displays the homepage where users can input a ticker symbol.

  + POST /predict: Accepts a ticker symbol, performs predictions, and returns the results in JSON format, including predictions, graph URL, current price, and volatility.

**Example Ticker Symbols**
  + AAPL (Apple Inc.)

  + TSLA (Tesla Inc.)

  + AMZN (Amazon)

  + GOOGL (Alphabet Inc.)

  + MSFT (Microsoft)

## Project Structure
<code>
stock-predictor/
│
├── app/                         # Contains Flask application files
│   ├── templates/               # HTML templates (index.html)
│   ├── static/                  # Generated images for prediction graphs
│   ├── main.py                  # Main Flask application
│   └── model.py                 # Model for stock prediction
│
├── Dockerfile                   # Docker configuration file
├── docker-compose.yml           # Docker Compose configuration
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
</code></br>

## Docker Compose
The application is set up with Docker Compose, which simplifies the management of Docker containers. It ensures that all the necessary services, like Flask and TensorFlow, are properly configured.

**Docker Compose Command**:
  + Build Docker Image:
    ```bash
      docker-compose build
  + Run Application:
    ```bash
      docker-compose up

## Trouble shooting: 
  + If you encounter issues while building the Docker image, ensure that you have all dependencies listed in requirements.txt installed and that you're running the latest version of Docker.
  + If the application fails to start, check the Docker container logs using:
    ```bash
      docker logs <container_id>
  
