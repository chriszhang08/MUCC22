import pandas as pd

class Customer:
    def __init__(self, id, region, category, company):
        self.id = id
        self.region = region
        self.category = category
        self.marketValue = 0
        self.quantity = 0
        self.isws = company

# %%
WScustomers = pd.read_csv('WSCustomerKey.csv')
listWSCustomers = []
for i in range(len(WScustomers)):
    listWSCustomers.append(Customer(WScustomers.iloc[i][0], WScustomers.iloc[i][1],
                                    WScustomers.iloc[i][2], True))

# %%
HHCustomers = pd.read_csv('HHCustomerKey.csv')
listHHCustomers = []
for i in range(len(HHCustomers)):
    listHHCustomers.append(Customer(HHCustomers.iloc[i][0], HHCustomers.iloc[i][1],
                                    HHCustomers.iloc[i][2], False))


# %%
WSsales = pd.read_csv('WSSales.csv')
for i in range(len(WSsales)):
    # calculate the total sales of each customer
    saleValue = WSsales.iloc[i][2] * WSsales.iloc[i][4]
    for j in range(len(listWSCustomers)):
        if listWSCustomers[j].id == WSsales.iloc[i][3]:
            listWSCustomers[j].marketValue += saleValue
            listWSCustomers[j].quantity += WSsales.iloc[i][4]

#%%
HHSales = pd.read_csv('HHSales.csv')
for i in range(len(HHSales)):
    # calculate the total sales of each customer
    saleValue = HHSales.iloc[i][2] * HHSales.iloc[i][4]
    for j in range(len(listHHCustomers)):
        if listHHCustomers[j].id == HHSales.iloc[i][3]:
            listHHCustomers[j].marketValue += saleValue
            listHHCustomers[j].quantity += HHSales.iloc[i][4]

# %%
# dictionary of each region and its total sales
dictRegion = {
    'West Coast': [0,0],
    'Mid-West': [0,0],
    'Southeast': [0,0],
    'Northeast': [0,0],
}
for i in range(len(listWSCustomers)):
    dictRegion[listWSCustomers[i].region][0] += listWSCustomers[i].quantity
    dictRegion[listWSCustomers[i].region][1] += listWSCustomers[i].marketValue

# %%
# iterate through the dictionary and print the results
for key, value in dictRegion.items():
    print(key, value)

#%%
# find the most profitable customer
maxValue = 0
for i in range(len(listWSCustomers)):
    if listWSCustomers[i].marketValue > maxValue:
        maxValue = listWSCustomers[i].marketValue
        maxCustomer = listWSCustomers[i].id


#%%
# count how many customers both have in common
customerShared = 0
for i in range(len(listWSCustomers)):
    for j in range(len(listHHCustomers)):
        if listWSCustomers[i].id == listHHCustomers[j].id:
            customerShared += 1
            # pop the customer from the list
            listHHCustomers.pop(j)
            break

#%%
# find total sales in each region after two lists merge
# skip customers that are in the WS list
for i in range(len(listHHCustomers)):
    if listHHCustomers[i].region == 'Pacific':
        dictRegion['West Coast'][0] += listHHCustomers[i].quantity
        dictRegion['West Coast'][1] += listHHCustomers[i].marketValue
    elif listHHCustomers[i].region == 'Midwest':
        dictRegion['Mid-West'][0] += listHHCustomers[i].quantity
        dictRegion['Mid-West'][1] += listHHCustomers[i].marketValue
    else:
        dictRegion[listHHCustomers[i].region][0] += listHHCustomers[i].quantity
        dictRegion[listHHCustomers[i].region][1] += listHHCustomers[i].marketValue