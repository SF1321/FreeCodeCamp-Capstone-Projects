# Demographic Data Visualizer

**Completed**: 7/29/25

**Part Of** FreeCodeCamp's Data Analysis with Python Certification.

This project uses Python and Pandas to read and analyze data from a CSV file, and calculates various statistics like race counts, average age, education levels, and income distributions across countries.

## Project Description:
Create a function called **calculate_demographic_data()** in **demographic_data_analyzer.py** that uses Pandas to analyze data from the adult.data.csv file. The function should store calculated statistics in ready-made variable to be printed out at the end of the function. Using Pandas, answer these questions:

- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
- What country has the highest percentage of people that earn >50K and what is that percentage?
- Identify the most popular occupation for those who earn >50K in India.

## Guidelines:

- **Input**: A CSV file with demographic data (adult.data.csv)
- **Output**: Printed out values, and returned values summarizing the demographics of the data.
- **Metrics**: Race count, Average age of men, Percentage of people with a Bachelor's Degree, Income Comparison by education level, Minimum work hours and high earners among them, Country with the highest Percentage of high earners, and Top occupation among high earners in India.

  
## Technologies used:
- Pandas
- Python
- VSCode / Gitpod (Starter Boilerplate)

## How to Run:
- Install Python & Pandas
- Make sure that adult.data.cav is in the same directory as script
- Run the script by typing python (or python3) main.py

## License:
- This project is licensed under The Unlicense. You are free to use, modify, and distribute this project with no restrictions. See the LICENSE file for more information.
