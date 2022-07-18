import random
import tkinter as Tk
from itertools import count

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk,Image

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


plt.style.use('ggplot')
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
    ax1.set_title("Temperature",fontweight ="bold",fontsize = 14)
    ax2.set_title("Humidity",fontweight ="bold",fontsize = 14)
    ax3.set_title("Moisture Level Of Soil",fontweight ="bold",fontsize = 14)
    ax1.plot(x_vals[-10:-1], y_vals[-10:-1],linewidth = 1)
    ax2.plot(x_vals[-10:-1], y_vals2[-10:-1],linewidth = 1)
    ax3.plot(x_vals[-10:-1], y_vals3[-10:-1],linewidth = 1)
    



# GUI
root = Tk.Tk()
root.geometry("1000x800")
root.config(bg=rgb_hack((0, 200, 150)))
# root.wm_attributes('-transparentcolor','#add123')

bgIm = ImageTk.PhotoImage(file = 'bg4.png')

label = Tk.Label(root, image = bgIm,text="TeleEnv",font=("Georgia", 30),fg="black", bg=rgb_hack((0, 200, 150))).grid(column=0, row=0)
root.wm_attributes('-transparentcolor','#add123')

# graph 1
fig = plt.figure(figsize=(10,5),facecolor=rgb_hack((0, 200, 150)), edgecolor= 'black')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0, row=1)
# Create two subplots in row 1 and column 1, 2
fig.subplots(1, 3)

ani = FuncAnimation(fig, animate, interval=1000, blit=False)

Tk.mainloop()
