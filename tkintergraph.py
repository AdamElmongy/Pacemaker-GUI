import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar
import numpy as np
 
def live_graph(root):
    """
    This function makes a live graph that integrates with a tkinter GUI.
    
    Parameters:
    root (tk.Tk): The root window of the tkinter GUI
    
    Returns:
    None
    """
    # Create a figure and axis for the graph
    fig, ax = plt.subplots()
    x = np.arange(0, 2*np.pi, 0.01)
    y = np.sin(x)
    print(y)
    line, = ax.plot(x, y)

    ax.set_title("Egram Live Graph")
    ax.set_xlabel("Time")
    ax.set_ylabel("Pulse")
    
    # Create a canvas to display the graph in the tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    NavigationToolbar(canvas)
    
    # Update the graph every 100 milliseconds
    def update_graph():
        nonlocal x, y, line
        x += 0.1
        y = np.sin(x)
        line.set_data(x, y)
        ax.relim()
        ax.autoscale_view(True,True,True)
        canvas.draw()
        root.after(50, update_graph)
    
    # Start updating the graph
    update_graph()