# Dependencies
from flask import Flask, jsonify
import datetime as dt
from datetime import datetime, date, time
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Database setup, connection
connection_string = "sqlite:///Resources/hawaii.sqlite"
engine = create_engine(connection_string)

Base = automap_base()
Base.prepare(engine, reflect=True)

# Print all of the classes mapped to the Base
print(Base.classes.keys())

Measurement = Base.classes.measurement
Station = Base.classes.station


# Create app
app = Flask(__name__)

# List all routes that are available


@app.route("/")
def home():
    return """
        Available routes:<br/>
        /api/v1.0/percipitation<br/>
        /api/v1.0/stations<br/>
        /api/v1.0/tobs<br/>
        /api/v1.0/start=YYYY-MM-DD<br/>
        /api/v1.0/start=YYYY-MM-DD/end=YYYY-MM-DD;
    """
