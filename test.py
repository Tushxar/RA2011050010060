from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    url_list = request.args.getlist('url')
    
    if not url_list:
        return jsonify({"error": "No URLs provided"}), 400
    
    numbers_data = []
    
    for url in url_list:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()  # Assuming the response contains JSON data
            numbers_data.append(data)
        except requests.exceptions.RequestException as e:
            numbers_data.append({"error": f"Failed to fetch data from {url}: {str(e)}"})
    
    return jsonify(numbers_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
