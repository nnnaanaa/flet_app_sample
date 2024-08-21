import tkinter as tk
from tkinter import messagebox
import time
import threading

# def calculate_sum():
#     try:
#         # 入力欄から値を取得し、数値に変換
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         num3 = float(entry3.get())
        
#         # 数値の合計を計算
#         total = num1 + num2 + num3
        
#         # 合計をラベルに表示
#         result_label.config(text=f"合計: {total}")
#     except ValueError:
#         # 数値以外の入力があった場合にエラーメッセージを表示
#         messagebox.showerror("エラー", "全ての入力欄に有効な数値を入力してください")

class TkApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("tkapp")

        # フレームの作成
        self.canvas = tk.Canvas(self.root)
        self.sample_frame_1 = tk.Frame(self.canvas)
        self.sample_frame_1.pack()

        # スクロールバー
        scrollbar = tk.Scrollbar(
            self.canvas, orient=tk.VERTICAL, command=self.canvas.yview
        )
        # スクロールの設定
        self.canvas.configure(scrollregion=(0, 0, 900, 900))
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # 諸々を配置
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Canvas上の座標(0, 0)に対してFrameの左上（nw=north-west）をあてがうように、Frameを埋め込む
        self.canvas.create_window((0, 0), window=self.sample_frame_1, anchor="nw", width=900, height=60)

        # ボタン領域
        tk.Button(self.sample_frame_1, text="非同期で実行", command=self.start_thread).pack(padx=10, pady=10, side=tk.LEFT)
        self.sample_label = tk.Label(self.sample_frame_1, text='停止中', width=10)
        self.sample_label.pack(side=tk.TOP)
 
        # 実行結果出力領域
        self.root.mainloop() # メインループの開始

    def threads_running(self):
        self.sample_label.config(text="実行中")
        for _ in range(10):
            print("Hello")
            current_dot_count = self.sample_label.cget("text").count("・")
            if current_dot_count != 3:
                self.sample_label.config(text=self.sample_label.cget("text") + "・")
            else:
                self.sample_label.config(text="実行中")
            
            time.sleep(1)

        self.sample_label.config(text="停止中")

    def start_thread(self):
        thread = threading.Thread(target=self.threads_running)
        thread.start()

# メインウィンドウの作成
tkapp = TkApp()