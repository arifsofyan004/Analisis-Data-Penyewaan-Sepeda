from google.colab import drive
drive.mount('/content/drive')

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca data dari file CSV
df_day = pd.read_csv("/content/drive/MyDrive/Proyek Akhir Dicoding/day.csv", index_col="instant", parse_dates=["dteday"])
df_hour = pd.read_csv("/content/drive/MyDrive/Proyek Akhir Dicoding/hour.csv", index_col="instant", parse_dates=["dteday"])

# Judul Dashboard
st.title('Dashboard Analisis Data Sepeda')

# Sidebar
st.sidebar.subheader('Pilih Analisis Data')
analysis_choice = st.sidebar.radio("Pilih Analisis:", ('Tren Jumlah Sepeda per Jam', 'Rata-rata Sepeda Disewakan per Musim',
                                                       'Rata-rata Sepeda Disewakan per Bulan', 'Rata-rata Sepeda Disewakan per Hari dalam Seminggu',
                                                       'Rata-rata Sepeda Disewakan per Hari Libur vs. Hari Kerja'))

# Analisis Data
if analysis_choice == 'Tren Jumlah Sepeda per Jam':
    st.subheader('Tren Jumlah Sepeda per Jam')
    st.write("Ini adalah grafik yang menunjukkan tren jumlah sepeda disewakan per jam.")
    st.write("Grafik ini membagi data berdasarkan musim dan menggambarkan perubahan jumlah sepeda disewakan sepanjang hari.")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df_hour, x='hr', y='cnt', hue='season', palette='husl', linewidth=2.5, ax=ax)
    ax.set_title('Tren Jumlah Sepeda Disewakan per Jam')
    ax.set_xlabel('Jam (hr)')
    ax.set_ylabel('Jumlah Sepeda Disewakan')
    ax.legend(title='Musim', loc='upper right', labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    ax.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(fig)

elif analysis_choice == 'Rata-rata Sepeda Disewakan per Musim':
    st.subheader('Rata-rata Sepeda Disewakan per Musim')
    st.write("Ini adalah grafik yang menampilkan rata-rata jumlah sepeda disewakan untuk setiap musim.")
    data_per_musim = df_day.groupby('season')['cnt'].mean()
    nama_musim = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(nama_musim.values(), data_per_musim.values)
    ax.set_title('Rata-rata Jumlah Sepeda Disewakan Per Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Rata-rata Jumlah Sepeda Disewakan')
    ax.set_xticklabels(nama_musim.values(), rotation=15, ha='right')
    st.pyplot(fig)

elif analysis_choice == 'Rata-rata Sepeda Disewakan per Bulan':
    st.subheader('Rata-rata Sepeda Disewakan per Bulan')
    st.write("Ini adalah grafik yang menunjukkan rata-rata jumlah sepeda disewakan per bulan.")
    data_per_bulan = df_day.groupby('mnth')['cnt'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_per_bulan.index, data_per_bulan.values, marker='o', linestyle='-')
    ax.set_title('Jumlah Sepeda Disewakan Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Sepeda Disewakan')
    ax.grid(True)
    ax.set_xticks(data_per_bulan.index)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
    st.pyplot(fig)

elif analysis_choice == 'Rata-rata Sepeda Disewakan per Hari dalam Seminggu':
    st.subheader('Rata-rata Sepeda Disewakan per Hari dalam Seminggu')
    st.write("Ini adalah grafik yang menampilkan rata-rata jumlah sepeda disewakan per hari dalam seminggu.")
    data_per_hari = df_day.groupby('weekday')['cnt'].mean()
    nama_hari = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(nama_hari, data_per_hari.values)
    ax.set_title('Rata-rata Jumlah Sepeda Disewakan per Hari dalam Seminggu')
    ax.set_xlabel('Hari dalam Seminggu')
    ax.set_ylabel('Rata-rata Jumlah Sepeda Disewakan')
    ax.set_xticklabels(nama_hari, rotation=45)
    st.pyplot(fig)

elif analysis_choice == 'Rata-rata Sepeda Disewakan per Hari Libur vs. Hari Kerja':
    st.subheader('Rata-rata Sepeda Disewakan per Hari Libur vs. Hari Kerja')
    st.write("Ini adalah grafik yang menampilkan rata-rata jumlah sepeda disewakan per hari libur dan hari kerja.")
    data_hari_libur = df_day[df_day['holiday'] == 1]['cnt'].mean()
    data_hari_kerja = df_day[df_day['workingday'] == 1]['cnt'].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(['Hari Libur', 'Hari Kerja'], [data_hari_libur, data_hari_kerja])
    ax.set_title('Rata-rata Jumlah Sepeda Disewakan per Hari Libur vs. Hari Kerja')
    ax.set_xlabel('Jenis Hari')
    ax.set_ylabel('Rata-rata Jumlah Sepeda Disewakan')
    st.pyplot(fig)

# Bagian keterangan
st.sidebar.subheader('Kesimpulan dan Implikasi')
st.sidebar.write("**Conclusion Pertanyaan 1:** Bagaimana tren penyewaan sepeda berubah sepanjang tahun dan apa faktor-faktor yang paling memengaruhinya?")
st.sidebar.write("Dari analisis data yang telah dilakukan, kami dapat mengambil kesimpulan sebagai berikut:")
st.sidebar.write("- Tren penyewaan sepeda menunjukkan pola musiman yang kuat, dengan tingkat penyewaan yang lebih tinggi selama musim panas dan musim gugur.")
st.sidebar.write("- Faktor-faktor seperti musim, suhu, dan kondisi cuaca memiliki dampak signifikan pada tren penyewaan sepeda.")
st.sidebar.write("- Penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan dengan hari libur.")

st.sidebar.write("**Conclusion Pertanyaan 2:** Bagaimana pola musiman dalam penyewaan sepeda dapat membantu dalam pengambilan keputusan persediaan sepeda yang lebih efektif?")
st.sidebar.write("Pola Musiman dalam Penyewaan Sepeda:")
st.sidebar.write("- Musim Panas (Summer): Rata-rata Jumlah Sepeda Disewakan = 4992.33")
st.sidebar.write("- Musim Gugur (Fall): Rata-rata Jumlah Sepeda Disewakan = 5644.3")

st.sidebar.write("Pola Harian dalam Penyewaan Sepeda:")
st.sidebar.write("- Hari Kerja (Weekday): Rata-rata Jumlah Sepeda Disewakan = 4584.82")
st.sidebar.write("- Hari Libur (Weekend): Rata-rata Jumlah Sepeda Disewakan = 3735.0")

st.sidebar.write("**Implikasi:**")
st.sidebar.write("Selama musim panas dan musim gugur, permintaan sepeda mencapai puncaknya. Oleh karena itu, strategi persediaan sepeda harus ditingkatkan untuk memenuhi permintaan tinggi selama periode ini.")
st.sidebar.write("Pada hari kerja, jumlah sepeda yang disewakan lebih tinggi dibandingkan dengan hari libur. Hal ini menunjukkan adanya potensi peluang bisnis pada hari-hari kerja, dan perusahaan sebaiknya mempertimbangkan strategi pemasaran dan promosi khusus untuk menarik pelanggan pada hari-hari tersebut.")
st.sidebar.write("Analisis pola musiman ini memberikan wawasan yang berharga dalam perencanaan persediaan sepeda, memungkinkan perusahaan untuk mengoptimalkan inventarisasi mereka. Hal ini dapat menghindari ketidakseimbangan antara permintaan dan persediaan, yang pada akhirnya dapat meningkatkan kepuasan pelanggan dan efisiensi operasional.")
