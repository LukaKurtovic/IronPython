import clr
import math
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms 
from System.Windows.Forms import  Form, TextBox, MenuStrip, ToolStripMenuItem

def LoadExtension(form):
    function = ToolStripMenuItem()
    function.Text = "korijen"
    form.added.DropDownItems.Add(function)
    function.Click += runKorijen
    function.Tag = form

def runKorijen(sender, args):
    a = float(sender.Tag.tbA.Text)
    rez = math.sqrt(a)
    sender.Tag.tbResult.Text = str(rez)

