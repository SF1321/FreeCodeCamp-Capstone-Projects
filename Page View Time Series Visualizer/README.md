# Page View Time Series Visualizer

**Completed**: 8/07/25

**Part Of** FreeCodeCamp's Data Analysis with Python Certification.

This project uses Python, Pandas, Matplotlib, and Seaborn to read and clean forum page view data from a CSV file, then generate visualizations to explore time-based trends and distributions in page visits.

## Project Description:

Create three functions (draw_line_plot(), draw_bar_plot(), draw_box_plot()) in the file time_series_visualizer.py to process and visualize a dataset of forum page views over time. Said functions produce a line chart to show long term viewing trends, a bar chart for monthly averages grouped by year, and box plots to reveal trends and seasonality in the data given

The project answers questions such as:

- How have page views on the FreeCodeCamp forum changed over time?
- How do the monthly averages across the years compare with each other?
- What seasonal patterns can be seen across months or years?

## Guidelines:

- **Input**: A CSV file with medical data (fcc-forum-pageviews.csv)
- **Output**: Three plots (line_plot.png, bar_plot.png and box_plot.png);
    - line_plot: A line chart showing daily page views over time.
    - bar_plot: A bar chart displaying average monthly page viewes per year.
    - box_plot: Two box plots - one showing year-wise distributions, and one showing month-wise distributions.
- **Steps taken**:
    - Import and parse the time series data
    - Clean outliers using quantile filtering (2.5%-97.5%)
    - Create a line plot to visualize long-term daily trends
    - Create a bar plot by grouping monthly averages by year
    - Create two box plots to show trends by year and seasonality by month 

## Technologies used:
- Python
- Pandas
- Seaborn
- Matplotlib
- VSCode / Gitpod (Starter Boilerplate)

## How to Run:
- Install Python & required libraries:
    - Matplotlib, Seaborn, and Pandas
    - NOTE: You may have to either upgrade seaborn or downgrade your Num.py to 1.23 make it work.
- Place fcc-forum-pageviews.csv in the same directory
- Run the script by typing python (or python3) main.py

## License:
- This project is licensed under The Unlicense. You are free to use, modify, and distribute this project with no restrictions. See the LICENSE file for more information.
