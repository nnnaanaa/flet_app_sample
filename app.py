import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        # 入力欄から値を取得し、数値に変換
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        
        # 数値の合計を計算
        total = num1 + num2 + num3
        
        # 合計をラベルに表示
        result_label.config(text=f"合計: {total}")
    except ValueError:
        # 数値以外の入力があった場合にエラーメッセージを表示
        messagebox.showerror("エラー", "全ての入力欄に有効な数値を入力してください")

# メインウィンドウの作成
root = tk.Tk()
root.title("合計計算アプリ")

sv = tk.StringVar()

# 入力欄の作成
entry1 = tk.Entry(root, textvariable=sv)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

# 各入力欄を画面に配置
entry1.pack(padx=10, pady=10, expand=False, fill=tk.BOTH, ipady=0, ipadx=0, side=tk.LEFT)
entry2.pack(padx=10, pady=10, expand=False, fill=tk.BOTH, ipady=0, ipadx=0, side=tk.LEFT)
entry3.pack(padx=10, pady=10, expand=False, fill=tk.BOTH, ipady=0, ipadx=0, side=tk.LEFT)

# 計算ボタンの作成
calc_button = tk.Button(root, text="計算", command=calculate_sum)
calc_button.pack(padx=10, pady=10)

# 結果表示用ラベルの作成
result_label = tk.Label(root, text="合計: ")
result_label.pack(padx=10, pady=10, fill=tk.BOTH, ipady=0, expand=False)

# メインループの開始
root.mainloop()
