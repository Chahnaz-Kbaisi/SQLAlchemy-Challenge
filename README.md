# SQLAlchemy - Surfs Up!

![surfs-up.png](Images/surfs-up.png)

Planning a long holiday vacation in Honolulu, Hawaii! A climate analysis was generated to help with your trip planning.

## Step 1 - [Climate Analysis and Exploration](https://github.com/Chahnaz-Kbaisi/SQLAlchemy-Surfs-Up/blob/main/climate_starter.ipynb)

Python and SQLAlchemy were used to perform basic analysis and data exploration of the climate database. All of the following analyses were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* A start date and end date was chosen for the trip, the vacation range was approximately 3-15 days total.

* A connection to sqlite database was made using SQLAlchemy `create_engine`.

* SQLAlchemy `automap_base()` was used to reflect the tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* A query was designed to retrieve the last 12 months of precipitation data.

* Only the `date` and `prcp` values were selected.

* The query results were loaded into a Pandas DataFrame and the index was set to the date column.

* The DataFrame values were sorted by `date`.

* The results were plotted using the DataFrame `plot` method.

  ![precipitation](https://github.com/Chahnaz-Kbaisi/SQLAlchemy-Surfs-Up/blob/main/Images/precipitation_data.png)

* Pandas was used to print the summary statistics for the precipitation data.

### Station Analysis

* A query was designed to calculate the total number of stations.

* A query was designed to find the most active stations.

  * The stations and observation counts were listed in descending order.

  * A station with the highest number of observations was identified.

* A query was designed to retrieve the last 12 months of temperature observation data (TOBS).

  * Filtration by the station with the highest number of observations was performed.

  * The results were plotted as a histogram with `bins=12`.

    ![station-histogram](https://github.com/Chahnaz-Kbaisi/SQLAlchemy-Surfs-Up/blob/main/Images/station_temp_observation.png)

- - -

## Step 2 - [Climate App](https://github.com/Chahnaz-Kbaisi/SQLAlchemy-Surfs-Up/blob/main/climate_app.py)

After the initial analysis, a Flask API was designed based on the queries developed.

* Flask was used to create the routes.

### Routes

* `/`

  * Home page.

  * List of all routes that are available.

* `/api/v1.0/precipitation`

  * The query results were converted to a dictionary using `date` as the key and `prcp` as the value.

  * The JSON representation returned as a dictionary.

* `/api/v1.0/stations`

  * A JSON list of stations was returned from the dataset.

* `/api/v1.0/tobs`
  * A query of the dates and temperature observations of the most active station for the last year of data was generated.
  
  * A JSON list was returned of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
- - -

## The following analysis were also performed:

1. Temperature Analysis I

   * The average temperature was identified in June at all stations across all available years in the dataset.

   * The t-test was used to determine whether the difference in the means, if any, was statistically significant. 

2. Temperature Analysis II

   * The `calc_temps` function was used to calculate the min, avg, and max temperatures for the trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

   * The min, avg, and max temperature were plotted from the previous query as a bar chart.

   * The average temperature was used as the bar height.
    
3. Daily Rainfall Average

   * The rainfall per weather station was calculated using the previous year's matching dates.

   * The daily normals were calculated. Normals are the averages for the min, avg, and max temperatures.

   * The function called `daily_normals` was used to calculate the daily normals for a specific date. 

   * A list of dates was created for the trip in the format `%m-%d`. The `daily_normals` function was used to calculate the normals for each date string and append the results to a list.

   * The list of daily normals was loaded into a Pandas DataFrame and the index was set equal to the date.
