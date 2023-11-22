import tkinter as tk
from tkinter import messagebox
from sympy import *

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng hỗ trợ học tập môn giải tích")
        
        # Tạo các button cho các chức năng
        self.button1 = tk.Button(root, text="Tính tích phân", command=self.open_integral)
        self.button1.pack()

        self.button2 = tk.Button(root, text="Tính giới hạn", command=self.open_limit)
        self.button2.pack()

        self.button3 = tk.Button(root, text="Tính đạo hàm", command=self.open_derivative)
        self.button3.pack()

    def open_integral(self):
        # Mở cửa sổ phụ cho chức năng tính tích phân
        sub_window = tk.Toplevel(self.root)
        sub_window.title("Tính tích phân")

        # Thiết lập phần tử trong cửa sổ phụ cho tính tích phân

        # Tạo khung nhập hàm
        function_label = tk.Label(sub_window, text="Nhập hàm:")
        function_label.pack()

        function_entry = tk.Entry(sub_window)
        function_entry.pack()

        # Tạo khung nhập giới hạn tích phân
        lower_limit_label = tk.Label(sub_window, text="Giới hạn dưới:")
        lower_limit_label.pack()

        lower_limit_entry = tk.Entry(sub_window)
        lower_limit_entry.pack()

        upper_limit_label = tk.Label(sub_window, text="Giới hạn trên:")
        upper_limit_label.pack()

        upper_limit_entry = tk.Entry(sub_window)
        upper_limit_entry.pack()

        # Tạo nút tính tích phân
        calculate_button = tk.Button(sub_window, text="Tính tích phân", command=lambda: self.calculate_integral(sub_window, function_entry.get(), lower_limit_entry.get(), upper_limit_entry.get()))
        calculate_button.pack()

        # Tạo nút "Back"
        back_button = tk.Button(sub_window, text="Back", command=sub_window.destroy)
        back_button.pack()

    def calculate_integral(self, sub_window, function, lower_limit, upper_limit):
        try:
            x = symbols('x')
            integral = integrate(function, (x, float(lower_limit), float(upper_limit)))
            messagebox.showinfo("Kết quả", f"Kết quả tích phân là: {integral}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")

    def open_limit(self):
        # Mở cửa sổ phụ cho chức năng tính giới hạn
        sub_window = tk.Toplevel(self.root)
        sub_window.title("Tính giới hạn")

        # Thiết lập phần tử trong cửa sổ phụ cho tính giới hạn

        # Tạo khung nhập hàm
        function_label = tk.Label(sub_window, text="Nhập hàm:")
        function_label.pack()

        function_entry = tk.Entry(sub_window)
        function_entry.pack()

        # Tạo khung nhập điểm tiến tới
        point_label = tk.Label(sub_window, text="Điểm tiến tới:")
        point_label.pack()

        point_entry = tk.Entry(sub_window)
        point_entry.pack()

        # Tạo nút tính giới hạn
        calculate_button = tk.Button(sub_window, text="Tính giới hạn", command=lambda: self.calculate_limit(sub_window, function_entry.get(), point_entry.get()))
        calculate_button.pack()

        # Tạo nút "Back"
        back_button = tk.Button(sub_window, text="Back", command=sub_window.destroy)
        back_button.pack()

    def calculate_limit(self, sub_window, function, point):
        try:
            x = symbols('x')
            limit = limit(function, x, float(point))
            messagebox.showinfo("Kết quả", f"Kết quả giới hạn là: {limit}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")

    def open_derivative(self):
        # Mở cửa sổ phụ cho chức năng tính đạo hàm
        sub_window =tk.Toplevel(self.root)
        sub_window.title("Tính đạo hàm")

        # Thiết lập phần tử trong cửa sổ phụ cho tính đạo hàm

        # Tạo khung nhập hàm
        function_label = tk.Label(sub_window, text="Nhập hàm:")
        function_label.pack()

        function_entry = tk.Entry(sub_window)
        function_entry.pack()

        # Tạo nút tính đạo hàm
        calculate_button = tk.Button(sub_window, text="Tính đạo hàm", command=lambda: self.calculate_derivative(sub_window, function_entry.get()))
        calculate_button.pack()

        # Tạo nút "Back"
        back_button = tk.Button(sub_window, text="Back", command=sub_window.destroy)
        back_button.pack()

    def calculate_derivative(self, sub_window, function):
        try:
            x = symbols('x')
            derivative = diff(function, x)
            messagebox.showinfo("Kết quả", f"Kết quả đạo hàm là: {derivative}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")

# Tạo giao diện chính
root = tk.Tk()
main_gui = MainGUI(root)

root.mainloop()
