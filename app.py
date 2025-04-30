from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return jsonify({
            "city": city,
            "temperature": data['main']['temp'],
            "condition": data['weather'][0]['description']
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
