import clr
import math
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms 
from System.Windows.Forms import  Form, TextBox, MenuStrip, ToolStripMenuItem

def LoadExtension(form):
    function = ToolStripMenuItem()
    function.Text = "cosinus"
    form.added.DropDownItems.Add(function)
    function.Click += runCos
    function.Tag = form

def runCos(sender, args):
    a = float(sender.Tag.tbA.Text)
    rez = math.cos(a)
    sender.Tag.tbResult.Text = str(rez)

