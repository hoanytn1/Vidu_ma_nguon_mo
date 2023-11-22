import pandas as pd

# Đường dẫn đến file CSV
file_path = "diemPython.csv"

# Đọc dữ liệu từ file CSV
df = pd.read_csv(file_path)

# Tính tỉ lệ các loại giỏi
total_students = df["Số SV"].sum()
excellent = df["Loại A+"].sum() + df["Loại A"].sum()
good = df["Loại B+"].sum() + df["Loại B"].sum()
average = df["Loại C+"].sum() + df["Loại C"].sum()
poor = df["Loại D+"].sum() + df["Loại D"].sum()
fail = df["Loại F"].sum()

excellent_percentage = (excellent / total_students) * 100
good_percentage = (good / total_students) * 100
average_percentage = (average / total_students) * 100
poor_percentage = (poor / total_students) * 100
fail_percentage = (fail / total_students) * 100

# Xếp hạng các lớp theo tỉ lệ loại A+
df["Tỉ lệ loại A+"] = (df["Loại A+"] / df["Số SV"]) * 100
df["Tỉ lệ loại A"] = (df["Loại A"] / df["Số SV"]) * 100
df["Tỉ lệ loại B+"] = (df["Loại B+"] / df["Số SV"]) * 100
df["Tỉ lệ loại B"] = (df["Loại B"] / df["Số SV"]) * 100
df["Tỉ lệ loại C+"] = (df["Loại C+"] / df["Số SV"]) * 100
df["Tỉ lệ loại C"] = (df["Loại C"] / df["Số SV"]) * 100
df["Tỉ lệ loại D+"] = (df["Loại D+"] / df["Số SV"]) * 100
df["Tỉ lệ loại D"] = (df["Loại D"] / df["Số SV"]) * 100
df["Tỉ lệ loại F"] = (df["Loại F"] / df["Số SV"]) * 100

# Sắp xếp và xếp hạng các lớp theo tỉ lệ loại A+
df_sorted = df.sort_values(by="Tỉ lệ loại A+", ascending=False)
df_sorted["Xếp hạng"] = range(1, len(df_sorted) + 1)

# In báo cáo tỉ lệ các loại giỏi
print("BÁO CÁO TỈ LỆ CÁC LOẠI GIỎI")
print(f"Tỉ lệ Loại A+: {excellent_percentage:.2f}%")
print(f"Tỉ lệ Loại A: {good_percentage:.2f}%")
print(f"Tỉ lệ Loại B+: {average_percentage:.2f}%")
print(f"Tỉ lệ Loại B: {poor_percentage:.2f}%")
print(f"Tỉ lệ Loại F: {fail_percentage:.2f}%")

# In báo cáo xếp hạng các lớp
print("\nBÁO CÁO XẾP HẠNG CÁC LỚP THEO TỈ LỆ LOẠI A+")
print(df_sorted[["Lớp Mã", "Số SV", "Tỉ lệ loại A+", "Xếp hạng"]])
