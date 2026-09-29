"""
Koden leser av sensor dataene og sammenligner med sensor informasjonen for å finne sensorer som trenger kalibrering. 
Resultatet lagres i en JSON-fil.
"""

import pandas as pd
import yaml
import json

# Leser konfigurasjonsfilen
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# Henter konfigurasjonsparametere
max_days = config["max_days_since_calibration"]
output_file = config["output_file"]

# Leser sensor data og sensor informasjon
sensor_data = pd.read_csv("calibrations.csv")
sensor_info = pd.read_excel("sensors.xlsx")

# Kombinerer sensor data og sensor informasjon basert på sensor_id
combined = sensor_data.merge(sensor_info, on="sensor_id")

# Filtrerer sensorer som trenger kalibrering basert på max_days
needs_calibration = combined[combined["days_since_calibration"] > max_days]

# Lagrer resultatet i en JSON-fil
records = needs_calibration.to_dict(orient="records")

with open(output_file, "w") as file:
    json.dump(records, file, indent=2)
