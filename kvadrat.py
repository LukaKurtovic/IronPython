import clr
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms 
from System.Windows.Forms import  Form, TextBox, MenuStrip, ToolStripMenuItem

def LoadExtension(form):
    function = ToolStripMenuItem()
    function.Text = "kvadrat"
    form.added.DropDownItems.Add(function)
    function.Click += runKvadrat
    function.Tag = form

def runKvadrat(sender, args):
    a = float(sender.Tag.tbA.Text)
    rez = a*a
    sender.Tag.tbResult.Text = str(rez)



