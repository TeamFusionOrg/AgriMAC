import random
import tkinter as Tk
from itertools import count

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use('dark_background')
# values for first graph
x_vals = []
y_vals = []
# values for second graph
y_vals2 = []
y_vals3 = []

index = count()
index2 = count()

def animate(i):
    # Generate values
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 50))
    y_vals2.append(random.randint(0, 50))
    y_vals3.append(random.randint(0, 50))
    # Get all axes of figure
    ax1, ax2,ax3 = fig.get_axes()
    # Clear current data
    ax1.cla()
    ax2.cla()
    ax3.cla()
    # Plot new data
    ax1.plot(x_vals[-10:-1], y_vals[-10:-1],linewidth = 1)
    ax2.plot(x_vals[-10:-1], y_vals2[-10:-1],linewidth = 1)
    ax3.plot(x_vals[-10:-1], y_vals3[-10:-1],linewidth = 1)



# GUI
root = Tk.Tk()
root.geometry("1000x800")
# root.attributes('-fullscreen',True)
label = Tk.Label(root, text="Realtime Animated Graphs").grid(column=0, row=0)

# graph 1
fig = plt.figure(figsize=(20,10))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0, row=1)
# Create two subplots in row 1 and column 1, 2

fig.subplots(1, 3)
ani = FuncAnimation(fig, animate, interval=1000, blit=False)

Tk.mainloop()



# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from random import randrange
 
# fig = plt.figure(figsize=(6, 3))
# x = [0]
# y = [0]
 
# ln, = plt.plot(x, y, '-')
# plt.axis([0, 100, 0, 10])
 
# def update(frame):
#     x.append(x[-1] + 1)
#     y.append(randrange(0, 10))
 
#     ln.set_data(x, y) 
#     return ln,
 
# animation = FuncAnimation(fig, update, interval=500)
# plt.show()