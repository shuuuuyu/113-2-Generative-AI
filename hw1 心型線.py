# -*- coding: utf-8 -*-
"""師大科技117林書妤hw1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JAXxfn04Hbzv65BcqlaK6vNhuZFn2Q1K

# 作業:畫函數圖形

- 笛卡爾心型線：$ F = X^2 + Y^2 + aX - a\sqrt{X^2 + Y^2} $
- 搭配塗色
"""

# Commented out IPython magic to ensure Python compatibility.
"""
繪製出笛卡爾心型線圖形，並搭配塗色。
"""

# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = 0.5
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

F = X**2 + Y**2 + a*X - a*np.sqrt(X**2 + Y**2)

plt.figure(figsize=(6,6))
plt.contourf(X, Y, F, levels=50, cmap="coolwarm")
plt.contour(X, Y, F, levels=[0, 1, 2], colors='black')
plt.grid(True)
plt.show()
