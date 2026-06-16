from flask import Flask, render_template, request
from analysis import get_stock_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    stock_data = None
    signal = None

    if request.method == "POST":
        ticker = request.form["ticker"]

        try:
            df, signal = get_stock_data(ticker)

            stock_data = {
                "ticker": ticker.upper(),
                "price": round(df["Close"].iloc[-1], 2),
                "volume": int(df["Volume"].iloc[-1])
            }

        except:
            stock_data = None

    return render_template(
        "index.html",
        stock_data=stock_data,
        signal=signal
    )

if __name__ == "__main__":
    app.run(debug=True)
