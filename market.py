import pandas as pd

competitors = pd.read_csv('competitors.csv')
mvPacific = 0
mvMidwest = 0
mvSoutheast = 0
mvNortheast = 0
# iterate through the dataframe
# sum market value of only plant based burgertype
for row in competitors.itertuples():
    if row.BurgerType == 'PlantBased':
        mvPacific += row.Pacific
        mvMidwest += row.Midwest
        mvSoutheast += row.Southeast
        mvNortheast += row.Northeast

#%%
print(mvPacific)
print(mvMidwest)
print(mvSoutheast)
print(mvNortheast)