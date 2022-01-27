using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using IronPython.Hosting;
using Microsoft.Scripting;
using IronPython.Runtime;
using Microsoft.Scripting.Hosting;
using System.IO;



namespace IronPython
{
    public partial class Form1 : Form
    {
        ScriptEngine pyEngine = null;
        ScriptScope pyScope = null;

        public Form1()
        {
            pyEngine = Python.CreateEngine();
            pyScope = pyEngine.CreateScope();
            InitializeComponent();
            add.Click += new System.EventHandler(this.MenuItemAdd_Click);
            sub.Click += new System.EventHandler(this.MenuItemSub_Click);
            mul.Click += new System.EventHandler(this.MenuItemMul_Click);
            div.Click += new System.EventHandler(this.MenuItemDiv_Click);
            exit.Click += new System.EventHandler(this.MenuItemExit_Click);
            load.Click += new System.EventHandler(this.MenuItemLoadExtension_Click);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void MenuItemAdd_Click(object sender, EventArgs e)
        {
            float a = float.Parse(tbA.Text);
            float b = float.Parse(tbB.Text);
            float result = a + b;
            tbResult.Text = result.ToString();
        }

        private void MenuItemSub_Click(object sender, EventArgs e)
        {
            float a = float.Parse(tbA.Text);
            float b = float.Parse(tbB.Text);
            float result = a - b;
            tbResult.Text = result.ToString();
        }

        private void MenuItemMul_Click(object sender, EventArgs e)
        {
            float a = float.Parse(tbA.Text);
            float b = float.Parse(tbB.Text);
            float result = a * b;
            tbResult.Text = result.ToString();
        }
        private void MenuItemDiv_Click(object sender, EventArgs e)
        {
            float a = float.Parse(tbA.Text);
            float b = float.Parse(tbB.Text);
            float result = a / b;
            tbResult.Text = result.ToString();
        }

        private void MenuItemExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void MenuItemLoadExtension_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                ScriptSource scriptSourceObj = pyEngine.CreateScriptSourceFromFile(openFileDialog1.FileName);
                scriptSourceObj.Execute(pyScope);
                dynamic addOperation = pyScope.GetVariable("LoadExtension");
                addOperation(this);
            }
        }


    }
}
