    # Güncel Türkçe Sözlük'ten rastgele kelimeleri sesli olarak yazdıran programdır.
    # Copyright (C) 2022 libsoykan-dev

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os # Sistemde komutları çalıştırabilmek için gereklidir...

import random # Rastgele seçimlerden rastgele dosya adlarını tespit eder...

alfabe = ['a', 'b', 'c', 'ch', 'd', 'e', 'f', 'g', 'h', 'i', 'ih', 'j', 'k', 'l', 'm', 'n', 'o', 'oh', 'p', 'r', 's', 'sh', 't', 'u', 'uh', 'v', 'y', 'z']

oynatici = "mpv" # Ses oynatıcının komut yolu. Linux için "mpv" önerilir.

kararlilik = 0 # Sistemin kararlılığı. TDK'nin sitesinde harf başına kaç kelime düştüğünü tespit edemedim. Bundan ötürü kararlılık değişkeni gerekli. (0 ila 9 arasında tamsayı bir değer atanmalıdır, 0 önerilir)

def tdk(): # Bir "tdk" fonksiyonu tanımlar

    harf = random.choice(alfabe)  # "harf" değişkenine rastgele bir harf atar

    sayi = random.randint(0, (kararlilik * 1000 + 1000))  # "sayi" değişkenine, "karalilik" değişkenine bağlı rastgele bir doğal sayı ata

    # ***

    # TDK'nin ses dosyalarının isim formatı "a1.wav" değil de "a0001.wav" şeklinde olduğu için belli aralıktaki sayıların başına gereken miktarda sıfır ekleyen komutlar silsilesi...

    if sayi >= 0 and sayi <= 9:

        d = os.system(oynatici +  " https://sozluk.tdk.gov.tr/ses/" + harf + "000" + str(sayi) + ".wav")

    elif sayi >= 10 and sayi <= 99:

        d = os.system(oynatici +  " https://sozluk.tdk.gov.tr/ses/" + harf + "00" + str(sayi) + ".wav")

    elif sayi >= 100 and sayi <= 999:

        d = os.system(oynatici +  " https://sozluk.tdk.gov.tr/ses/" + harf + "0" + str(sayi) + ".wav")

    elif sayi >= 1000 and sayi <= 9999:

        d = os.system(oynatici +  " https://sozluk.tdk.gov.tr/ses/" + harf + str(sayi) + ".wav")

    # ***

    if d == 0: # Eğer komut başarıyla tamamlanırsa

        exit() # çık,

    else: # tamamlanmazsa

        return d # çıktıya d'yi ver.

cikis = tdk() # "cikis" değişkenine "tdk" fonksiyonunun çıktısını ata

while cikis == 512: # Fonksiyon olumsuz sonuçlanırken

    tdk() # "tdk" fonksiyonunu çalıştır
