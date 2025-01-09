# Enerji Tüketim Takip Sistemi

Bu proje, enerji tüketimini takip etme, analiz etme ve optimizasyon önerileri sunma amacını taşır. Python, pandas, matplotlib, tkinter ve sklearn gibi çeşitli kütüphaneler kullanılarak geliştirilmiştir. Proje, cihazların günlük enerji tüketimini, maliyetini, karbon emisyonunu ve tasarruf önerilerini hesaplamayı sağlar. Ayrıca, geçmiş verilere dayalı tahminler yaparak gelecekteki enerji tüketimini tahmin eder.

## İçerik

1. **Veri İşleme ve Hesaplamalar**:
   - Enerji tüketim verileri (günlük tüketim, çalışma süresi vb.)
   - Saatlik tüketim hesaplama
   - Günlük ve aylık maliyet hesaplama
   - Verimlilik artırımı ile tasarruf hesaplama
   - Karbon emisyonu hesaplama
   - Karbon telafi için ağaç sayısı hesaplama

2. **Veri Analizi**:
   - Günlük toplam enerji tüketimi analizi
   - Cihaz bazında enerji tüketim oranlarının hesaplanması
   - Gerçek zamanlı izleme (simülasyon)
   - Eşik değerine göre uyarı sistemi
   - Optimizasyon önerileri

3. **Tahmin ve Modelleme**:
   - Basit bir lineer regresyon modeli kullanarak geçmiş verilere dayalı tüketim tahminleri yapılır.

4. **Veri Görselleştirme**:
   - Cihaz bazında günlük enerji tüketimi grafiği
   - Tarih bazında toplam enerji tüketimi grafiği
   - Geçmiş ve tahmin edilen enerji tüketimi grafiği
   - Cihaz tüketim oranlarının pasta grafiği

5. **Kullanıcı Arayüzü (GUI)**:
   - Tkinter kullanılarak basit bir kullanıcı arayüzü oluşturulmuştur. Kullanıcılar:
     - Raporu görüntüleyebilir.
     - Grafiklere erişebilir.
     - Zamanlama yapabilirler.

## Kullanıcı Arayüzü Özellikleri

- **Raporu Göster**: Verilerin özetini içeren bir rapor gösterir.
- **Grafikleri Göster**: Cihaz bazında günlük enerji tüketimi grafiği gösterir.
- **Zamanlama Yap**: Analizlerin her gün sabah 8:00'de yapılacağı bilgisini verir.

## Nasıl Çalışır?

1. **Veri Seti**: `Cihaz`, `Günlük Tüketim (kWh)`, `Çalışma Süresi (Saat)`, `Tarih` gibi verilerle başlatılır.
2. **Hesaplamalar**: Tüketim, maliyet, tasarruf, karbon emisyonu ve ağaç telafi hesaplamaları yapılır.
3. **Tahmin ve Modelleme**: Geçmiş verilere dayalı enerji tüketim tahminleri yapılır.
4. **Grafikler ve Raporlar**: Kullanıcı, analizleri görsel olarak inceleyebilir.
5. **GUI Kullanımı**: Tkinter tabanlı basit bir arayüz ile kullanıcı etkileşimi sağlanır.

## Gerekli Kütüphaneler

Bu projeyi çalıştırabilmek için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- pandas
- matplotlib
- numpy
- sklearn
- tkinter

Yüklemek için şu komutları kullanabilirsiniz:

```bash
pip install pandas matplotlib numpy scikit-learn
```

## Rapor Çıktıları

Proje sonunda, enerji tüketim verileri ve analizler içeren bir CSV raporu oluşturulur. Bu rapor, cihaz bazında günlük tüketim, maliyet, karbon emisyonu, ağaç telafi sayısı gibi bilgileri içerir.

## Kullanım

1. **Veri Girişi**: Cihazlar ve günlük enerji tüketimleri gibi veriler sisteme girilir.
2. **Hesaplama ve Analiz**: Sistemdeki enerji tüketimi hesaplanır ve optimizasyon önerileri sunulur.
3. **Grafikler**: Enerji tüketimi ve tahmin sonuçları görsel olarak gösterilir.
4. **Raporlama**: Detaylı bir rapor oluşturulup CSV dosyasına kaydedilir.

## Sonuç

Bu sistem, enerji tüketimini optimize etmeye yardımcı olur, maliyetleri düşürür, karbon ayak izini azaltır ve çevresel etkileri telafi etmek için öneriler sunar.
