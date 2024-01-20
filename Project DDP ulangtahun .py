import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime, timedelta

def hitung_ulang_tahun():
    # mengambil data tanggal lahir
    birthday_date = entry_lahir.get_date()

    # mendapatkan tanggal hari ini
    today_date = datetime.now().date()

    # hitung perbedaan hari
    if today_date > birthday_date.replace(year=today_date.year):
        next_birthday = birthday_date.replace(year=today_date.year + 1)
    else:
        next_birthday = birthday_date.replace(year=today_date.year)


    sisa_hari_ultah = (next_birthday - today_date).days

    if sisa_hari_ultah > 0:
        pesan = f"Ulang tahun mu {sisa_hari_ultah} lagi"
    else:
        pesan = "Hari ini Ulang tahun mu!!! Selamat Ulang Tahun!!!"

    # meng-update label dengan hasil
    result_label.config(text=pesan)

# membuat window
app = tk.Tk()
app.title("Birthday Countdown App")

# membuat widgets
label_instructions = tk.Label(app, text="Pilih tanggal lahir kamu:")
label_instructions.pack(pady=10, padx=50)

entry_lahir = DateEntry(app, width=12, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
entry_lahir.pack(pady=10)

button_calculate = tk.Button(app, text="Hitung", command=hitung_ulang_tahun)
button_calculate.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)


app.mainloop()
