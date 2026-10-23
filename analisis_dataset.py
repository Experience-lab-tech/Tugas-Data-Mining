
import pandas as pd

df = pd.read_csv("reviews.csv")

print("=== INFORMASI DATASET ===")
print("Jumlah baris:", df.shape[0])
print("Jumlah kolom:", df.shape[1])
print("\nSepuluh data pertama:")
print(df.head(10).to_string())

print("\n=== TIPE DATA SETIAP KOLOM ===")
print(df.dtypes)

print("\n=== JENIS DATA ===")
print("Data kategorikal: version")
print("Data teks: review")
print("Data numerikal: rating, thumbs_up")
print("Data temporal: date")

print("\n=== JUMLAH NULL ===")
print(df.isnull().sum())

print("\nTotal nilai null:", df.isnull().sum().sum())

print("\n=== PERSENTASE NULL ===")
print((df.isnull().mean() * 100).round(2))

print("\n=== DATA DUPLIKAT ===")
print("Jumlah baris duplikat:", df.duplicated().sum())

print("\n=== JUMLAH DATA UNIK ===")
print(df.nunique(dropna=True))

df["date"] = pd.to_datetime(df["date"], errors="coerce")

print("\n=== TIPE DATA SETELAH PERUBAHAN ===")
print(df.dtypes)

print("\n=== PEMERIKSAAN OUTLIER THUMBS_UP ===")

kolom = "thumbs_up"

Q1 = df[kolom].quantile(0.25)
Q3 = df[kolom].quantile(0.75)
IQR = Q3 - Q1

batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR

outlier = df[
    (df[kolom] < batas_bawah) |
    (df[kolom] > batas_atas)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Batas bawah:", batas_bawah)
print("Batas atas:", batas_atas)
print("Jumlah kandidat outlier:", len(outlier))


print("\nTABEL DISTRIBUSI RATING ULASAN")

distribusi = df["rating"].value_counts().sort_index()
total = len(df)

garis = "+--------+----------------+--------------+"

print(garis)
print("| Rating | Jumlah Ulasan  | Persentase   |")
print(garis)

for rating, jumlah in distribusi.items():
    persen = jumlah / total * 100

    print(
        f"| {rating:^6} "
        f"| {jumlah:>14,} "
        f"| {persen:>11.2f}% |"
    )

print(garis)
print(
    f"| {'Total':<6} "
    f"| {total:>14,} "
    f"| {100.00:>11.2f}% |"
)
print(garis)


print("\n=== PEMERIKSAAN REVIEW ===")
print("Nilai review null:", df["review"].isnull().sum())
print(
    "Review kosong atau hanya spasi:",
    df["review"].fillna("").str.strip().eq("").sum()
)

tanggal = pd.to_datetime(df["date"], errors="coerce")
print("\n=== PEMERIKSAAN TANGGAL ===")
print("Tanggal tidak valid:", tanggal.isnull().sum())

print("\n=== FREKUENSI VERSION ===")
print(df["version"].value_counts(dropna=False).head(15))
