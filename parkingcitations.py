import pandas
import numpy as np
pc = pandas.read_csv('Parking_Citations.csv', parse_dates = ['ViolDate'])
pc = pc[(pc['ViolDate'] < '2019-1-1')]
pc.to_csv('citations_bf_2019.csv')
meanfine = pc['ViolFine'].mean()
print(meanfine)

op = pc.loc[pc['OpenPenalty'] != 0,['OpenPenalty']]
print(op.quantile(.81))
pd = pc.loc[pc['PoliceDistrict'].notnull(),['ViolFine','PoliceDistrict']]
central= pd.loc[pd['PoliceDistrict'].isin(['Central', 'CENTRAL'])]
print(central.mean())
western= pd.loc[pd['PoliceDistrict'].isin(['Western','WESTERN'])]
northeast = pd.loc[pd['PoliceDistrict'].isin(['Northeastern','NORTHEASTERN'])]
eastern= pd.loc[pd['PoliceDistrict'].isin(['Eastern', 'EASTERN'])]
southeast= pd.loc[pd['PoliceDistrict'].isin(['Southeastern', 'SOUTHEASTERN'])]
southern = pd.loc[pd['PoliceDistrict'].isin(['Southern', 'SOUTHERN'])]
northwest = pd.loc[pd['PoliceDistrict'].isin(['Northwestern', 'NORTHWESTERN'])]
northern = pd.loc[pd['PoliceDistrict'].isin(['Northern', 'NORTHERN'])]
southwest = pd.loc[pd['PoliceDistrict'].isin(['Southwestern', 'SOUTHWESTERN'])]
print(western.mean())
print(northeast.mean())
print(eastern.mean())
print(southeast.mean())
print(southern.mean())
print(northwest.mean())
print(northern.mean())
print(southwest.mean())

vm = pc[(pc['ViolDate'] >= '2017-1-1') & (pc['ViolDate'] <= '2017-12-31')]
make = vm['Make']
mazda = make.str.contains('MAZD')
acura = make.str.contains('ACUR')
honda = make.str.contains('HOND')
toyota = make.str.contains('TOY')
nissan = make.str.contains('NISS')
chevr = make.str.contains('CHEV')
jeep = make.str.contains('JEEP')
lexus = make.str.contains('LEX')
chry = make.str.contains('CHRY')
volks = make.str.contains('VOL')
dodge = make.str.contains('DODG')
hyundai = make.str.contains ('HYUN')
subaru = make.str.contains('SUBA')
cadi = make.str.contains('CADI')
merz = make.str.contains('MER')
infi = make.str.contains('INFI')
buick = make.str.contains('BUIC')

vm['Make'] = np.where(mazda, 'MAZD', np.where(acura, 'ACURA', np.where(honda, 'HONDA', np.where(toyota, 'TOYOT',np.where(nissan, 'NISSA',np.where(chevr, 'CHEVR', np.where(jeep, 'JEEP',np.where(lexus, 'LEXUS', np.where(chry, 'CHRY',np.where(volks, 'VOLKS',np.where(dodge, 'DODG',np.where(hyundai, 'HYUN', np.where(subaru, 'SUBAR',np.where(cadi, 'CADI', np.where(merz, 'MERZ', np.where(buick, 'BUICK', np.where(infi, 'INFIN',make.str.replace('-', ' '))))))))))))))))))
print(vm.Make.value_counts())

hon= pc.loc[pc['Make'].isin(['HONDA','HON','HOND'])]
toy = pc.loc[pc['Make'].isin(['TOYOTA','TOYT','TOYOT','TOY'])]
acu= pc.loc[pc['Make'].isin(['ACU','ACURA','ACUR'])]
nis= pc.loc[pc['Make'].isin(['NISSAN','NISS','NISSA','NIS'])]
print((len(hon.index)+len(toy.index)+len(acu.index)+len(nis.index))/len(pc.index))

i = 0
num=[]
while i < 11:
    year = pc[(pc['ViolDate'] >= str(i+2004)+'-1-1') & (pc['ViolDate'] <= str(i+2004)+'-12-31')]
    num.append (len(year.index))
    print(num[i])
    i += 1
    
x = np.array([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]).reshape(-1,1)
y = np.array(num)
model = LinearRegression().fit(x,y)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
