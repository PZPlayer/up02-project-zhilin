using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PavelZhilinProject
{
    internal class Program
    {
        static void Main(string[] args)
        {
            FirstTask();
            SecondTask();
            ThirdTask();
        }

        private static void FirstTask()
        {
            Task02 task02 = new Task02();

            System.Console.WriteLine("Введите стоимость");
            float num = float.Parse(System.Console.ReadLine());
            System.Console.WriteLine("Введите скидку");
            float discNum = float.Parse(System.Console.ReadLine());
            float discountValue = task02.mineShop.Discount(num, discNum);

            System.Console.WriteLine($"Скидка {discountValue}  К оплтае {num - discountValue}$");
        }

        private static void SecondTask()
        {
            Task02 task02 = new Task02();

            task02.mineShop.WriteDownAllItems();
        }

        private static void ThirdTask()
        {
            Task02 task02 = new Task02();

            task02.mineShop.GiveMeSortedList();
        }
    }

}
