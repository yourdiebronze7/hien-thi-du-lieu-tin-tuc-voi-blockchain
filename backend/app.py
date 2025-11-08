from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/news', methods=['POST'])
def post_news():
    news_data = request.json
    # Logic to save news data on blockchain
    return jsonify({'status': 'success', 'data': news_data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)