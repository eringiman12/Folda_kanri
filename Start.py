import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import filedialog
from tkinter import messagebox

import os

import os.path
import tkinter.filedialog
from turtle import color
# import openpyxl as excel
# import datetime
# import os
# import pathlib

import glob
# import numpy as np

from tkinter import *

# ファイルの参照処理
def click_refer_button():

   global Process_Naiyo
   f_path = ""
   f_path = filedialog.askdirectory(initialdir = dir)
   Oya_foldapath.insert(tkinter.END, f_path)
   # files = glob.glob(f_path + "/*")
   odd_lst = f_path.split("/")
   X_zahyo = 100;
   
   # スクロールXの値
   scroll_x = 0
   
   # スクロールｙの値
   scroll_y = 0
   
   # 順番処理の初期化
   i = 0
   
   File_name = "";
   
   # 5階層より深い場合はスクロールさせる
   if len(odd_lst) > 5:
      # xのスクロールバーウィジェットの作成
      bar_x = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)
      # ｘ位置指定
      bar_x.pack(side=tk.BOTTOM, fill=tk.X)
      # スクロールバーをcanvas配置で定義
      bar_x.config(command=canvas.xview)
      # スクロールバーの設定
      canvas.config(xscrollcommand=bar_x.set)
      # スクロール量代入
      scroll_x = len(odd_lst)
   
   # ファイル数の初期化
   File_Num = 0
   # ファイル数のマックス地の初期化
   Max_Num = 0

   # 参照したファイルリストの配列処理
   for item  in odd_lst:
       # ファイル名ボタンの定義
      File_btn = tk.Button(
         canvas,
         text=item,
         justify = tk.CENTER,
         bg='#005E54',
         foreground='white',
         width=17
      )
      
      # ファイルボックスの重なり順を一番下にする
      File_btn.lower()
      
      File_btn.bind("<Enter>", enter_bg)
      File_btn.bind("<Leave>", leave_bg)

      # ウィジェット作成
      canvas.create_window(X_zahyo, 20, window = File_btn)
      
      # Y座標地の初期化
      Y_zahyo = 45
      F_List = "";
      
      # ファイル名を追加していく
      if i > 0:
         File_name += "\\" + item
      else:
         File_name += item
      
      # サブフォルダ内を検索
      F_List = glob.glob(File_name + "/*")   
      
      # ファイルリスト配列の初期化
      File_lists = []
      # ファイル順に処理を行う
      for sub_f in F_List:
         # ファイル名ORフォルダ名のみファイルリスト配列に格納する
         File_lists.append(os.path.basename(sub_f))
      
      # 各フォルダのファイルパス
      File_Num = len(File_lists)   
      
      # ファイル + フォルダ　の数が一番多い列を検索する
      if File_Num > Max_Num:
         Max_Num = File_Num
      
      # 各階層のファイル名を入力ボックスに格納
      for sub_fitem in File_lists:
         # 入力ボックスをcanvasに定義
         sub_File_box = tk.Entry(canvas)
         # 入力ボックスにファイル名orフォルダ名を記載する 
         sub_File_box.insert(tkinter.END, os.path.basename(sub_fitem))
         # 入力ボックスの重なり順を最下層にする
         sub_File_box.lower()
         # 定義した入力ボックスをcanvasに配置
         canvas.create_window(X_zahyo, Y_zahyo, window = sub_File_box)
         Y_zahyo += 20
      
      # X座標に加算
      X_zahyo += 130
      i = i + 1 
   
   #　ファイルとフォルダ数の数が22を超えている列があれば
   #  スクロール追加
   if Max_Num > 22:
      bar_y = tk.Scrollbar(canvas, orient=tk.VERTICAL)
      bar_y.pack(side=tk.RIGHT, fill=tk.Y)
      bar_y.config(command=canvas.yview)
      canvas.config(yscrollcommand=bar_y.set)
      scroll_y = Max_Num
      
   # Canvasのスクロール範囲を設定
   canvas.config(scrollregion=(0, 0, scroll_x * 140, scroll_y * 22))   

   # messagebox.showerror("選択エラー",Max_Num)

# 親フォルダボタンにカーソルが乗った時
def enter_bg(event):
   event.widget['bg'] = 'white'
   event.widget['foreground'] = '#005E54'
   event.widget['troughcolor'] = '#005E54'

# 親フォルダボタンにカーソルが離れたとき
def leave_bg(event):
   event.widget['bg'] = '#005E54' 
   event.widget['foreground'] = 'white'
   
def on_mouse_down(event,it):
    messagebox.showerror("選択エラー",it)
       

### 選択インデックス取得関数
def get_index(event):
   # 
   Sub = tk.Tk() 
   Sub.title("編集フォーム")

   # 全体サイズ
   Sub.geometry('300x50')
    ### 選択インデックス取得
   index = event.widget.curselection()
   edit_box = tk.Entry(Sub) 
   edit_box.insert(tk.END, os.path.basename(event.widget.get(index)))
        
   Sub.mainloop()
   
#-------------------------------------------------#  
#-------------- 　  画面レイアウト   　-----------#   
#-------------------------------------------------# 
Process_Naiyo = ""
app = tk.Tk() 

# アプリタイトル
app.title("フォルダ・ファイル整理")
# 全体サイズ
app.geometry('1000x600')
# 背景色（）
app.config(bg="white")

# 処理内容ラベル
labelTop = tk.Label(
   app,
   text = "整理対象親フォルダを選択してください。",
   bg="white"
)
labelTop.place(relx=0.01, rely=0.1)   

# 選択されたフォルダの親パス 
Oya_foldapath = tk.Entry(
   app
) 
Oya_foldapath.place(relx=0.22, rely=0.1, relheight=0.05, relwidth=0.65) 


# # 参照ボタン
refer_button = ttk.Button(
   app,
   text=u'参照',
   command=click_refer_button,
   padding=0,
)
refer_button.place(relx=0.88, rely=0.095, relheight=0.06, relwidth=0.1) 

# canvas定義
canvas = tk.Canvas(
   app,
   bg="white",
)

# canvas配置
canvas.pack()
#キャンバスバインド
canvas.place(x=10, y=100,width=750, height=480)

# リサイズ禁止
app.resizable(0,0)
# アプリの描画
app.mainloop()