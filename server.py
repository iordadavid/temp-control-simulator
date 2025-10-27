from flask import Flask, jsonify, render_template
import threading, time, random

app = Flask(__name__)

temperature = 25.0
heater_on = False

def simulate_temperature():
    global temperature, heater_on
    while True:
        # simulate heating/cooling
        if heater_on:
            temperature += random.uniform(0.2, 0.4) # heating
        else:
            temperature -= random.uniform(0.1, 0.2) # cooling

        if temperature < 22:
            heater_on = True
        elif temperature > 28:
            heater_on = False

        time.sleep(1)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/data')
def data():
    return jsonify({
        'temperature': round(temperature, 2),
        'heater': heater_on
    })

if __name__ == '__main__':
    t = threading.Thread(target=simulate_temperature)
    t.daemon = True
    t.start()

    app.run(debug=True)
