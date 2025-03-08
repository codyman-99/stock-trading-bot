import yfinance as yf
from flask import Flask
import threading
import time

app = Flask(__name__)

def fetch_stock_price():
    while True:
        stock = yf.Ticker("AAPL")
        price = stock.history(period="1d")['Close'].iloc[-1]
        print(f"Latest AAPL Stock Price: ${price:.2f}")
        time.sleep(60)  # Fetch price every 60 seconds

@app.route('/')
def home():
    return "Stock Bot is Running!"

# Start stock fetching in the background
threading.Thread(target=fetch_stock_price, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    
    from webull import webull

wb = webull()

# Replace with your Webull login credentials
email = "your_email@example.com"
password = "your_password"

# Login to Webull
wb.login(email=email, password=password)

# Verify login success
account_id = wb.get_account_id()
print(f"✅ Webull Login Successful! Account ID: {account_id}")
print(\"Attempting to log into Webull...\")
wb.login(email=email, password=password)
print(\"✅ Webull login function executed.\")
