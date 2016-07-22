# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: learn1.py
@time: 2016/7/22 10:55
@contact: ustb_liubo@qq.com
@annotation: learn1
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='learn1.log',
                    filemode='a+')
from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 画出x,y 的曲线
x = np.linspace(0, 5, 10)
y = x ** 2

# figure()
# plot(x, y, 'r')
# xlabel('x')
# ylabel('y')
# title('title')
# show()
# # 使用不同的点表示曲线, [将两幅图画在一个图像里,使用subplot]
# subplot(1,2,1)
# plot(x, y, 'r--')
# subplot(1,2,2)
# plot(y, x, 'g*-')
# show()
#
# fig = plt.figure()
#
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
#
# axes.plot(x, y, 'r')
#
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
#
# show()
#
#
# fig = plt.figure()
# # 画布占整个图像的比例[可以在一个图像画多个画布,也可以在一个画布上添加另一个画布]
# axes1 = fig.add_axes([0.01, 0.01, 0.98, 0.98]) # main axes
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes
#
# # main figure
# axes1.plot(x, y, 'r')
# axes1.set_xlabel('x')
# axes1.set_ylabel('y')
# axes1.set_title('title')
#
# # insert
# axes2.plot(y, x, 'g')
# axes2.set_xlabel('y')
# axes2.set_ylabel('x')
# axes2.set_title('insert title')
# show()


# fig, axes = plt.subplots(nrows=2, ncols=4)
#
# for index_x in range(axes.shape[0]):
#     for index_y in range(axes.shape[1]):
#         ax = axes[index_x, index_y]
#         ax.plot(x, y, 'r')
#         ax.set_xlabel('x')
#         ax.set_ylabel('y')
#     ax.set_title('title')
#
# fig.tight_layout()
# show()
#
# fig.savefig("filename.png")
#
# fig.savefig("filename.png", dpi=200)
#
#
# ax.legend(["curve1", "curve2", "curve3"])
#
# ax.plot(x, x**2, label="curve1")
# ax.plot(x, x**3, label="curve2")
# ax.legend()
#
# ax.legend(loc=0) # let matplotlib decide the optimal location
# ax.legend(loc=1) # upper right corner
# ax.legend(loc=2) # upper left corner
# ax.legend(loc=3) # lower left corner
# ax.legend(loc=4) # lower right corner
#
#
# matplotlib.rcParams.update({'font.size': 24, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix', 'text.usetex': True})
# # 这样是定义了多个画布,可以任意添加(可以在一幅图中画出多条曲线)
# fig, ax = plt.subplots()
#
# ax.plot(x, x**2, 'r--', label="y = x**2")
# ax.plot(x, x**3, 'g*-', label="y = x**3")
# ax.legend(loc=2) # upper left corner
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_title('title')
#
# show()

