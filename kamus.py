meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "IDK": "Saya tidak tau",
            "OTW": "Sedang diperjalanan",
            "OMG": "Oh tuhan ku"
            }
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!):")
    if word in meme_dict.keys():
        print(meme_dict[word])
        # Apa yang harus kita lakukan jika kata itu ditemukan?
    else:
        print('kata tidak diketemukan')
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
