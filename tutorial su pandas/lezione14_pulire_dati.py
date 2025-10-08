import pandas as pd

df = pd.read_csv('pulizia.csv')
print(df)

new_df = df.dropna()
print(new_df.to_string())

df_filled_all = df.copy()
df_filled_all.fillna(130, inplace=True)
print(df_filled_all.to_string())

df_filled_cal_130 = df.copy()
df_filled_cal_130.fillna({"Calorie": 130}, inplace=True)
print(df_filled_cal_130.to_string())

df_mean = df.copy()
mean_cal = df_mean["Calorie"].mean()
df_mean.fillna({"Calorie": mean_cal}, inplace=True)
print(df_mean.to_string())

df_median = df.copy()
median_cal = df_median["Calorie"].median()
df_median.fillna({"Calorie": median_cal}, inplace=True)
print(df_median.to_string())

df_mode = df.copy()
mode_cal = df_mode["Calorie"].mode()[0]
df_mode.fillna({"Calorie": mode_cal}, inplace=True)
print(df_mode.to_string())

df['Data'] = pd.to_datetime(df['Data'], format='mixed', errors='coerce')
print(df.to_string())

df.dropna(subset=['Data'], inplace = True)

if 7 in df.index:
    df.loc[7, 'Durata'] = 45
    print("\n Modificato 'Durata' in riga 7 a 45")
else:
    print("\n Riga con indice 7 non presente dopo il dropna")
print(df.to_string())