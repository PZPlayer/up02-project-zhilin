import tkinter as tk
from tkinter import ttk, messagebox
from styles import *
import order_manager as om


class OrdersWindow:
    def __init__(self, parent, current_user=None):
        self.current_user = current_user

        self.window = tk.Toplevel(parent)
        self.window.title("Список заказов")
        self.window.geometry("800x500")
        self.window.configure(bg=COLOR_MAIN_BG)

        self.build_ui()
        self.load_orders()

    def is_admin(self):
        return bool(self.current_user and self.current_user[3] == "Администратор")

    def build_ui(self):
        self.tree = ttk.Treeview(self.window, columns=("id", "date", "client"),
                                 show="headings", height=15)
        self.tree.heading("id", text="№")
        self.tree.heading("date", text="Дата")
        self.tree.heading("client", text="Клиент")
        self.tree.column("id", width=50)
        self.tree.column("date", width=120)
        self.tree.column("client", width=400)
        self.tree.pack(fill="x", expand=True, padx=20, pady=20)
        self.tree.bind("<Double-1>", self.on_order_select)

        btn_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", padx=20, pady=10)
        tk.Button(btn_frame, text="Просмотр состава",
                  command=self.on_order_select, bg=COLOR_ACCENT, fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Обновить",
                  command=self.load_orders, bg=COLOR_ACCENT, fg="white").pack(side="left", padx=5)
        if self.is_admin():
            tk.Button(btn_frame, text="Удалить заказ",
                      command=self.delete_selected, bg=COLOR_HIGHLIGHT, fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Назад",
                  command=self.window.destroy, bg=COLOR_ACCENT, fg="white").pack(side="right")

    def load_orders(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            orders = om.get_all_orders()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить заказы: {e}")
            return
        for order in orders:
            self.tree.insert("", tk.END, iid=order[0], values=order)

    def _selected_id(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Ошибка", "Выбери сначала заказ")
            return None
        return int(selected[0])

    def on_order_select(self, event=None):
        order_id = self._selected_id()
        if order_id is None:
            return
        from order_items_window import OrderItemssWindow
        OrderItemssWindow(self.window, order_id, self.current_user)

    def delete_selected(self):
        order_id = self._selected_id()
        if order_id is None:
            return
        if not messagebox.askyesno("Удаление", f"Удалить заказ №{order_id}? Талоны вернутся врачам."):
            return
        if om.delete_order(order_id):
            self.load_orders()
