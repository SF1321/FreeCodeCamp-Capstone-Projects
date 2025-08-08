# Sea Level Predictor

**Completed**: 8/08/25

**Part Of** FreeCodeCamp's Data Analysis with Python Certification.

This project uses Python, Pandas, Matplotlib, and SciPy to read hostroical sea level data from a CSV file, create regresssion models, and visualize predictions on how the sea level will rise through the year 2050.

## Project Description:

Create a function (draw_plot()) in sea_level_predictor.py that:
- Reads and processes the CSV file (epa-sea-level.csv) which contains global average sea levels since 1880.
- Generates a scatter plot of the historical measurements.
- Creates a line of best fit for all of the data points and projects it onward to 2050.
- Creates a second line of best fit using only data from 2000 onward and projects it to 2050.

The project answers questions such as:

- How have global sea levels changes since 1880?
- What is the projectsed sea level rise if historical trends continue?
- How does the post-2000 trends compare to the historical long term trends?

## Guidelines:

- **Input**: A CSV file with time series data (epa-sea-level.csv)
- **Output**: One plot file (sea_level_plot.png) which is a scatter plot of historical data points:
    - Red line: linear regression for all years (1880-2050).
    - Green line: linear regression for all years post-2000 (2000-2050)
- **Steps taken**:
    - Import and parse the sea level data
    - Create scatter plot of raw data with matplotlib
    - Perform linear regression on all the data (linregress from SciPy)
    - Predict and plot the long-term trend line through 2050
    - Label axes, title, and save the final figure as sea_level_plot.png 

## Technologies used:
- Python
- Pandas
- SciPy
- Matplotlib
- VSCode / Gitpod (Starter Boilerplate)

## How to Run:
- Install Python & required libraries:
    - Matplotlib, SciPy, and Pandas
- Place epa-sea-level.csv in the same directory
- Run the script by typing python (or python3) main.py

## License:
- This project is licensed under The Unlicense. You are free to use, modify, and distribute this project with no restrictions. See the LICENSE file for more information.
