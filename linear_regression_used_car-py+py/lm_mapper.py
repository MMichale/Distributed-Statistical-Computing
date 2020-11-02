#!/usr/bin/env python3
import sys
import re
import pandas as pd
import numpy as np
import warnings
import csv
warnings.filterwarnings("ignore")


data = pd.DataFrame()

next(sys.stdin)
reader = csv.reader(sys.stdin)
for line in reader:
    try:
        assert len(line)==66
        data = data.append([line],ignore_index=True)
    except:
        continue

# print(data.shape) #cols 66
# print(data)

# 1 back_legroom
data[1] = data[1].str.split().str[0] # can get nan
data.loc[data[1].isnull(), 1] = 0
data[1] = data[1].replace('--', 0)
data[1] = data[1].astype('float')
data.rename(columns={1: 'back_legroom'}, inplace=True)

# 5 body_type make 10 category cols +10
data.loc[data[5]=='', 5] = 'Unknown'
data.rename(columns={5: 'body_type'}, inplace=True)
data['body_type_SUV/Crossover'],data['body_type_Sedan'],data['body_type_Pickup Truck'],data['body_type_Coupe'],data['body_type_Hatchback'],data['body_type_Minivan'],data['body_type_Wagon'],data['body_type_Van'],data['body_type_Convertible'],data['body_type_Unknown'] = 0,0,0,0,0,0,0,0,0,0
data['body_type_SUV/Crossover'] = data['body_type'].str.contains('SUV / Crossover').astype(int)
data['body_type_Sedan'] = data['body_type'].str.contains('Sedan').astype(int)
data['body_type_Pickup Truck'] = data['body_type'].str.contains('Pickup Truck').astype(int)
data['body_type_Coupe'] = data['body_type'].str.contains('Coupe').astype(int)
data['body_type_Hatchback'] = data['body_type'].str.contains('Hatchback').astype(int)
data['body_type_Minivan'] = data['body_type'].str.contains('Minivan').astype(int)
data['body_type_Wagon'] = data['body_type'].str.contains('Wagon').astype(int)
data['body_type_Van'] = data['body_type'].str.contains('Van').astype(int)
data['body_type_Convertible'] = data['body_type'].str.contains('Convertible').astype(int)
data['body_type_Unknown'] = data['body_type'].str.contains('Unknown').astype(int)
# franchise_make_dummy = pd.get_dummies(data['franchise_make'],prefix='franchise_make')
# data= pd.concat([data, franchise_make_dummy], axis=1)

# 8 city_fuel_economy
data.loc[data[8]=='', 8] = 0
data[8] = data[8].astype('float')
data.rename(columns={8: 'city_fuel_economy'}, inplace=True)

# 10 daysonmarket
data.loc[data[10]=='', 10] = 0
data[10] = data[10].astype('int')
data.rename(columns={10: 'daysonmarket'}, inplace=True)

# 12 Description

# 13 engine_cylinders cols-1+2
data['engine_type'] = data[13].str.extract('(\w)')[0]
data['enging_number'] = data[13].str.extract('(\d+)')[0]
data.loc[data['engine_type'].isnull(), 'engine_type'] = 'Unknown'
data.loc[data['enging_number'].isnull(), 'enging_number'] = 0
data['enging_number'] = data['enging_number'].astype(int)
data.drop(columns=13, inplace=True)

# engine_type 6 cat cols +6
data['engine_type_I'],data['engine_type_V'],data['engine_type_H'],data['engine_type_Unknown'],data['engine_type_W'],data['engine_type_R'] = 0,0,0,0,0,0
data['engine_type_I'] = data['engine_type'].str.contains('I').astype(int)
data['engine_type_V'] = data['engine_type'].str.contains('V').astype(int)
data['engine_type_H'] = data['engine_type'].str.contains('H').astype(int)
data['engine_type_Unknown'] = data['engine_type'].str.contains('Unknown').astype(int)
data['engine_type_W'] = data['engine_type'].str.contains('W').astype(int)
data['engine_type_R'] = data['engine_type'].str.contains('R').astype(int)

# 14 engine_displacement
data.loc[data[14]=='', 14] = 0
data[14] = data[14].astype('float')
data.rename(columns={14: 'engine_displacement'}, inplace=True)


# 16 exterior_color
data.loc[data[16].str.contains('Black|White|Gray'), 16] = 1
data.loc[data[16] != 1, 16] = 0
data[16] = data[16].astype('int')
data.rename(columns={16: 'exterior_color'}, inplace=True)

# 19 franchise_dealer T/F to 1/0
data.rename(columns={19: 'franchise_dealer'}, inplace=True)
data['franchise_dealer'] = data['franchise_dealer'].astype(bool).astype(int)

