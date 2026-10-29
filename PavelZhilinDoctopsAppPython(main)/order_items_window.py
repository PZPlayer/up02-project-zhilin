import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from styles import *
import order_manager as om


class OrderItemssWindow:
    def __init__(self, parent, order_id, current_user=None):
        self.current_user = current_user
        self.order_id = order_id

        self.window = tk.Toplevel(parent)
        self.window.title(f"Состав заказа {order_id}")
        self.window.geometry("900x600")
        self.window.configure(bg=COLOR_MAIN_BG)

        self.build_ui()
        self.load_order_info()
        self.load_items()

    def is_admin(self):
        return bool(self.current_user and self.current_user[3] == "Администратор")

    def build_ui(self):
        info_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        info_frame.pack(fill="x", padx=20, pady=10)
        tk.Label(info_frame, text="Дата заказа:", font=font(bold=True),
                 bg=COLOR_MAIN_BG).pack(side="left")
        self.date_var = tk.StringVar()
        self.date_entry = tk.Entry(info_frame, textvariable=self.date_var, width=15, state="readonly")
        self.date_entry.pack(side="left", padx=5)
        if self.is_admin():  # только администратор может править дату
            self.date_entry.config(state="normal")
            tk.Button(info_frame, text="Сохранить дату",
                      command=self.save_data, font=font(bold=True)).pack(side="left")
        tk.Label(info_frame, text="Клиент:", font=font(bold=True),
                 bg=COLOR_MAIN_BG).pack(side="left", padx=(20, 0))
        self.client_label = tk.Label(info_frame, text="", font=font(bold=True), bg=COLOR_MAIN_BG)
        self.client_label.pack(side="left")

        columns = ("id", "name", "speciality", "quantity", "price", "total")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings", height=12)
        self.tree.heading("id", text="№")
        self.tree.heading("name", text="ФИО")
        self.tree.heading("speciality", text="Специальность")
        self.tree.heading("quantity", text="Количество")
        self.tree.heading("price", text="Цена")
        self.tree.heading("total", text="Итого")
        self.tree.column("id", width=50)
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        self.total_label = tk.Label(self.window, text="",
                                    font=font(FONT_SIZE_NORMAL, bold=True),
                                    fg=COLOR_ACCENT, bg=COLOR_MAIN_BG)
        self.total_label.pack(pady=5)

        btn_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", padx=20, pady=10)
        if self.is_admin():
            tk.Button(btn_frame, text="Удалить позицию",
                      command=self.delete_item, bg=COLOR_HIGHLIGHT, fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Обновить", command=self.refresh_all).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Назад", command=self.window.destroy).pack(side="right")

    def load_order_info(self):
        order = om.get_order(self.order_id)
        if order:
            _, order_date, client = order
            self.date_var.set(str(order_date))
            self.client_label.config(text=client)

    def load_items(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            items = om.get_order_item(self.order_id)
            if not items:
                self.total_label.config(text="Позиций нет")
                return
            for item in items:
                item_id, speciality, name, years, date, price, quantity = item
                self.tree.insert("", tk.END,
                                 values=(item_id, name, speciality, quantity,
                                         f"{price:g}", f"{quantity * price:g}"))
            self.total_label.config(text=f"ИТОГО: {om.get_order_total(self.order_id):g} руб.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {e}")

    def save_data(self):
        new_date = self.date_var.get().strip()
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Ошибка", "Формат даты: ГГГГ-ММ-ДД")
            return
        if om.update_order_date(self.order_id, new_date):
            messagebox.showinfo("Успех", "Дата обновлена")

    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Ошибка", "Выбери позицию")
            return
        item_id = int(self.tree.item(selected[0], "values")[0])
        if not messagebox.askyesno("Удаление", "Удалить позицию? Талоны вернутся врачу."):
            return
        if om.delete_order_item(item_id):
            messagebox.showinfo("Успех", "Позиция удалена")
            self.refresh_all()

    def refresh_all(self):
        self.load_order_info()
        self.load_items()
