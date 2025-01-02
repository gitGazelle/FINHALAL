from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/api/get_stock_data', methods=['GET'])
def get_stock_data():
    stock_symbol = request.args.get('symbol')
    if not stock_symbol:
        return jsonify({'error': 'No stock symbol provided'}), 400

    # Placeholder data (replace with real stock API)
    stock_data = {
        'symbol': stock_symbol,
        'price': 123.45,
        'change': '+1.23%',
        'market_cap': '500B'
    }

    return jsonify(stock_data)

@api.route('/api/check_shariah_compliance', methods=['GET'])
def check_shariah_compliance():
    stock_symbol = request.args.get('symbol')
    if not stock_symbol:
        return jsonify({'error': 'No stock symbol provided'}), 400

    # Placeholder compliance check
    is_compliant = stock_symbol.lower() not in ['alibaba', 'microsoft']
    return jsonify({
        'symbol': stock_symbol,
        'is_compliant': is_compliant
    })
