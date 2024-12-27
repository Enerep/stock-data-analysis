#startin project

from flask import Flask, render_template, request
import yfinance as yf
#non gui backend(error fix)
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    #user submit
    if request.method == "POST":
        ticker = request.form["ticker"]
        stock = yf.Ticker(ticker)

        # 6 month of data
        data = stock.history(period="6mo")
        
        # Save chart
        plt.figure(figsize=(10, 6))
        #closing stock prices
        data["Close"].plot(title=f"{ticker} Stock Price (6mo)", xlabel="Date", ylabel="Price")
        chart_path = os.path.join("static", "chart.png")
        #save
        plt.savefig(chart_path)
        plt.close()
        
        # Stock Info
        info = stock.info
        
        #html
        return render_template("index.html", chart_path="chart.png", info=info)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
