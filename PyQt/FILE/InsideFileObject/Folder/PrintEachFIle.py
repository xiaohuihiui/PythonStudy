from tkinter import *
from tkinter.ttk import *
import os

class tree(object):
    def __init__(self, path):
        self.win = Tk()
        self.win.title("ウィンドウタイト")  # ウィンドウタイトルを設定
        self.tree = Treeview()  # Treeview（ツリー表示用ウィジェット）
        self.tree.heading("#0", text="file")  # ツリーのヘッダー名を "file" に設定
        self.tree.pack()  # ウィジェットをウィンドウに配置
        temppath = os.path.basename(path)  # 指定pathの最後のフォルダ名を取得
        treeF = self.tree.insert("", 0, text=temppath)  # ルートディレクトリを追加
        self.showtree(path, treeF)  # 再帰的にツリーを展開
        self.win.mainloop()  # GUIループ開始
    def showtree(self, path, root):
        filelist = os.listdir(path)  # 指定path配下のファイル・ディレクトリ一覧取得
        for filename in filelist:
         abspath = os.path.join(path, filename)  # 絶対パス作成
        # ツリーに項目を追加
         treeFinside = self.tree.insert(root, 0, text=filename, values=(abspath))
         if os.path.isdir(abspath):              # ディレクトリなら再帰呼び出し
            self.showtree(abspath, treeFinside)
tree(r"E:\GitCheck\EnglishLearnning")
