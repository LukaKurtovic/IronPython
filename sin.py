import clr
import math
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms 
from System.Windows.Forms import  Form, TextBox, MenuStrip, ToolStripMenuItem

def LoadExtension(form):
    function = ToolStripMenuItem()
    function.Text = "sinus"
    form.added.DropDownItems.Add(function)
    function.Click += runSin
    function.Tag = form

def runSin(sender, args):
    a = float(sender.Tag.tbA.Text)
    rezultat = math.sin(a)
    sender.Tag.tbResult.Text = str(rezultat)


    