# fig, ax = plt.subplots()
#
# ax.plot(x, x**2, label=r"$y = \alpha^2$")
# ax.plot(x, x**3, label=r"$y = \alpha^3$")
# ax.legend(loc=2) # upper left corner
# # 设置label的字体
# ax.set_xlabel(r'$\alpha$', fontsize=30)
# ax.set_ylabel(r'$y$', fontsize=30)
# ax.set_title('title')
# show()
#
# # 设置线的颜色,点的形状
# fig, ax = plt.subplots(figsize=(12,6))
#
# ax.plot(x, x+1, color="blue", linewidth=0.25)
# ax.plot(x, x+2, color="blue", linewidth=0.50)
# ax.plot(x, x+3, color="blue", linewidth=1.00)
# ax.plot(x, x+4, color="blue", linewidth=2.00)
#
# # possible linestype options ‘-‘, ‘--’, ‘-.’, ‘:’, ‘steps’
# ax.plot(x, x+5, color="red", lw=2, linestyle='-')
# ax.plot(x, x+6, color="red", lw=2, ls='-.')
# ax.plot(x, x+7, color="red", lw=2, ls=':')
#
# # custom dash
# line, = ax.plot(x, x+8, color="black", lw=1.50)
# line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...
#
# # possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
# ax.plot(x, x+ 9, color="green", lw=2, ls='--', marker='+')
# ax.plot(x, x+10, color="green", lw=2, ls='--', marker='o')
# ax.plot(x, x+11, color="green", lw=2, ls='--', marker='s')
# ax.plot(x, x+12, color="green", lw=2, ls='--', marker='1')
#
# # marker size and color
# ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
# ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
# ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
# ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
#         markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue");
#
# show()
#
# # 绘图范围 -- 可以设置x,y 的limit,
# fig, axes = plt.subplots(1, 3, figsize=(12, 4))
#
# axes[0].plot(x, x**2, x, x**3)
# axes[0].set_title("default axes ranges")
#
# axes[1].plot(x, x**2, x, x**3)
# axes[1].axis('tight')
# axes[1].set_title("tight axes")
#
# axes[2].plot(x, x**2, x, x**3)
# axes[2].set_ylim([0, 60])
# axes[2].set_xlim([2, 5])
# axes[2].set_title("custom axes range")
# show()
#
# # 使用对数刻度
# fig, axes = plt.subplots(1, 2, figsize=(10,4))
# # 正常刻度
# axes[0].plot(x, x**2, x, np.exp(x))
# axes[0].set_title("Normal scale")
# # 对数刻度
# axes[1].plot(x, x**2, x, np.exp(x))
# axes[1].set_yscale("log")
# axes[1].set_title("Logarithmic scale (y)");
# show()
#
# # 给x,y的label设置特殊的值
# fig, ax = plt.subplots(figsize=(10, 4))
#
# ax.plot(x, x**2, x, x**3, lw=2)
#
# ax.set_xticks([1, 2, 3, 4, 5])
# ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)
#
# yticks = [0, 50, 100, 150]
# ax.set_yticks(yticks)
# ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18); # use LaTeX formatted labels
# show()
#
#
# # 刻度使用科学计数法来表示
# fig, ax = plt.subplots(1, 1)
#
# ax.plot(x, x**2, x, np.exp(x))
# ax.set_title("scientific notation")
#
# ax.set_yticks([0, 50, 100, 150])
#
# from matplotlib import ticker
# formatter = ticker.ScalarFormatter(useMathText=True)
# formatter.set_scientific(True)
# formatter.set_powerlimits((-1,1))
# ax.yaxis.set_major_formatter(formatter)
# show()
#
# # 给坐标轴设置网格(可以设置颜色,线的风格,宽度)
# fig, axes = plt.subplots(1, 2, figsize=(10,3))
#
# # default grid appearance
# axes[0].plot(x, x**2, x, x**3, lw=2)
# axes[0].grid(True, color='r')
#
# # custom grid appearance
# axes[1].plot(x, x**2, x, x**3, lw=2)
# axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=1.5)
# show()
#
# # 改变坐标轴的颜色
# fig, ax = plt.subplots(figsize=(6,2))
#
# ax.spines['bottom'].set_color('blue')
# ax.spines['top'].set_color('blue')
#
# ax.spines['left'].set_color('red')
# ax.spines['left'].set_linewidth(2)
#
# # turn off axis spine to the right
# ax.spines['right'].set_color("none")
# ax.yaxis.tick_left() # only ticks on the left side
# show()
#
#
# # 一个x轴,两个y轴
# ig, ax1 = plt.subplots()
#
# ax1.plot(x, x**2, lw=2, color="blue")
# ax1.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
# for label in ax1.get_yticklabels():
#     label.set_color("blue")
#
# ax2 = ax1.twinx()
# ax2.plot(x, x**3, lw=2, color="red")
# ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
# for label in ax2.get_yticklabels():
#     label.set_color("red")
# show()

