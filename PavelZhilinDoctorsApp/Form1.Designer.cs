namespace PavelZhilinDoctorsApp
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            Button btnChooseDirection;
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            toolStripTextBox1 = new ToolStripTextBox();
            panel1 = new Panel();
            label1 = new Label();
            pictureBox1 = new PictureBox();
            tabControl1 = new TabControl();
            tabPage1 = new TabPage();
            txtAvaivbleDoctors = new Label();
            listBoxDirections = new ListBox();
            tabPage2 = new TabPage();
            labelDoctorDirections = new Label();
            pictureDoctorAva = new PictureBox();
            labelDoctorDiscount = new Label();
            labelDoctorPrice = new Label();
            labelDoctorDescription = new Label();
            labelDoctorName = new Label();
            listBox2 = new ListBox();
            button1 = new Button();
            tabPage3 = new TabPage();
            buttonPay = new Button();
            labelReciptValue = new Label();
            labelReciptDiscount = new Label();
            labelResiptCostRaw = new Label();
            label2 = new Label();
            btnChooseDirection = new Button();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            tabControl1.SuspendLayout();
            tabPage1.SuspendLayout();
            tabPage2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureDoctorAva).BeginInit();
            tabPage3.SuspendLayout();
            SuspendLayout();
            // 
            // btnChooseDirection
            // 
            resources.ApplyResources(btnChooseDirection, "btnChooseDirection");
            btnChooseDirection.BackColor = Color.FromArgb(112, 178, 175);
            btnChooseDirection.FlatAppearance.BorderColor = Color.FromArgb(112, 178, 175);
            btnChooseDirection.FlatAppearance.BorderSize = 0;
            btnChooseDirection.ForeColor = Color.Black;
            btnChooseDirection.Name = "btnChooseDirection";
            btnChooseDirection.UseVisualStyleBackColor = false;
            btnChooseDirection.Click += btnChooseDirection_Click;
            // 
            // toolStripTextBox1
            // 
            resources.ApplyResources(toolStripTextBox1, "toolStripTextBox1");
            toolStripTextBox1.Name = "toolStripTextBox1";
            // 
            // panel1
            // 
            resources.ApplyResources(panel1, "panel1");
            panel1.BackColor = Color.FromArgb(210, 246, 231);
            panel1.BorderStyle = BorderStyle.FixedSingle;
            panel1.CausesValidation = false;
            panel1.Controls.Add(label1);
            panel1.Controls.Add(pictureBox1);
            panel1.Name = "panel1";
            // 
            // label1
            // 
            resources.ApplyResources(label1, "label1");
            label1.Name = "label1";
            // 
            // pictureBox1
            // 
            resources.ApplyResources(pictureBox1, "pictureBox1");
            pictureBox1.Image = Properties.Resources.logo__1_;
            pictureBox1.Name = "pictureBox1";
            pictureBox1.TabStop = false;
            // 
            // tabControl1
            // 
            resources.ApplyResources(tabControl1, "tabControl1");
            tabControl1.Controls.Add(tabPage1);
            tabControl1.Controls.Add(tabPage2);
            tabControl1.Controls.Add(tabPage3);
            tabControl1.Name = "tabControl1";
            tabControl1.SelectedIndex = 0;
            tabControl1.Deselecting += tabControl1_Deselecting;
            // 
            // tabPage1
            // 
            resources.ApplyResources(tabPage1, "tabPage1");
            tabPage1.Controls.Add(txtAvaivbleDoctors);
            tabPage1.Controls.Add(listBoxDirections);
            tabPage1.Controls.Add(btnChooseDirection);
            tabPage1.Name = "tabPage1";
            tabPage1.UseVisualStyleBackColor = true;
            // 
            // txtAvaivbleDoctors
            // 
            resources.ApplyResources(txtAvaivbleDoctors, "txtAvaivbleDoctors");
            txtAvaivbleDoctors.Name = "txtAvaivbleDoctors";
            // 
            // listBoxDirections
            // 
            resources.ApplyResources(listBoxDirections, "listBoxDirections");
            listBoxDirections.FormattingEnabled = true;
            listBoxDirections.Name = "listBoxDirections";
            listBoxDirections.SelectedIndexChanged += listBox1_SelectedIndexChanged;
            // 
            // tabPage2
            // 
            resources.ApplyResources(tabPage2, "tabPage2");
            tabPage2.Controls.Add(labelDoctorDirections);
            tabPage2.Controls.Add(pictureDoctorAva);
            tabPage2.Controls.Add(labelDoctorDiscount);
            tabPage2.Controls.Add(labelDoctorPrice);
            tabPage2.Controls.Add(labelDoctorDescription);
            tabPage2.Controls.Add(labelDoctorName);
            tabPage2.Controls.Add(listBox2);
            tabPage2.Controls.Add(button1);
            tabPage2.Name = "tabPage2";
            tabPage2.UseVisualStyleBackColor = true;
            // 
            // labelDoctorDirections
            // 
            resources.ApplyResources(labelDoctorDirections, "labelDoctorDirections");
            labelDoctorDirections.Name = "labelDoctorDirections";
            // 
            // pictureDoctorAva
            // 
            resources.ApplyResources(pictureDoctorAva, "pictureDoctorAva");
            pictureDoctorAva.Name = "pictureDoctorAva";
            pictureDoctorAva.TabStop = false;
            // 
            // labelDoctorDiscount
            // 
            resources.ApplyResources(labelDoctorDiscount, "labelDoctorDiscount");
            labelDoctorDiscount.Name = "labelDoctorDiscount";
            // 
            // labelDoctorPrice
            // 
            resources.ApplyResources(labelDoctorPrice, "labelDoctorPrice");
            labelDoctorPrice.Name = "labelDoctorPrice";
            // 
            // labelDoctorDescription
            // 
            resources.ApplyResources(labelDoctorDescription, "labelDoctorDescription");
            labelDoctorDescription.Name = "labelDoctorDescription";
            // 
            // labelDoctorName
            // 
            resources.ApplyResources(labelDoctorName, "labelDoctorName");
            labelDoctorName.Name = "labelDoctorName";
            // 
            // listBox2
            // 
            resources.ApplyResources(listBox2, "listBox2");
            listBox2.FormattingEnabled = true;
            listBox2.Name = "listBox2";
            listBox2.SelectedIndexChanged += listBox2_SelectedIndexChanged;
            // 
            // button1
            // 
            resources.ApplyResources(button1, "button1");
            button1.BackColor = Color.FromArgb(112, 178, 175);
            button1.FlatAppearance.BorderColor = Color.FromArgb(112, 178, 175);
            button1.FlatAppearance.BorderSize = 0;
            button1.Name = "button1";
            button1.UseVisualStyleBackColor = false;
            button1.Click += button1_Click;
            // 
            // tabPage3
            // 
            resources.ApplyResources(tabPage3, "tabPage3");
            tabPage3.Controls.Add(buttonPay);
            tabPage3.Controls.Add(labelReciptValue);
            tabPage3.Controls.Add(labelReciptDiscount);
            tabPage3.Controls.Add(labelResiptCostRaw);
            tabPage3.Controls.Add(label2);
            tabPage3.Name = "tabPage3";
            tabPage3.UseVisualStyleBackColor = true;
            // 
            // buttonPay
            // 
            resources.ApplyResources(buttonPay, "buttonPay");
            buttonPay.BackColor = Color.FromArgb(112, 178, 175);
            buttonPay.FlatAppearance.BorderColor = Color.FromArgb(112, 178, 175);
            buttonPay.Name = "buttonPay";
            buttonPay.UseVisualStyleBackColor = false;
            buttonPay.Click += buttonPay_Click;
            // 
            // labelReciptValue
            // 
            resources.ApplyResources(labelReciptValue, "labelReciptValue");
            labelReciptValue.Name = "labelReciptValue";
            // 
            // labelReciptDiscount
            // 
            resources.ApplyResources(labelReciptDiscount, "labelReciptDiscount");
            labelReciptDiscount.Name = "labelReciptDiscount";
            // 
            // labelResiptCostRaw
            // 
            resources.ApplyResources(labelResiptCostRaw, "labelResiptCostRaw");
            labelResiptCostRaw.Name = "labelResiptCostRaw";
            // 
            // label2
            // 
            resources.ApplyResources(label2, "label2");
            label2.Name = "label2";
            // 
            // Form1
            // 
            resources.ApplyResources(this, "$this");
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add(tabControl1);
            Controls.Add(panel1);
            Name = "Form1";
            Load += Form1_Load;
            panel1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            tabControl1.ResumeLayout(false);
            tabPage1.ResumeLayout(false);
            tabPage2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)pictureDoctorAva).EndInit();
            tabPage3.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion
        private ToolStripTextBox toolStripTextBox1;
        private Panel panel1;
        private PictureBox pictureBox1;
        private Label label1;
        private TabControl tabControl1;
        private TabPage tabPage1;
        private TabPage tabPage2;
        private TabPage tabPage3;
        private Button button1;
        private Label txtAvaivbleDoctors;
        private ListBox listBoxDirections;
        private Label labelDoctorDescription;
        private Label labelDoctorName;
        private ListBox listBox2;
        private PictureBox pictureDoctorAva;
        private Label labelDoctorDiscount;
        private Label labelDoctorPrice;
        private Label labelDoctorDirections;
        private Label labelReciptValue;
        private Label labelReciptDiscount;
        private Label labelResiptCostRaw;
        private Label label2;
        private Button buttonPay;
    }
}
