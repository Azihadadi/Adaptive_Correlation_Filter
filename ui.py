from tkinter import *
from tkinter import filedialog, ttk
from tkinter.font import Font, BOLD
from tkinter.ttk import Style, Notebook
from core.controller import Controller
from PIL import Image, ImageTk

class Root(Tk):
    # Styles
    colorHeader = '#2a9d8f'
    colorHeaderTab = '#005580'
    colorContent = "#f0f5f5"
    colorSelected = "#005580"
    colorUnSelected = "#b1cae7"
    colorLabel = "#05668d"
    colorBgLabel = "#ffffff"
    colorStartButton = "#05668d"
    colorExitButton = "#ff0000"

    def __init__(self):
        super(Root, self).__init__()
        self.setStylies()
        # headers
        self.var1 = StringVar()
        self.var1.set("Visual Object Tracking")
        self.var2 = StringVar()
        self.var2.set("Adaptive Correlation Filters(MOSSE)")
        self.header_up = Label(self, textvariable=self.var1, relief=RAISED, font=self.fontStyleHeader_up,
                               bg=self.colorHeader,
                               fg="white",
                               bd="0",
                               pady="10")
        self.header_down = Label(self, textvariable=self.var2, relief=RAISED, font=self.fontStyleHeader_down,
                                 bg=self.colorHeader,
                                 fg="white",
                                 bd="0",
                                 pady="10")
        # icon
        self.img = ImageTk.PhotoImage(Image.open('data/icons/logo.png'))
        self.imageIcon_label = Label(self, image=self.img)
        self.imageIcon_label.img = self.img

        # Tab Page
        self.tabControl = Notebook(self)
        self.tab_algorithm = Frame(self.tabControl, width=200, height=300)
        self.tab_application = Frame(self.tabControl, width=200, height=300)
        self.tabControl.add(self.tab_algorithm, text="Demo")

        # information frame
        self.info_labelFrame = LabelFrame(self.tab_algorithm, text="Help", width=550,
                                          height=200,
                                          bd=2,
                                          font=self.fontStyleTabHeader_down, foreground=self.colorHeaderTab,
                                          background="white")
        self.info_labelFrame.grid_propagate(0)

        self.info_label = ttk.Label(self.info_labelFrame,
                                    text="(1) You can track a moving object from a video or use your webcam."
                                    "\n      (If you want to use a video, click on Browse button and choose the video)"
                                    "\n(2) Click on Start Tracking."
                                    "\n(3) Draw the ROI."
                                    "\n(4) If you want to reset the tracker, press 'c' key."
                                    "\n(5) If you want to pause/continue the frame, press on space key."
                                    "\n(6) If you want to quit the frame, press Esc key.",
                                    background="white",
                                    foreground=self.colorSelected, font=self.fontStyleContent_labelFrame, justify=LEFT,
                                    padding=10)

        self.lr = DoubleVar()
        self.num_pretrain = IntVar()

        # # default values
        self.lr.set(0.125)
        self.num_pretrain.set(128)

        # start Button
        self.video_src = ''
        self.browse_botton = Button(self.tab_algorithm, text="Browse", command=self.browseCallBack,
                                     bg=self.colorStartButton,
                                     fg=self.colorBgLabel,
                                     width=10, font=self.fontStyleTabHeader_down, relief=FLAT)

        # start Button
        self.start_botton = Button(self.tab_algorithm, text="Start Tracking", command=self.startCallBack,
                                     bg=self.colorStartButton,
                                     fg=self.colorBgLabel,
                                     width=13, font=self.fontStyleTabHeader_down, relief=FLAT)

        self.exit_botton = Button(self.tab_algorithm, text="Exit", command=self.exitCallBack,
                                     bg=self.colorExitButton,
                                     fg=self.colorBgLabel,
                                     width=10, font=self.fontStyleTabHeader_down, relief=FLAT)

        self.footPage_label = Label(self.tab_algorithm,
                                    text="Azadeh Hadadi & Jue Wang, Visual Tracking Module, MSCV2, December 2020",
                                    font=self.fontStyleLabelFooter, fg=self.colorSelected, bg=self.colorContent)
        self.setPositions()

    def browseCallBack(self):
        self.video_src = filedialog.askopenfilename(initialdir=".\\data\\videos", title="Select A Video")

    def startCallBack(self):
        if self.video_src == '':
            self.video_src = '0'
        self.app = Controller(self,self.video_src).run()
        self.video_src = ''

    def exitCallBack(self):
        self.destroy()

    def setStylies(self):
        # styles
        self.fontStyleHeader_up = Font(family="ARIAL", size=20, weight=BOLD)
        self.fontStyleHeader_down = Font(family="ARIAL", size=13, weight=BOLD)
        self.fontStyleTabHeader_down = Font(family="ARIAL", size=12, weight=BOLD)
        self.fontStyleContent_labelFrame = Font(family="ARIAL", size=12)
        self.fontStyleLabelFooter = Font(family="ARIAL", size=10)

        self.style_tabControl = Style()
        self.style_tabControl.configure('.', background=self.colorContent)
        self.style_tabControl.configure('TNotebook', background="white", tabmargins=[5, 5, 0, 0])
        self.style_tabControl.map("TNotebook.Tab", foreground=[("selected", self.colorSelected)])
        self.style_tabControl.configure('TNotebook.Tab', padding=[10, 4], font=('ARIAL', '13', 'bold'),
                                        foreground=self.colorUnSelected)

    def setPositions(self):
        # Position
        self.header_up.place(x=50, y=50)
        self.header_down.place(x=50, y=50)
        self.header_up.pack(fill="x")
        self.header_down.pack(fill="x")
        # icon
        self.imageIcon_label.place(x=0, y=3)

        # tab
        self.tabControl.pack(expand=1, fill="both")

        # info frame
        self.info_labelFrame.place(x=10, y=30)

        # info frame label
        self.info_label.place(x=0,y=0)

        # start button
        self.browse_botton.place(x=10, y=250)
        self.start_botton.place(x=140, y=250)
        self.exit_botton.place(x=300, y=250)
        self.footPage_label.pack(side=BOTTOM, anchor="sw")

root = Root()
root.title("demo")
root.geometry("800x500")
root.mainloop()