# # 四维象限的坐标
# fig, ax = plt.subplots()
#
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
#
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0
#
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data',0))   # set position of y spine to y=0
#
# xx = np.linspace(-0.75, 1., 100)
# ax.plot(xx, xx**3)
# show()
#
# # 其它风格的图片(散点,柱状图,填图模式)
# n = np.array([0,1,2,3,4,5])
#
#
# fig, axes = plt.subplots(1, 4, figsize=(12,3))
#
# axes[0].scatter(xx, xx + 0.25*np.random.randn(len(xx)))
# axes[0].set_title("scatter")
#
# axes[1].step(n, n**2, lw=2)
# axes[1].set_title("step")
#
# axes[2].bar(n, n**2, align="center", width=0.6, alpha=0.6)
# axes[2].set_title("bar")
#
# axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5);
# axes[3].set_title("fill_between");
#
# fig = plt.figure()
# ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
# t = np.linspace(0, 2 * np.pi, 100)
# ax.plot(t, t, color='blue', lw=3);
# show()
#
# # 直方图
# n = np.random.randn(100000)
# fig, axes = plt.subplots(1, 2, figsize=(12,4))
#
# axes[0].hist(n)
# axes[0].set_title("Default histogram")
# axes[0].set_xlim((min(n), max(n)))
#
# axes[1].hist(n, cumulative=True, bins=50)
# axes[1].set_title("Cumulative detailed histogram")
# axes[1].set_xlim((min(n), max(n)));
#
# show()
#
# # 在曲线位置加上注释
# fig, ax = plt.subplots()
# xx = np.linspace(-0.75, 1., 100)
# ax.plot(xx, xx**2, xx, xx**3)
#
# ax.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
# ax.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green")
# show()
#

# # 子图
# # 设置多个大小相同的子图
# fig, ax = plt.subplots(2, 3)
# fig.tight_layout()
# show()
#
# # 设置多个子图,每个子图的大小不定
# fig = plt.figure()
# ax1 = plt.subplot2grid(shape=(3, 3), loc=(0, 0), colspan=3, rowspan=1)
# ax1.set_title('ax1')
# ax2 = plt.subplot2grid(shape=(3, 3), loc=(1, 0), colspan=2)
# ax2.set_title('ax2')
# ax3 = plt.subplot2grid(shape=(3, 3), loc=(1,2), rowspan=2)
# ax3.set_title('ax3')
# ax4 = plt.subplot2grid(shape=(3, 3), loc=(2, 0))
# ax4.set_title('ax4')
# ax5 = plt.subplot2grid(shape=(3, 3), loc=(2, 1))
# ax5.set_title('ax5')
# fig.tight_layout()
# show()
#
# fig = plt.figure()
# ax1 = plt.subplot2grid(shape=(3, 3), loc=(0, 0), colspan=3, rowspan=2)
# ax1.set_title('ax1')
# # ax2 = plt.subplot2grid(shape=(3, 3), loc=(1, 0), colspan=2)
# # ax2.set_title('ax2')
# # ax3 = plt.subplot2grid(shape=(3, 3), loc=(1,2), rowspan=2)
# # ax3.set_title('ax3')
# ax4 = plt.subplot2grid(shape=(3, 3), loc=(2, 0))
# ax4.set_title('ax4')
# ax5 = plt.subplot2grid(shape=(3, 3), loc=(2, 1))
# ax5.set_title('ax5')
# fig.tight_layout()
# show()
#
#
# # 在子图中插入另一个子图
# fig, ax = plt.subplots()
# xx = np.linspace(-0.75, 1., 100)
# ax.plot(xx, xx**2, xx, xx**3)
# fig.tight_layout()
#
# # inset
# inset_ax = fig.add_axes([0.2, 0.55, 0.35, 0.35]) # X, Y, width, height
#
# inset_ax.plot(xx, xx**2, xx, xx**3)
# inset_ax.set_title('zoom near origin')
#
# # set axis range
# inset_ax.set_xlim(-.2, .2)
# inset_ax.set_ylim(-.005, .01)
#
# # set axis tick locations
# inset_ax.set_yticks([0, 0.005, 0.01])
# inset_ax.set_xticks([-0.1,0,.1])
# show()


# 3维图像
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

from mpl_toolkits.mplot3d.axes3d import Axes3D
fig = plt.figure(figsize=(14,6))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)
show()

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1, 1, 1, projection='3d')

p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)
show()

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-np.pi, cmap=matplotlib.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-np.pi, cmap=matplotlib.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3*np.pi, cmap=matplotlib.cm.coolwarm)

ax.set_xlim3d(-np.pi, 2*np.pi);
ax.set_ylim3d(0, 3*np.pi);
ax.set_zlim3d(-np.pi, 2*np.pi)
show()

fig = plt.figure(figsize=(12,6))

ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.view_init(30, 45)

ax = fig.add_subplot(1,2,2, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.view_init(70, 30)

fig.tight_layout()
show()

