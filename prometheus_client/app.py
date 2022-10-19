import imp
from flask import Flask
from prometheus_client import Counter, generate_latest, Gauge
from random import randint

app = Flask(__name__)

temp_sensor_metric = Gauge(
        name="temperature",
        documentation="Temperature Sensor Guage",
        labelnames= ["unit", "sensor"]
    )

def read_temp():
    temp_sensor_metric.labels("a", "a1").set(randint(20, 60))
    temp_sensor_metric.labels("a", "a2").set(randint(20, 60))
    temp_sensor_metric.labels("a", "a3").set(randint(10, 60))
    temp_sensor_metric.labels("b", "b1").set(randint(10, 60))
    temp_sensor_metric.labels("b", "b2").set(randint(10, 60))
    temp_sensor_metric.labels("b", "b3").set(randint(20, 60))
    temp_sensor_metric.labels("c", "c1").set(randint(20, 60))
    temp_sensor_metric.labels("c", "c2").set(randint(20, 60))
    temp_sensor_metric.labels("c", "c3").set(randint(20, 60))

@app.route('/metrics')
def metrics():
    read_temp()
    return generate_latest()


if __name__ == "__main__":
    app.run(port=7080)
