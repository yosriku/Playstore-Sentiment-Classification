# scraping_playstore.py

from google_play_scraper import app, reviews_all, Sort
import csv

# ID aplikasi-aplikasi yang ingin di-scrape
app_ids = ['com.bethsoft.falloutshelter', 'com.chillyroom.soulknightprequel','com.superplanet.evilhunter','com.chucklefish.stardewvalley', 'com.ChillyRoom.DungeonShooter' ]

# Membuka file CSV untuk menyimpan ulasan dari kedua aplikasi
with open('playstore_reviews_combined.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["App Name", "Review", "Rating", "Date", "Likes", "Review ID"])
    
    # Iterasi melalui setiap app_id
    for app_id in app_ids:
        # Mendapatkan detail aplikasi
        app_info = app(app_id)
        app_name = app_info['title']
        print(f"Scraping reviews for: {app_name}")
        
        # Mengambil semua ulasan (dapat memakan waktu jika datanya banyak)
        reviews = reviews_all(
            app_id,
            lang='id',  # Bahasa ulasan, 'id' untuk ulasan dalam bahasa Indonesia
            country='id',  # Negara, 'id' untuk Indonesia
            sort=Sort.MOST_RELEVANT,  # Menggunakan enum Sort untuk penyortiran
        )
        
        # Menyimpan setiap ulasan ke dalam file CSV
        for review in reviews:
            writer.writerow([app_name, review['content'], review['score'], review['at'], review['thumbsUpCount'], review['reviewId']])
        
        print(f"Scraping selesai untuk {app_name}. Total ulasan yang diambil: {len(reviews)}")

print("Data telah disimpan ke playstore_reviews_combined.csv")
