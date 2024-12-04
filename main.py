# add_two_numbers_gui.py

import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        sum_result = num1 + num2
        messagebox.showinfo("结果", f"{num1} 和 {num2} 的和是: {sum_result}")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字！")

# 创建主窗口
root = tk.Tk()
root.title("计算两数之和")

# 创建输入框和标签
tk.Label(root, text="第一个数:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="第二个数:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# 创建计算按钮
calculate_button = tk.Button(root, text="计算", command=calculate_sum)
calculate_button.grid(row=2, column=0, columnspan=2)

# 运行主循环
root.mainloop()
