import pandas as pd

carac = pd.read_csv("carac.csv",sep=';')
lieux = pd.read_csv("lieux.csv",sep=';')
veh = pd.read_csv("veh.csv",sep=';')
vict = pd.read_csv("vict.csv",sep=';')

victime = vict.merge(veh,on=['Num_Acc','num_veh'])
accident = carac.merge(lieux,on = 'Num_Acc')

df = victime.merge(accident,on='Num_Acc')

hrmn=pd.cut(victime['hrmn'],24,labels=[str(i) for i in range(0,24)])