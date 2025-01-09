import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Enerji tüketim verileri
data = {
    'Cihaz': ['Tufting Makinesi', 'Büküm Makinesi', 'Kesme Makinesi', 'Yıkama Makinesi'],
    'Günlük Tüketim (kWh)': [120, 80, 60, 150],
    'Çalışma Süresi (Saat)': [10, 8, 6, 12],
    'Tarih': [datetime.date(2025, 1, i) for i in range(1, 5)]
}

# Veri çerçevesi oluşturma
df = pd.DataFrame(data)

# Saatlik tüketim hesaplama
df['Saatlik Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] / df['Çalışma Süresi (Saat)']

# Elektrik birim fiyatı (TL/kWh)
unit_price = 2.0  # Örnek birim fiyat

# Günlük maliyet hesaplama
df['Günlük Maliyet (TL)'] = df['Günlük Tüketim (kWh)'] * unit_price

# %10 verimlilik artırımı ile tasarruf hesaplama
df['Tasarruflu Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] * 0.9
df['Tasarruf (kWh)'] = df['Günlük Tüketim (kWh)'] - df['Tasarruflu Tüketim (kWh)']
df['Tasarruflu Maliyet (TL)'] = df['Tasarruflu Tüketim (kWh)'] * unit_price
savings = df['Günlük Maliyet (TL)'].sum() - df['Tasarruflu Maliyet (TL)'].sum()

# Günlük karbon emisyonu hesaplama (kg CO₂/kWh)
carbon_emission_factor = 0.5  # Örnek emisyon faktörü (kg CO₂/kWh)
df['Karbon Emisyonu (kg CO₂)'] = df['Günlük Tüketim (kWh)'] * carbon_emission_factor

# Karbon telafi hesaplama (örneğin, ağaç dikimi)
tree_absorption = 22  # Bir ağacın yıllık absorbe ettiği CO₂ miktarı (kg)
df['Telafi İçin Ağaç Sayısı'] = (df['Karbon Emisyonu (kg CO₂)'] / tree_absorption).apply(np.ceil)

# Aylık tahmini tüketim ve maliyet hesaplama
df['Aylık Tahmini Tüketim (kWh)'] = df['Günlük Tüketim (kWh)'] * 30
df['Aylık Tahmini Maliyet (TL)'] = df['Aylık Tahmini Tüketim (kWh)'] * unit_price

# Toplam enerji tüketimi içinde cihaz oranları
df['Tüketim Oranı (%)'] = (df['Günlük Tüketim (kWh)'] / df['Günlük Tüketim (kWh)'].sum()) * 100

# Eşik değeri belirleme ve uyarı sistemi
threshold = 100  # kWh
df['Uyarı'] = df['Günlük Tüketim (kWh)'].apply(lambda x: 'Yüksek Tüketim!' if x > threshold else 'Normal')

# Günlük toplam enerji tüketimini tarih bazında analiz etme
df['Tarih'] = pd.to_datetime(df['Tarih'])
daily_usage = df.groupby('Tarih')['Günlük Tüketim (kWh)'].sum()

# Gerçek zamanlı izleme (Simülasyon)
real_time_data = np.random.randint(50, 150, size=len(df))
df['Gerçek Zamanlı Tüketim (kWh)'] = real_time_data

# Geçmiş verilerden tahmin (Basit lineer regresyon)
dates = np.arange(len(daily_usage)).reshape(-1, 1)
consumptions = daily_usage.values.reshape(-1, 1)
model = LinearRegression().fit(dates, consumptions)
future_dates = np.arange(len(daily_usage), len(daily_usage) + 5).reshape(-1, 1)
future_predictions = model.predict(future_dates)

# Optimizasyon önerileri
df['Optimizasyon Önerisi'] = df['Günlük Tüketim (kWh)'].apply(
    lambda x: 'Çalışma süresi azaltılabilir.' if x > threshold else 'Düşük tüketim, uygun!'
)

# Görselleştirme: Cihaz bazında tüketim
plt.figure(figsize=(10, 6))
plt.bar(df['Cihaz'], df['Günlük Tüketim (kWh)'], color='skyblue')
plt.xlabel('Cihaz')
plt.ylabel('Günlük Tüketim (kWh)')
plt.title('Günlük Enerji Tüketimi (Cihaz Bazında)')
plt.show()

# Görselleştirme: Tarih bazında toplam tüketim
plt.figure(figsize=(10, 6))
plt.plot(daily_usage.index, daily_usage.values, marker='o', color='orange')
plt.xlabel('Tarih')
plt.ylabel('Toplam Tüketim (kWh)')
plt.title('Günlük Toplam Enerji Tüketimi')
plt.grid(True)
plt.show()

# Görselleştirme: Gelecek tahmin
plt.figure(figsize=(10, 6))
plt.plot(daily_usage.index, daily_usage.values, label='Geçmiş Tüketim', marker='o')
plt.plot(pd.date_range(daily_usage.index[-1], periods=6, freq='D')[1:], future_predictions, label='Tahmin Edilen Tüketim', linestyle='--')
plt.xlabel('Tarih')
plt.ylabel('Tüketim (kWh)')
plt.title('Geçmiş ve Tahmin Edilen Enerji Tüketimi')
plt.legend()
plt.grid(True)
plt.show()

# Görselleştirme: Cihaz tüketim oranları
plt.figure(figsize=(10, 6))
plt.pie(df['Tüketim Oranı (%)'], labels=df['Cihaz'], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Cihaz Tüketim Oranları')
plt.show()

# Konsol çıktıları
print("\nCihaz Tüketim Analizi:")
print(df[['Cihaz', 'Günlük Tüketim (kWh)', 'Günlük Maliyet (TL)', 'Karbon Emisyonu (kg CO₂)', 'Uyarı', 'Telafi İçin Ağaç Sayısı', 'Optimizasyon Önerisi']])

print(f"\nVerimlilik artırımı ile günlük toplam tasarruf miktarı: {savings:.2f} TL")

print("\nAylık Tahmini Tüketim ve Maliyet:")
print(df[['Cihaz', 'Aylık Tahmini Tüketim (kWh)', 'Aylık Tahmini Maliyet (TL)']])

print("\nGelecek Tüketim Tahminleri:")
for i, pred in enumerate(future_predictions.flatten(), 1):
    print(f"Gün {i}: {pred:.2f} kWh")

# Verileri CSV olarak kaydetme
df.to_csv('enerji_tuketim_raporu.csv', index=False)
print("\nRapor başarıyla 'enerji_tuketim_raporu.csv' dosyasına kaydedildi!")

# Kullanıcı Arayüzü (GUI)
def show_summary():
    messagebox.showinfo("Rapor", df.to_string(index=False))

def plot_summary():
    plt.figure(figsize=(10, 6))
    plt.bar(df['Cihaz'], df['Günlük Tüketim (kWh)'], color='skyblue')
    plt.xlabel('Cihaz')
    plt.ylabel('Günlük Tüketim (kWh)')
    plt.title('Günlük Enerji Tüketimi (Cihaz Bazında)')
    plt.show()

def schedule_analysis():
    messagebox.showinfo("Zamanlama", "Analizler günlük olarak sabah 8:00'de yapılacaktır.")

root = tk.Tk()
root.title("Enerji Tüketim Takip Sistemi")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

summary_button = ttk.Button(frame, text="Raporu Göster", command=show_summary)
summary_button.grid(row=0, column=0, pady=5)

plot_button = ttk.Button(frame, text="Grafikleri Göster", command=plot_summary)
plot_button.grid(row=1, column=0, pady=5)

schedule_button = ttk.Button(frame, text="Zamanlama Yap", command=schedule_analysis)
schedule_button.grid(row=2, column=0, pady=5)

root.mainloop()
