# Medical Data Visualizer

**Completed**: 8/01/25

**Part Of** FreeCodeCamp's Data Analysis with Python Certification.

This project uses Python, Pandas, Matplotlib, and Seaborn to read and clean medical data from a CSV file, and visualize key health indicators using categorical plots and heatmaps.

## Project Description:

Create functions called draw_cat_plot() and draw_heat_map() in medical_data_visualizer.py to process and visualize a dataset of medical information. The functions clean the data, generate a plot (categorical) of health features across target classes such as glucose and cholesterol, and create a heatmap showing the correlation of said health features.

The project answers questions such as:

- How do cholesterol, glucose, smoking, alcohol, and activity levels differ between people with and without cardiovascular disease?
- What are the correlations between different health measurements (BMI, age, blood pressure)?

## Guidelines:

- **Input**: A CSV file with medical data (medical_examination.csv)
- **Output**: Two plots (catplot.png and heatmap.png);
    - Catplot is a categorical plot which shows the distributions of health features split by cardiovasuclar disease.
    - Heatmap.png is a heatmap that displays the correlation between different health metrics like height, weight, and blood pressure.
- **Steps taken**:
    -  Add an 'overweight' column using BMI
    -  Normalizing cholesterol and glucose values
    -  Data Cleaning
    -  Reshaping data into long format using pd.melt() for categorical plotting
    -  Use sns.catplot() and sns.heatmap() for final visualizations
 

## Technologies used:
- Python
- Pandas
- Seaborn
- Matplotlib
- VSCode / Gitpod (Starter Boilerplate)

## How to Run:
- Install Python & required libraries:
    - Matplotlib, Seaborn, and Pandas
- Place medical_examination.csv in the same directory
- Run the script by typing python (or python3) main.py

## License:
- This project is licensed under The Unlicense. You are free to use, modify, and distribute this project with no restrictions. See the LICENSE file for more information.
