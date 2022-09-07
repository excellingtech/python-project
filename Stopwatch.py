from tkinter import *
import time

def Main():
    global watch

    watch = Tk()
    watch.title("Stopwatch")
    width = 600
    height = 200
    screen_width = watch.winfo_screenwidth()
    screen_height = watch.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    watch.geometry("%dx%d+%d+%d" % (width, height, x, y))
    watch.resizable(width=False,height=False)

    Top = Frame(watch, width=600)
    Top.pack(side=TOP)

    stopWatch = StopWatch(watch)
    stopWatch.pack(side=TOP)

    Bottom = Frame(watch, width=600)
    Bottom.pack(side=BOTTOM)

    Start = Button(Bottom, text='START',bg="yellow",command=stopWatch.Start, width=10, height=2)
    Start.pack(side=LEFT)

    Stop = Button(Bottom, text='STOP',bg="yellow",command=stopWatch.Stop, width=10, height=2)
    Stop.pack(side=LEFT)

    Reset = Button(Bottom, text='RESET',bg="yellow",command=stopWatch.Reset, width=10, height=2)
    Reset.pack(side=LEFT)

    Exit = Button(Bottom, text='CLOSE',bg="yellow",command=stopWatch.Exit, width=10, height=2)
    Exit.pack(side=LEFT)

    Title = Label(Top, text="STOPWATCH", font=("arial",26,'bold'), fg="orange", bg="black")
    Title.pack(fill=X)

    watch.config(bg="black")
    watch.mainloop()

class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):

        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="lime", bg="black")

        self.SetTime(self.nextTime)

        timeText.pack(fill=X, expand=NO, pady=2, padx=2)

    def Updater(self):

        self.nextTime = time.time() - self.startTime

        self.SetTime(self.nextTime)

        self.timer = self.after(50, self.Updater)

    def SetTime(self, nextElap):

        minutes = int(nextElap / 60)

        seconds = int(nextElap - minutes * 60.0)

        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)

        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))

    def Start(self):
        if not self.onRunning:

            self.startTime = time.time() - self.nextTime

            self.Updater()

            self.onRunning = 1

    def Stop(self):
        if self.onRunning:

            self.after_cancel(self.timer)

            self.nextTime = time.time() - self.startTime

            self.SetTime(self.nextTime)

            self.onRunning = 0

    def Exit(self):
        watch.destroy()
        exit()

    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)
        self.Stop()

if __name__ == '__main__':
    Main()
