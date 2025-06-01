import pandas as pd 
df = pd.read_csv('investments_VC.csv')
print(df.info())

#Menghapus data yang kosng
df = df.dropna()


# Membersihkan kolom funding_total_usd
def hapus_koma(data):
    if data == ' -   ':
        return 1
    else:
        return int(data.replace(',', ''))
df[' funding_total_usd '] = df[' funding_total_usd '].apply(hapus_koma)

# #Mengelompokkan berdasarkan status dan membandingkan rata-rata fundingnya
grup = df.groupby( by = 'status')[' funding_total_usd '].mean()

print(grup)