# 20 franchise_make 
# too many category, only have 10 cols +10
data.loc[data[20]=='', 20] = 'Unknown'
data.rename(columns={20: 'franchise_make'}, inplace=True)
data['franchise_make_Ford'],data['franchise_make_Chevrolet'],data['franchise_make_Jeep'],data['franchise_make_Toyota'],data['franchise_make_Hyundai'],data['franchise_make_Kia'],data['franchise_make_BMW'],data['franchise_make_Honda'],data['franchise_make_Nissan'],data['franchise_make_Mercedes-Benz']= 0,0,0,0,0,0,0,0,0,0
data['franchise_make_Ford'] = data['franchise_make'].str.contains('Ford').astype(int)
data['franchise_make_Chevrolet'] = data['franchise_make'].str.contains('Chevrolet').astype(int)
data['franchise_make_Jeep'] = data['franchise_make'].str.contains('Jeep').astype(int)
data['franchise_make_Toyota'] = data['franchise_make'].str.contains('Toyota').astype(int)
data['franchise_make_Hyundai'] = data['franchise_make'].str.contains('Hyundai').astype(int)
data['franchise_make_Kia'] = data['franchise_make'].str.contains('Kia').astype(int)
data['franchise_make_BMW'] = data['franchise_make'].str.contains('BMW').astype(int)
data['franchise_make_Honda'] = data['franchise_make'].str.contains('Honda').astype(int)
data['franchise_make_Nissan'] = data['franchise_make'].str.contains('Convertible').astype(int)
data['franchise_make_Mercedes-Benz'] = data['franchise_make'].str.contains('Mercedes-Benz').astype(int)

# 21 front_legroom
data[21] = data[21].str.split().str[0]
data.loc[data[21].isnull(), 21] = 0
data[21] = data[21].replace('--', 0)
data[21] = data[21].astype('float')
data.rename(columns={21: 'front_legroom'}, inplace=True)

# 22 fuel_tank_volume
data[22] = data[22].str.split().str[0]
data.loc[data[22].isnull(), 22] = 0
data[22] = data[22].replace('--', 0)
data[22] = data[22].astype('float')
data.rename(columns={22: 'fuel_tank_volume'}, inplace=True)

# 23 fuel_type 8 category cols +8
data.loc[data[23]=='', 23] = 'Unknown'
data.rename(columns={23: 'fuel_type'}, inplace=True)

data['fuel_type_Gasoline'],data['fuel_type_Flex Fuel Vehicle'],data['fuel_type_Unknown'],data['fuel_type_Hybrid'],data['fuel_type_Diesel'],data['fuel_type_Electric'],data['fuel_type_Biodiesel'],data['fuel_type_Compressed Natural Gas']= 0,0,0,0,0,0,0,0
data['fuel_type_Gasoline'] = data['fuel_type'].str.contains('Gasoline').astype(int)
data['fuel_type_Flex Fuel Vehicle'] = data['fuel_type'].str.contains('Flex Fuel Vehicle').astype(int)
data['fuel_type_Unknown'] = data['fuel_type'].str.contains('Unknown').astype(int)
data['fuel_type_Hybrid'] = data['fuel_type'].str.contains('Hybrid').astype(int)
data['fuel_type_Diesel'] = data['fuel_type'].str.contains('Diesel').astype(int)
data['fuel_type_Electric'] = data['fuel_type'].str.contains('Electric').astype(int)
data['fuel_type_Biodiesel'] = data['fuel_type'].str.contains('Biodiesel').astype(int)
data['fuel_type_Compressed Natural Gas'] = data['fuel_type'].str.contains('Compressed Natural Gas').astype(int)

# 24 has_accidents 3 cat cols +3
data.loc[data[24]=='',24]='Unknown'
data.rename(columns={24: 'has_accidents'}, inplace=True)

data['has_accidents_True'],data['has_accidents_False'],data['has_accidents_Unknown']=0,0,0
data['has_accidents_True'] = data['has_accidents'].str.contains('True').astype(int)
data['has_accidents_False'] = data['has_accidents'].str.contains('False').astype(int)
data['has_accidents_Unknown'] = data['has_accidents'].str.contains('Unknown').astype(int)

# 25 height
data[25] = data[25].str.split().str[0]
data.loc[data[25].isnull(),25]=0
data[25] = data[25].replace('--',0)
data[25]=data[25].astype('float')
data.rename(columns={25: 'height'}, inplace=True)

# 26 highway_fuel_economy
data.loc[data[26]=='',26]=0
data[26] = data[26].astype('float')
data.rename(columns={26: 'highway_fuel_economy'}, inplace=True)

# 28 interior_color
data.loc[data[28].str.contains('Black|White|Gray'),28]=1 
data.loc[data[28]!=1,28]=0
data[28] = data[28].astype(int)
data.rename(columns={28: 'interior_color'}, inplace=True)

# 29 isCab 3 cat cols +3
data.loc[data[29]=='',29]='Unknown'
data.rename(columns={29: 'isCab'}, inplace=True)
data['isCab_True'],data['isCab_False'],data['isCab_Unknown']=0,0,0
data['isCab_True'] = data['isCab'].str.contains('True').astype(int)
data['isCab_False'] = data['isCab'].str.contains('False').astype(int)
data['isCab_Unknown'] = data['isCab'].str.contains('Unknown').astype(int)

