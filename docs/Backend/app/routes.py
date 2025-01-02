from flask import Blueprint, render_template
from .models import Stock

# Define a Blueprint for routes
main_routes = Blueprint('main', __name__)

# Home route
@main_routes.route('/')
def home():
    return "Welcome to FinHalal Website!"

# Example API route for fetching stock data
@main_routes.route('/stocks')
def get_stocks():
    stocks = Stock.query.all()
    return {'stocks': [{'id': stock.id, 'name': stock.name, 'symbol': stock.symbol, 'price': stock.price} for stock in stocks]}

# More routes can be added here for other pages, API, etc.
