using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PavelZhilinProject
{
    public class Item
    {
        public string Name { get; set; }

        public float Cost;
    }

    internal class Task02
    {
        public Shop mineShop = new Shop(new Dictionary<Item, int>());

        public Task02()
        {
            Item Carrot = new Item();
            Carrot.Name = "Морковь";
            Carrot.Cost = 100f;

            Item Potato = new Item();
            Potato.Name = "Картошка";
            Potato.Cost = 80f;

            mineShop.AddItemToCart(Carrot);
            mineShop.AddItemToCart(Potato, 3);
            mineShop.AddItemToCart(Carrot);
        }
    }

    public class Shop
    {
        private Dictionary<Item, int> items = new Dictionary<Item, int>();

        public Shop(Dictionary<Item, int> itms)
        {
            items = itms;
        }

        public bool AddItemToCart(Item item, int howMuch = 1)
        {
            if (items.ContainsKey(item))
            {
                items[item] += howMuch;

                return true;
            }

            items.Add(item, howMuch);
            return true;
        }

        public float Discount(float cost, float procentageDiscount)
        {
            return cost * procentageDiscount;
        }

        public void GiveMeSortedList()
        {
            var sorted = items
                .OrderByDescending(kvp => kvp.Value)
                .ToList();

            int itemNum = 0;
            foreach (var kvp in sorted)
            {
                var item = kvp.Key;
                var qty = kvp.Value;
                var lineTotal = (item?.Cost ?? 0f) * qty;
                string value = qty > 2 ? "Много" : "Мало";
                Console.WriteLine($"{itemNum}.{item?.Name} Кол-во {qty}   {value}");
                itemNum++;
            }
        }

        public void WriteDownAllItems()
        {
            int itemNum = 0;
            float total = 0;

            foreach (var item in items)
            {
                total += item.Key.Cost * item.Value;
                Console.WriteLine($"{itemNum.ToString()}.{item.Key.Name} {item.Key.Cost} * Кол-во {item.Value}   | {item.Key.Cost * item.Value}");
                itemNum++;
            }

            Console.WriteLine($"\nИТОГО: {total}$");
        }

        ~Shop()
        {
            items.Clear();
        }
    }

}
