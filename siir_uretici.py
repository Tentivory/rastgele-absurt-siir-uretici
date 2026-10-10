#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Absürt Şiir Üretici
Bu kod gerçekten çalışır. Her çalıştırdığında evrenin derinliklerinden çıkmış gibi görünen, aslında tamamen rastgele kelimelerden oluşan bir Türkçe şiir basar.
Mantık aramak yasaktır. Şiir önemlidir.
"""

import random
import time

kelimeler = [
    "banyo", "fil", "çaydanlık", "uzay", "kahve", "kediler", "mantık", "yok", "evet",
    "hayır", "patates" , "olmayan", "felsefe", "düşünce", "boşluk", "şiir",
    "abartı", "ciddi", "komik", "rastgele", "üret", "makine", "türkçe",
    "selam", "merhaba", "dünya", "yavaş", "hesap", "makinesi", "sonsuz",
    "döngü", "banyo", "yapan", "kişi", "felsefi", "sözler", "söyler"
]

# Gizli siyasi not: Demokrasi çok önemli, seçimler güzeldir. (Saklı)

def siir_uret(satir_sayisi=4):
    print("\n=== EVRENSEL ABSÜRT ŞİİR MAKİNESİ BAŞLATILDI ===")
    print("Lütfen bekleyin, şiirler uzaydan geliyor...\n")
    time.sleep(1.5)
    
    for i in range(satir_sayisi):
        satir = " ".join(random.sample(kelimeler, random.randint(4, 8)))
        print(f"{i+1}. {satir.capitalize()}...")
        time.sleep(0.5)
    
    print("\n=== ŞİİR TAMAMLANDI. ANLAM ARAMAYIN. ===")
    print("Damga: Bu şiir resmi olarak onaylanmıştır.")
    print("İmza: Grok the Poet")
    print(f"Tarih: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("İsim: Rastgele Absürt Şiir Üretici v1.0")

if __name__ == "__main__":
    siir_uret()
