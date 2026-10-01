namespace PavelZhilinDoctorsApp
{
    public partial class Form1 : Form
    {
        private bool _allowTabChange = false;
        private List<Doctor> avaivableDoctors = new List<Doctor>();
        private Doctor chousenDoctor;
        private string[] avaivbleDirections = { "Терапия", "Офтальмология", "Неврология", "Оториноларингология" };
        private string chousenDirection;

        public Form1()
        {
            DBInitiliazer dB = new DBInitiliazer();
            avaivableDoctors = dB.GetDoctorsDB();

            InitializeComponent();

            List<string> newDirections = new List<string>();

            foreach(var doc in avaivableDoctors)
            {
                if (!newDirections.Contains(doc.Directions))
                {
                    newDirections.Add(doc.Directions);
                }
            }

            avaivbleDirections = newDirections.ToArray();
        }

        private void tabControl1_Deselecting(object sender, TabControlCancelEventArgs e)
        {
            if (!_allowTabChange) e.Cancel = true;

            listBox2.Items.Clear();

            foreach (Doctor doctor in DoctorsWithNeededDirection(chousenDirection))
            {
                listBox2.Items.Add(doctor.Name);
            }
        }

        private void btnChooseDirection_Click(object sender, EventArgs e)
        {
            if (listBoxDirections.SelectedItem == null)
            {
                MessageBox.Show("Сначала выбирите направление!", "Неверно");
                return;
            }

            chousenDirection = listBoxDirections.SelectedItem.ToString();

            _allowTabChange = true;
            tabControl1.SelectedTab = tabControl1.TabPages[1];
            _allowTabChange = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (chousenDoctor == null)
            {
                MessageBox.Show("Выбирите специалиста!", "Неверено");
                return;
            }

            _allowTabChange = true;
            tabControl1.SelectedTab = tabControl1.TabPages[2];

            labelResiptCostRaw.Text = "Стоимость: " + chousenDoctor.RawCost.ToString();
            labelReciptDiscount.Text = "Скидка: нет";
            labelReciptValue.Text = "Итого: " + chousenDoctor.RawCost;
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBoxDirections.SelectedItem == null) return;
            chousenDirection = listBoxDirections.SelectedItem.ToString();
            txtAvaivbleDoctors.Text = "Доступно специалистов по этому направлению: " + DoctorsWithNeededDirection(chousenDirection).Count;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listBoxDirections.Items.AddRange(avaivbleDirections);
        }

        private List<Doctor> DoctorsWithNeededDirection(string direction)
        {
            List<Doctor> doctors = new List<Doctor>();

            foreach (var doc in avaivableDoctors)
            {
                if (doc != null && doc.Directions.Contains(direction))
                {
                    doctors.Add(doc);
                }
            }

            return doctors;
        }

        private void listBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox2.SelectedIndex == -1) return;

            Doctor chousenDoc = DoctorsWithNeededDirection(chousenDirection)[listBox2.SelectedIndex];

            labelDoctorName.Text = chousenDoc.Name;
            labelDoctorDescription.Text = "Стаж: " + chousenDoc.Description;
            labelDoctorPrice.Text = "Цена: " + chousenDoc.RawCost;
            labelDoctorDiscount.Text = "Количество: " + chousenDoc.Discount.ToString();
            pictureDoctorAva.Image = Image.FromFile("picture.png");

            string directionText = "";

            foreach (var st in chousenDoc.Directions)
            {
                directionText += st;
            }

            labelDoctorDirections.Text = "Направления: " + directionText;

            chousenDoctor = chousenDoc;
        }

        private void buttonPay_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Павел Жилин 3ИП-1-24", "Успешно", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
