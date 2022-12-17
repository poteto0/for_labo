import numpy as np
import matplotlib.pyplot as plt

class AnimePlot:
    def __init__(self, path, w=5, h=5, xlim="nan", ylim ="nan"):
        self.path = path
        self.w = w
        self.h = h
        self.xlim = xlim
        self.ylim = ylim
        self.is_marked = False
        
    def set_color(self, colors):
        self.colors = colors
    
    def set_data(self, x_data, data_list):
        self.x = x_data
        self.data_list = data_list
    
    def set_marker(self, color="red", marker="o"):
        self.is_marked = True
        self.cm = color
        self.marker = marker
    
    def unset_marker(self):
        self.is_marked = False
        
    def plot_timelapse(self, interval=10):
        if len(self.colors) != len(self.data_list):
            print('\033[47m'+'\033[31m'+"エラー: colorとdataの長さが違います"+'\033[0m')
        else:
            if self.is_marked == False:
                print('\033[47m'+'\033[32m'+"注意: set_marker()でマーカーを設定できます"+'\033[0m')
            fig= plt.figure(figsize=(self.w, self.h))
        
            for i in range(0,len(self.x),interval):
                x_data = self.x[:i+1]
                j = 0
                for data in self.data_list:  
                    plot_data = data[:i+1]
                    plt.plot(x_data, plot_data, color=self.colors[j])
                    if self.is_marked:
                        plt.plot(self.x[i], data[i], color=self.cm, marker=self.marker)
                    j+=1
                if self.xlim != "nan":
                    plt.xlim(self.xlim)
                if self.ylim != "nan":
                    plt.ylim(self.ylim)
                
                try:
                    plt.savefig(f"{self.path}/plot_{i}.tiff")
                except:
                    print('\033[47m'+'\033[31m'+"エラー: pathを確認してください"+'\033[0m')
                    break
                plt.cla()
        
        
