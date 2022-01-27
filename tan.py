import clr
import math
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms 
from System.Windows.Forms import  Form, TextBox, MenuStrip, ToolStripMenuItem

def LoadExtension(form):
    function = ToolStripMenuItem()
    function.Text = "tangens"
    form.added.DropDownItems.Add(function)
    function.Click += runTan
    function.Tag = form

def runTan(sender, args):
    a = float(sender.Tag.tbA.Text)
    rez = math.tan(a)
    sender.Tag.tbResult.Text = str(rez)


    