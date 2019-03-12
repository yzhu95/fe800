import pandas as pd

df = pd.read_excel('raw_data.xlsx')

def get_data(year, features):
    data = df[df.iloc[:, 1] == features[0]].iloc[:, [0, year-2006]]
    data.columns = ['Ticker', features[0]]
    data.set_index('Ticker', inplace=True)
    
    for feature in features[1:]:
        data[feature] = df[df.iloc[:, 1] == feature].iloc[:, year-2006].values
    
    return data
#%%
year = 2010
features = [
        'TOTAL ASSETS', 
        'Cash & Equivalents',
        'Receivables - Total (Net)',
        'Inventories - Total',
        'Sales (Net)',
        'Cost of Good Sold',
        'GROSS PROFIT'
    ]

data = get_data(year, features)
#%%
universe = pd.read_csv('universe.csv', header=None)[0]
data = data.loc[universe]
#%%
data.to_csv('data.csv')