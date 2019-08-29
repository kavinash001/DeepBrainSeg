#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25
#  in conjunction with Tcl version 8.6
#    Aug 21, 2019 09:22:32 AM IST  platform: Linux

import sys
import nibabel as nib
import PIL
from tkinter import filedialog
import PIL.Image, PIL.ImageTk

sys.path.append("../src/")
from Tester import get_brainsegmentation
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import numpy as np
import DeepBrainSeg_support
from helpers import *


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    DeepBrainSeg_support.set_Tk_var()
    top = Toplevel1 (root)
    DeepBrainSeg_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    DeepBrainSeg_support.set_Tk_var()
    top = Toplevel1 (w)
    DeepBrainSeg_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


def plot_normalize(img):
    print (img.min(), img.max())
    img_ = 255.*((img - img.min())/(img.max() - img.min()))
    img_ = img_.astype("uint8")
    print (img_.min(), img_.max())
    return img_

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1385x947+327+65")
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.007, rely=0.137, relheight=0.85, relwidth=0.986)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.007, rely=0.0, relheight=0.602, relwidth=0.985)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")

        self.TProgressbar1 = ttk.Progressbar(self.Frame2)
        self.TProgressbar1.place(relx=0.007, rely=0.948, relwidth=0.981
                , relheight=0.0, height=19)
        self.TProgressbar1.configure(variable=DeepBrainSeg_support.progress_bar)

        self.Frame9 = tk.Frame(self.Frame2)
        self.Frame9.place(relx=0.007, rely=0.021, relheight=0.918
                , relwidth=0.985)
        self.Frame9.configure(relief='groove')
        self.Frame9.configure(borderwidth="2")
        self.Frame9.configure(relief="groove")

        self.Frame10 = tk.Frame(self.Frame9)
        self.Frame10.place(relx=0.008, rely=0.022, relheight=0.955
                , relwidth=0.321)
        self.Frame10.configure(relief='groove')
        self.Frame10.configure(borderwidth="2")
        self.Frame10.configure(relief="groove")

        self.AxialCanvas = tk.Canvas(self.Frame10)
        self.AxialCanvas.place(relx=0.024, rely=0.024, relheight=0.944
                , relwidth=0.873)
        self.AxialCanvas.configure(borderwidth="2")
        self.AxialCanvas.configure(relief="ridge")
        self.AxialCanvas.configure(selectbackground="#c4c4c4")

        self.Frame11 = tk.Frame(self.Frame9)
        self.Frame11.place(relx=0.34, rely=0.022, relheight=0.955
                , relwidth=0.321)
        self.Frame11.configure(relief='groove')
        self.Frame11.configure(borderwidth="2")
        self.Frame11.configure(relief="groove")

        self.SagitalCanvas = tk.Canvas(self.Frame11)
        self.SagitalCanvas.place(relx=0.024, rely=0.024, relheight=0.944
                , relwidth=0.873)
        self.SagitalCanvas.configure(borderwidth="2")
        self.SagitalCanvas.configure(relief="ridge")
        self.SagitalCanvas.configure(selectbackground="#c4c4c4")

        self.Frame12 = tk.Frame(self.Frame9)
        self.Frame12.place(relx=0.672, rely=0.022, relheight=0.955
                , relwidth=0.321)
        self.Frame12.configure(relief='groove')
        self.Frame12.configure(borderwidth="2")
        self.Frame12.configure(relief="groove")

        self.CorronalCanvas = tk.Canvas(self.Frame12)
        self.CorronalCanvas.place(relx=0.024, rely=0.024, relheight=0.944
                , relwidth=0.873)
        self.CorronalCanvas.configure(borderwidth="2")
        self.CorronalCanvas.configure(relief="ridge")
        self.CorronalCanvas.configure(selectbackground="#c4c4c4")

        self.LoadFrame = tk.Frame(self.Frame1)
        self.LoadFrame.place(relx=0.007, rely=0.621, relheight=0.366
                , relwidth=0.985)
        self.LoadFrame.configure(relief='groove')
        self.LoadFrame.configure(borderwidth="2")
        self.LoadFrame.configure(relief="groove")

        self.Flair_Frame = tk.Frame(self.LoadFrame)
        self.Flair_Frame.place(relx=0.007, rely=0.034, relheight=0.932
                , relwidth=0.175)
        self.Flair_Frame.configure(relief='groove')
        self.Flair_Frame.configure(borderwidth="2")
        self.Flair_Frame.configure(relief="groove")

        self.Button1 = tk.Button(self.Flair_Frame)
        self.Button1.place(relx=0.255, rely=0.836, height=35, width=110)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=self.Load_Flair)
        self.Button1.configure(compound='center')
        self.Button1.configure(text='''Load Flair''')

        self.Flair_canvas = tk.Canvas(self.Flair_Frame)
        self.Flair_canvas.place(relx=0.043, rely=0.036, relheight=0.767
                , relwidth=0.898)
        self.Flair_canvas.configure(borderwidth="2")
        self.Flair_canvas.configure(relief="ridge")
        self.Flair_canvas.configure(selectbackground="#c4c4c4")

        self.T1Frame = tk.Frame(self.LoadFrame)
        self.T1Frame.place(relx=0.201, rely=0.034, relheight=0.932
                , relwidth=0.182)
        self.T1Frame.configure(relief='groove')
        self.T1Frame.configure(borderwidth="2")
        self.T1Frame.configure(relief="groove")

        self.Button2 = tk.Button(self.T1Frame)
        self.Button2.place(relx=0.286, rely=0.836, height=35, width=110)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(command=self.Load_T1)
        self.Button2.configure(compound='center')
        self.Button2.configure(text='''Load T1''')

        self.T1_canvas = tk.Canvas(self.T1Frame)
        self.T1_canvas.place(relx=0.041, rely=0.036, relheight=0.767
                , relwidth=0.902)
        self.T1_canvas.configure(borderwidth="2")
        self.T1_canvas.configure(relief="ridge")
        self.T1_canvas.configure(selectbackground="#c4c4c4")

        self.T1ceFrame = tk.Frame(self.LoadFrame)
        self.T1ceFrame.place(relx=0.401, rely=0.034, relheight=0.932
                , relwidth=0.19)
        self.T1ceFrame.configure(relief='groove')
        self.T1ceFrame.configure(borderwidth="2")
        self.T1ceFrame.configure(relief="groove")

        self.Button3 = tk.Button(self.T1ceFrame)
        self.Button3.place(relx=0.314, rely=0.836, height=35, width=100)
        self.Button3.configure(activebackground="#f9f9f9")
        self.Button3.configure(command=self.Load_T1ce)
        self.Button3.configure(compound='center')
        self.Button3.configure(text='''Load T1ce''')

        self.T1ce_canvas = tk.Canvas(self.T1ceFrame)
        self.T1ce_canvas.place(relx=0.039, rely=0.036, relheight=0.767
                , relwidth=0.906)
        self.T1ce_canvas.configure(borderwidth="2")
        self.T1ce_canvas.configure(relief="ridge")
        self.T1ce_canvas.configure(selectbackground="#c4c4c4")

        self.T2Frame = tk.Frame(self.LoadFrame)
        self.T2Frame.place(relx=0.61, rely=0.034, relheight=0.932
                , relwidth=0.182)
        self.T2Frame.configure(relief='groove')
        self.T2Frame.configure(borderwidth="2")
        self.T2Frame.configure(relief="groove")

        self.Button4 = tk.Button(self.T2Frame)
        self.Button4.place(relx=0.327, rely=0.836, height=35, width=100)
        self.Button4.configure(activebackground="#f9f9f9")
        self.Button4.configure(command=self.Load_T2)
        self.Button4.configure(compound='center')
        self.Button4.configure(text='''Load T2''')

        self.T2_canvas = tk.Canvas(self.T2Frame)
        self.T2_canvas.place(relx=0.041, rely=0.036, relheight=0.767
                , relwidth=0.902)
        self.T2_canvas.configure(borderwidth="2")
        self.T2_canvas.configure(relief="ridge")
        self.T2_canvas.configure(selectbackground="#c4c4c4")

        self.SegFrame = tk.Frame(self.LoadFrame)
        self.SegFrame.place(relx=0.81, rely=0.034, relheight=0.932
                , relwidth=0.175)
        self.SegFrame.configure(relief='groove')
        self.SegFrame.configure(borderwidth="2")
        self.SegFrame.configure(relief="groove")

        self.Button5 = tk.Button(self.SegFrame)
        self.Button5.place(relx=0.213, rely=0.836, height=35, width=160)
        self.Button5.configure(activebackground="#f9f9f9")
        self.Button5.configure(command=self.Get_Segmentation)
        self.Button5.configure(compound='center')
        self.Button5.configure(text='''Get Segmentation''')

        self.seg_canvas = tk.Canvas(self.SegFrame)
        self.seg_canvas.place(relx=0.043, rely=0.036, relheight=0.767
                , relwidth=0.898)
        self.seg_canvas.configure(borderwidth="2")
        self.seg_canvas.configure(relief="ridge")
        self.seg_canvas.configure(selectbackground="#c4c4c4")

        self.SegmentationOverlay = tk.Button(self.Frame1)
        self.SegmentationOverlay.place(relx=0.432, rely=0.0, height=25
                , width=190)
        self.SegmentationOverlay.configure(activebackground="#f9f9f9")
        self.SegmentationOverlay.configure(command=DeepBrainSeg_support.SegmentationOverlay)
        self.SegmentationOverlay.configure(text='''Segmentation overlay''')

        self.LogoCanvas = tk.Canvas(top)
        self.LogoCanvas.place(relx=0.007, rely=0.011, relheight=0.117
                , relwidth=0.983)
        self.LogoCanvas.configure(borderwidth="2")
        self.LogoCanvas.configure(relief="ridge")
        self.LogoCanvas.configure(selectbackground="#c4c4c4")
    

    def update_main_view(self, vol, slice1, slice2, slice3):

        true_size = vol.shape[:2]
        size = (self.AxialCanvas.winfo_width(), self.AxialCanvas.winfo_height())
        size = (size[0], int(true_size[0]/true_size[1])*size[1]) if size[0] < size[1] else (int(true_size[1]/true_size[0])*size[0], size[1])
    
        self.AxialCanvas_image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(plot_normalize(vol[:,:,slice3].T)).resize(size))
        self.AxialCanvas.create_image(0, 0, image=self.AxialCanvas_image, anchor=tk.NW)


        true_size = (vol.shape[0], vol.shape[2])
        size = (self.AxialCanvas.winfo_width(), self.AxialCanvas.winfo_height())
        size = (size[0], int(true_size[0]/true_size[1])*size[1]) if size[0] < size[1] else (int(true_size[1]/true_size[0])*size[0], size[1])
    
        self.SagitalCanvas_image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(plot_normalize(np.flipud(vol[:, slice2, :].T))).resize(size))
        self.SagitalCanvas.create_image(0, 0, image=self.SagitalCanvas_image, anchor=tk.NW)


        true_size = (vol.shape[1], vol.shape[2])
        size = (self.AxialCanvas.winfo_width(), self.AxialCanvas.winfo_height())
        size = (size[0], int(true_size[0]/true_size[1])*size[1]) if size[0] < size[1] else (int(true_size[1]/true_size[0])*size[0], size[1])
    
        self.CorronalCanvas_image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(plot_normalize(np.flipud(vol[slice1, :, :].T))).resize(size))
        self.CorronalCanvas.create_image(0, 0, image=self.CorronalCanvas_image, anchor=tk.NW)


    def Load_T2(self, event=None):

        filename = filedialog.askopenfilename()
        nib_vol = nib.load(filename)
        self.affine = nib_vol.affine
        self.T2_vol = nib_vol.get_data()

        mid_slice = self.T2_vol.shape[2]//2

        true_size = self.T2_vol.shape[:2]
        size = (self.T2_canvas.winfo_width(), self.T2_canvas.winfo_height())
        size = (size[0], int(true_size[0]/true_size[1])*size[1]) if size[0] < size[1] else (int(true_size[1]/true_size[0])*size[0], size[1])

        self.T2_canvas_image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(plot_normalize(self.T2_vol[:,:,mid_slice].T)).resize(size))
        self.T2_canvas.create_image(0, 0, image=self.T2_canvas_image, anchor=tk.NW)
        self.update_main_view(self.T2_vol, self.T2_vol.shape[0]//2, self.T2_vol.shape[1]//2, self.T2_vol.shape[2]//2)
    
    def Load_T1(self, event=None):
        filename = filedialog.askopenfilename()
        nib_vol = nib.load(filename)
        self.affine = nib_vol.affine
        self.T1_vol = nib_vol.get_data()

        mid_slice = self.T1_vol.shape[2]//2

        true_size = self.T1_vol.shape[:2]
        size = (self.T1_canvas.winfo_width(), self.T1_canvas.winfo_height())
        size = (size[0], int(true_size[0]/true_size[1])*size[1]) if size[0] < size[1] else (int(true_size[1]/true_size[0])*size[0], size[1])


        self.T1_canvas_image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(plot_normalize(self.T1_vol[:,:,mid_slice].T)).resize(size))
        self.T1_canvas.create_image(0, 0, image=self.T1_canvas_image, anchor=tk.NW)
        self.update_main_view(self.T1_vol, self.T1_vol.shape[0]//2, self.T1_vol.shape[1]//2, self.T1_vol.shape[2]//2)


    def Load_Flair(self, event=None):
        filename = filedialog.askopenfilename()
        nib_vol = nib.load(filename)
        self.affine = nib_vol.affine
        self.Flair_vol = nib_vol.get_data()

        mid_slice = self.Flair_vol.shape[2]//2

        true_size = self.Flair_vol.shape[:2]
        size = (self.Flair_canvas.winfo_width(), self.Flair_canvas.winfo_height())
        size = (size[0], int(true_size[0]/true_size[1])*size[1]) if size[0] < size[1] else (int(true_size[1]/true_size[0])*size[0], size[1])


        self.Flair_canvas_image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(plot_normalize(self.Flair_vol[:,:,mid_slice].T)).resize(size))
        self.Flair_canvas.create_image(0, 0, image=self.Flair_canvas_image, anchor=tk.NW)
        self.update_main_view(self.Flair_vol, self.Flair_vol.shape[0]//2, self.Flair_vol.shape[1]//2, self.Flair_vol.shape[2]//2)


    def Load_T1ce(self, event=None):
        filename = filedialog.askopenfilename()
        nib_vol = nib.load(filename)
        self.affine = nib_vol.affine
        self.T1ce_vol = nib_vol.get_data()

        mid_slice = self.T1ce_vol.shape[2]//2

        true_size = self.T1ce_vol.shape[:2]
        size = (self.T1ce_canvas.winfo_width(), self.T1ce_canvas.winfo_height())
        size = (size[0], int(true_size[0]/true_size[1])*size[1]) if size[0] < size[1] else (int(true_size[1]/true_size[0])*size[0], size[1])


        self.T1ce_canvas_image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(plot_normalize(self.T1ce_vol[:,:,mid_slice].T)).resize(size))
        self.T1ce_canvas.create_image(0, 0, image=self.T1ce_canvas_image, anchor=tk.NW)
        self.update_main_view(self.T1ce_vol, self.T1ce_vol.shape[0]//2, self.T1ce_vol.shape[1]//2, self.T1ce_vol.shape[2]//2)

    
    def Get_Segmentation(self, event=None):
        try:
            if (self.T1_vol != None) and (self.T2_vol != None) and (self.T1ce_vol != None) and (self.Flair_vol != None):
                pass
            else:
                pass
        except:
            ValueError 

        self.prediction = get_brainsegmentation(self.T1_vol, self.T2_vol, self.T1ce_vol, self.Flair_vol)
        self.update_main_view(self.prediction, self.prediction.shape[0]//2, self.prediction.shape[1]//2, self.prediction.shape[2]//2)

        pass


if __name__ == '__main__':
    vp_start_gui()





