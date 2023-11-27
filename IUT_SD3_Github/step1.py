import pandas as pd 

# Lire les fichiers CSV 
df_veh = pd.read_csv('veh.csv', sep=";", error_bad_lines=False) 
df_vict = pd.read_csv('vict.csv', sep=";", error_bad_lines=False) 
df_lieux = pd.read_csv('lieux.csv', sep=";", error_bad_lines=False) 
df_carac = pd.read_csv('carac.csv', sep=";", error_bad_lines=False) 

# Fusionner les fichiers 
df_merged = pd.merge(df_veh, df_vict, on='Num_Acc', how='outer') 
df_merged = pd.merge(df_merged, df_lieux, on='Num_Acc', how='outer') 
df_merged = pd.merge(df_merged, df_carac, on='Num_Acc', how='outer') 

# Enregistrer le DataFrame fusionné dans un nouveau fichier 
df_merged.to_csv('data/merged_data.csv', index=False)