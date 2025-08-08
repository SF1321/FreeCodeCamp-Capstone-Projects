import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(15,7))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color = 'blue', 
                label = 'Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'],
                                             df['CSIRO Adjusted Sea Level'])
    
    years = pd.Series(range(1880,2051))
    
    plt.plot(years, (intercept + slope * (years)), 'r', label = 'Fit: 1880-2050')
    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]
    r_slope, r_intercept, _, _, _ = linregress(recent_df['Year'], 
                                               recent_df['CSIRO Adjusted Sea Level'])
    r_years = pd.Series(range(2000, 2051))
    plt.plot(r_years, (r_intercept + r_slope * (r_years)), 'green', label = 
                                                            'Fit: 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()