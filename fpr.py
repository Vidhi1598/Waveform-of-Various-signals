from tkinter import*
from tkinter import messagebox
import matplotlib.pyplot as plot
import numpy as np
from scipy import signal

# For main window designing
root=Tk()
root.geometry("500x500+500+300")
root.title("signal generation")
root.configure(background='blue')






# For Sinewave geneartion
addFrame=Toplevel(root)
addFrame.title("Sine wave")
addFrame.geometry("400x200+300+200")
addFrame.withdraw()
# function to generate sinewave
def generate():
	try:
		s = entFrequency.get()
		f=float(s)
		Fs=8000
		sample = 8000
		x = np.arange(sample)
		y = np.sin(2 * np.pi * f * x / Fs)
		plot.plot(x, y)
		plot.xlabel('time')
		plot.ylabel('amplitude')
		plot.show()
		messagebox.showinfo("Results","Sine wave generated")
	except ValueError:
		messagebox.showerror("Issue","Incorrect Input")
		entFrequency.delete(0,END)
		entFrequency.focus()
# buttons,entry delcared
lblFrequency = Label(addFrame,text="Enter a frequency:")
lblFrequency.place(x=10,y=10)
entFrequency = Entry(addFrame,bd=5)
entFrequency.place(x=120,y=10)
btnGenerate=Button(addFrame,text="Generate",command=generate)
btnGenerate.place(x=100,y=50)
def f1():
	root.withdraw()
	addFrame.deiconify()
btnSine=Button(root,text="Sine waveform",font=('arial',20,'bold'),width=20,command=f1)


		

#Triangular waveform

triFrame=Toplevel(root)
triFrame.title("Triangular wave")
triFrame.geometry("400x200+300+200")
triFrame.withdraw()
#Function
def generate1():
	try:
	
		phase=-10
		length=30 # should be positive
		amplitude=10
		s= entFrequency1.get()
		x=float(s)
		x=np.arange(0,100,0.1)
		def triang(x,phase,length,amplitude):
			alpha=(amplitude)/(length/2)
			return -amplitude/2+amplitude*((x-phase)%length==length/2) \
            		+alpha*((x-phase)%(length/2))*((x-phase)%length<=length/2) \
            		+(amplitude-alpha*((x-phase)%(length/2)))*((x-phase)%length>length/2)
		tr=triang(x,phase,length,amplitude)
		plot.plot(tr)
		plot.xlabel('Time')
		plot.ylabel('Amplitude = time')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='b')
		plot.show()
		messagebox.showinfo("Results","Triangular wave generated")
	except ValueError:
		messagebox.showerror("Issue","Incorrect Input")
		entFrequency1.delete(0,END)
		entFrequency1.focus()
lblFrequency1 = Label(triFrame,text="Enter a frequency:")
lblFrequency1.place(x=10,y=10)
entFrequency1 = Entry(triFrame,bd=5)
entFrequency1.place(x=120,y=10)
btnGenerate1=Button(triFrame,text="Generate",command=generate1)
btnGenerate1.place(x=100,y=50)
def f3():
	root.withdraw()
	triFrame.deiconify()
btnTri=Button(root,text="Triangular waveform",font=('arial',20,'bold'),width=20,command=f3)







#Sawtooth wave generation
sawFrame=Toplevel(root)
sawFrame.title("Sawtooth waveform")
sawFrame.geometry("400x200+300+200")
sawFrame.withdraw()
#Function
def generate2():	
	try:
		s2 = entFrequency2.get()
		t=float(s2)
		t = np.linspace(0, 1, 500)
		plot.plot(t, signal.sawtooth(2 * np.pi * 5 * t))
		plot.xlabel('time')
		plot.ylabel('amplitude')
		plot.show()
		messagebox.showinfo("Results","Sawtooth wave generated")
	except ValueError:
		messagebox.showerror("Issue","Incorrect Input")
		entFrequency2.delete(0,END)
		entFrequency2.focus()

lblFrequency2 = Label(sawFrame,text="Enter a frequency:")
lblFrequency2.place(x=10,y=10)
entFrequency2 = Entry(sawFrame,bd=5)
entFrequency2.place(x=120,y=10)
btnGenerate2=Button(sawFrame,text="Generate",command=generate2)
btnGenerate2.place(x=100,y=50)
def f5():
	root.withdraw()
	sawFrame.deiconify()
btnSaw=Button(root,text="Sawtooth waveform",font=('arial',20,'bold','red'),width=20,command=f5)



btnSine.pack(pady=10)
btnTri.pack(pady=10)
btnSaw.pack(pady=10)




# From sine wave generation window to main window
def f2():
	addFrame.withdraw()
	root.deiconify()
addFrame.protocol("WM_DELETE_WINDOW",f2)
# From triangle wave generation window to main window
def f4():
	triFrame.withdraw()
	root.deiconify()
triFrame.protocol("WM_DELETE_WINDOW",f4)
# From sawtooth wave generation window to main window
def f6():
	sawFrame.withdraw()
	root.deiconify()
sawFrame.protocol("WM_DELETE_WINDOW",f6)





root.mainloop()