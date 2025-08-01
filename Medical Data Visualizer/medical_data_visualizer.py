import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 (reading and parsing in the csv file)
df = pd.read_csv('medical_examination.csv', skipinitialspace=True)

# 2 (making a new overweight column)
df['overweight'] = ((df['weight'] / ((df['height'] / 100))**2) > 25).astype(int)

# 3(normalizing both the cholesterol and gluc columns [making evverthing 1's and 0's])
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5 (melting the data and creating a new df out of it)
    df_cat = pd.melt(df, 
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 
                                 'active', 'overweight'])


    # 6 (grouping and reformatting the data)
    df_cat = df_cat.groupby(['cardio', 'variable', 
                             'value']).size().reset_index(name = 'total')
    

    # 7
    
    
    # 8 (making a catplot using seaborn)
    fig = sns.catplot(data = df_cat,
                      kind = 'bar', x = 'variable', y = 'total', hue = 'value',
                      col = 'cardio').fig


    # 9 (saving and returning the catplot)
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11 (cleaning the data to use in the heatmap)
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12 (making a correlation matrix bsed off of the cleaned data)
    corr = df_heat.corr()

    # 13 (creating a mask for the upper triangle part of the heatmap)
    mask = np.triu(np.ones_like(corr, dtype = bool))



    # 14 (set up matplotlib figure [and make sure it can be visible])
    fig, ax = plt.subplots(figsize = (12,10))

    # 15 (drawing the actual heatmap)
    sns.heatmap(corr,
                mask = mask,
                annot = True,
                fmt = '.1f',
                center = 0,
                square = True,
                linewidths = .5,
                cbar_kws = {"shrink": .45, "format": '%.2f'})

    # 16
    fig.savefig('heatmap.png')
    return fig
