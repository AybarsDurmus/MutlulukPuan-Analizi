import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('c:/Users/aybar/Downloads/World Happiness Report 2022.csv')
print(data)

print(data.head())

print(data.info())

print(data.isnull().sum())

print(data.describe())

data = data.dropna()  # Eksik verileri kaldırma

# Alternatif: Ortalama ile doldurma
data['Happiness score'] = data['Happiness score'].fillna(data['Happiness score'].mean())

#Happiness score'un histogram grafiğini çizdirir
sns.histplot(data['Happiness score'], kde=True, bins=20)
plt.title('Happiness score Dağılımı')
plt.show()

#Happiness score'un en yüksek olduğu 10 ülkeyi gösterir
top_countries = data.sort_values(by='Happiness score', ascending=False).head(10)
sns.barplot(x='Happiness score', y='Country', data=top_countries)
plt.title('En Yüksek Happiness score\'a Sahip 10 Ülke')
plt.show()

# X ve Y eksenlerini tanımlıyoruz
x = data['Explained by: GDP per capita']  
y = data['Happiness score']  

# Dağılım grafiğini oluştur
plt.scatter(x, y, color='blue', alpha=0.7)  

# Grafiği düzenle
plt.title('Happiness score ve Kişi Başına Düşen GSYH İlişkisi')  # Başlık
plt.xlabel('Explained by: GDP per capita')  # X ekseni etiketi
plt.ylabel('Happiness score')  # Y ekseni etiketi

# Grafiği göster
plt.show()

columns_to_include = ['Explained by: GDP per capita', 'Happiness score']  
correlation = data[columns_to_include].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasyon Matrisi')
plt.show()
#Korelasyon katsayısının 0.74 çıkması iki değişken arasında güçlü bir pozitif ilişki olduğunu gösterir. 

# X ve Y eksenlerini tanımlayın
x = data['Explained by: Social support']  
y = data['Happiness score']  

# Dağılım grafiğini oluştur
plt.scatter(x, y, color='blue', alpha=0.7)  

plt.title('Happiness score ve Explained by: Social support')  # Başlık
plt.xlabel('Explained by: Social support')  # X ekseni etiketi
plt.ylabel('Happiness score')  # Y ekseni etiketi

# Grafiği göster
plt.show()

columns_to_include = ['Explained by: Social support', 'Happiness score']  
correlation = data[columns_to_include].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasyon Matrisi')
plt.show()
#Korelasyon katsayısının 0.78 çıkması iki değişken arasında güçlü bir pozitif ilişki olduğunu gösterir.

# X ve Y eksenlerini tanımlayın
x = data['Explained by: Healthy life expectancy']  
y = data['Happiness score']  

# Dağılım grafiğini oluştur
plt.scatter(x, y, color='blue', alpha=0.7)  

plt.title('Happiness score ve Explained by: Healthy life expectancy')  # Başlık
plt.xlabel('Explained by: Healthy life expectancy')  # X ekseni etiketi
plt.ylabel('Happiness score')  # Y ekseni etiketi

# Grafiği göster
plt.show()

columns_to_include = ['Explained by: Healthy life expectancy', 'Happiness score']  
correlation = data[columns_to_include].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasyon Matrisi')
plt.show()
#Korelasyon katsayısının 0.74 çıkması iki değişken arasında güçlü bir pozitif ilişki olduğunu gösterir.


x = data['Explained by: Freedom to make life choices']  
y = data['Happiness score']  

# Dağılım grafiğini oluştur
plt.scatter(x, y, color='blue', alpha=0.7)  

plt.title('Happiness score ve Explained by: Freedom to make life choices')  # Başlık
plt.xlabel('Explained by: Freedom to make life choices')  # X ekseni etiketi
plt.ylabel('Happiness score')  # Y ekseni etiketi

# Grafiği göster
plt.show()

columns_to_include = ['Explained by: Freedom to make life choices', 'Happiness score']  
correlation = data[columns_to_include].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasyon Matrisi')
plt.show()
#Korelasyon katsayısının 0.62 çıkması iki değişken arasında orta düzey bir pozitif ilişki olduğunu gösterir.


x = data['Explained by: Generosity']  
y = data['Happiness score']  

# Dağılım grafiğini oluştur
plt.scatter(x, y, color='blue', alpha=0.7)  

plt.title('Happiness score ve Explained by: Generosity')  # Başlık
plt.xlabel('Explained by: Generosity')  # X ekseni etiketi
plt.ylabel('Happiness score')  # Y ekseni etiketi

# Grafiği göster
plt.show()

columns_to_include = ['Explained by: Generosity', 'Happiness score']  
correlation = data[columns_to_include].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasyon Matrisi')
plt.show()
#Korelasyon katsayısının 0.064 çıkması iki değişken arasında çok zayıf bir pozitif ilişki olduğunu gösterir.


x = data['Explained by: Perceptions of corruption']  
y = data['Happiness score']  

# Dağılım grafiğini oluştur
plt.scatter(x, y, color='blue', alpha=0.7)  

plt.title('Happiness score ve Explained by: Perceptions of corruption')  # Başlık
plt.xlabel('Explained by: Perceptions of corruption')  # X ekseni etiketi
plt.ylabel('Happiness score')  # Y ekseni etiketi

# Grafiği göster
plt.show()

columns_to_include = ['Explained by: Perceptions of corruption', 'Happiness score']  
correlation = data[columns_to_include].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasyon Matrisi')
plt.show()
#Korelasyon katsayısının 0.42 çıkması iki değişken arasında zayıf bir pozitif ilişki olduğunu gösterir.