# 32 is_new
data.rename(columns={32: 'is_new'}, inplace=True)
data['is_new'] = data['is_new'].astype(bool).astype(int)

# 35 length
data[35] = data[35].str.split().str[0]
data.loc[data[35].isnull(),35]=0
data[35] = data[35].replace('--',0)
data[35]=data[35].astype('float')
data.rename(columns={35: 'length'}, inplace=True)

# 36 listed_date
data[36] = pd.to_datetime(data[36])
data[36] = 2020 - data[36].dt.year 
data.rename(columns={36: 'listed_date'}, inplace=True)

# 41 major_option

# 43 maximum_seating
data[43] = data[43].str.split().str[0]
data.loc[data[43].isnull(),43]=0
data[43] = data[43].replace('--',0)
data[43]=data[43].astype('float')
data.rename(columns={43: 'maximum_seating'}, inplace=True)

# 44 mileage
data.loc[data[44]=='',44]=0
data[44] = data[44].astype(float)
data.rename(columns={44: 'mileage'}, inplace=True)

# 46 owner_count
data.loc[data[46]!=1,46] = 0
data[46] = data[46].astype(int)
data.rename(columns={46: 'owner_count'}, inplace=True)

# 47 Power

# 48 price
data.loc[data[48]=='',48]=0
data[48] = data[48].astype(float)
data.rename(columns={48: 'price'}, inplace=True)

# 51 seller_rating
data.loc[data[51]=='',51]=0
data[51] = data[51].astype(float)
data.rename(columns={51: 'seller_rating'}, inplace=True)

# 55 Torque

# 56 transmission 5 cat cols +5
data.loc[data[56]=='',56]='Unknown'
data.rename(columns={56: 'transmission'}, inplace=True)

data['transmission_A'],data['transmission_CVT'],data['transmission_M'],data['transmission_Unknown'],data['transmission_Dual Clutch']= 0,0,0,0,0
data['transmission_A'] = data['transmission'].str.contains('A').astype(int)
data['transmission_CVT'] = data['transmission'].str.contains('CVT').astype(int)
data['transmission_M'] = data['transmission'].str.contains('M').astype(int)
data['transmission_Unknown'] = data['transmission'].str.contains('Unknown').astype(int)
data['transmission_Dual Clutch'] = data['transmission'].str.contains('Dual Clutch').astype(int)

# 61 wheel_system 6 cat cols +6
data.loc[data[61]=='',61]='Unknown'
data.rename(columns={61: 'wheel_system'}, inplace=True)

data['wheel_system_AWD'] = data['wheel_system'].str.contains('AWD').astype(int)
data['wheel_system_FWD'] = data['wheel_system'].str.contains('FWD').astype(int)
data['wheel_system_4WD'] = data['wheel_system'].str.contains('4WD').astype(int)
data['wheel_system_Unknown'] = data['wheel_system'].str.contains('Unknown').astype(int)
data['wheel_system_RWD'] = data['wheel_system'].str.contains('RWD').astype(int)
data['wheel_system_4X2'] = data['wheel_system'].str.contains('4X2').astype(int)

# 63 wheelbase
data[63] = data[63].str.split().str[0]
data.loc[data[63].isnull(),63]=0
data[63] = data[63].replace('--',0)
data[63]=data[63].astype('float')
data.rename(columns={63: 'wheelbase'}, inplace=True)

# 64 width
data[64] = data[64].str.split().str[0]
data.loc[data[64].isnull(),64]=0
data[64] = data[64].replace('--',0)
data[64]=data[64].astype('float')
data.rename(columns={64: 'width'}, inplace=True)



# print(data.shape) # 118 cols
cols = list(data.columns)
new_cols = [i for i in cols if isinstance(i,str)]
# # print(new_cols)
# # some cols need del, because it has dummy
# # 'body_type','franchise_make','fuel_type','has_accidents','isCab','transmission','wheel_system','engine_type'
new_cols.remove('body_type')
new_cols.remove('franchise_make')
new_cols.remove('fuel_type')
new_cols.remove('has_accidents')
new_cols.remove('isCab')
new_cols.remove('transmission')
new_cols.remove('wheel_system')
new_cols.remove('engine_type')
new_cols.remove('price')
new_cols.append('price')
data = data[new_cols]
# print('{0}\t{1}'.format(data.shape[0], data.shape[1])) # cols 73
# print(data.info())
n = data.shape[0]
p = data.shape[1] - 1 # 73-1=72
y = data['price'].values
x = data.iloc[:,:72].values
xy = np.dot(x.T,y)
xx = np.dot(x.T,x)
xy = xy.tolist()
xx = xx.reshape((1,p**2))[0].tolist()
res = xx + xy
print("\t".join(str(i) for i in res))
