using Microsoft.Data.Sqlite;
using Microsoft.EntityFrameworkCore;
namespace PavelZhilinDoctorsApp
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            Application.Run(new Form1());
        }
    }

    public class DBInitiliazer
    {

        public List<Doctor> GetDoctorsDB()
        {
            List<Doctor> Doctors = new List<Doctor>();

            using var conn = new SqliteConnection("Data Source=db_variant_8.db");
            conn.Open();
            var command = conn.CreateCommand();
            command.CommandText = "SELECT id, специальность, фио, стаж, цена, количество, фото FROM Товар";

            var reader = command.ExecuteReader();

            while (reader.Read())
            {
                Doctor doctor = new Doctor(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetInt32(3), reader.GetFloat(4), reader.GetInt32(5), reader.GetString(6));
                Doctors.Add(doctor);
            }

            return Doctors;
        }
    }

    public class Doctor
    {
        public string Name = "";
        public int Description = 1;
        public string ImagePath = "";
        public string Directions = "";
        public float RawCost;
        public int Discount;

        public int ID;

        public Doctor(int id, string directions, string name, int description, float rawCost, int discount = 1, string imagePath = "picture.png")
        {
            Name = name;
            ID = id;
            Description = description;
            Directions = directions;
            RawCost = rawCost;
            Discount = discount;
            ImagePath = imagePath;
        }
    }
}