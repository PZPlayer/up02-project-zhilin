import tkinter as tk
from tkinter import messagebox
from styles import *
from resources import get_product_image
from database import get_product_quantity
from order_manager import create_order
from error_handler import validate_positive_int


class ViewForm:
    def __init__(self, parent, product, on_add_to_order=None, get_user=None):
        self.product = product
        self.on_add_to_order = on_add_to_order
        self.get_user = get_user

        self.window = tk.Toplevel(parent)
        self.window.title(f"Просмотр - {product[1]}")
        self.window.geometry("700x600")
        self.window.configure(bg=COLOR_MAIN_BG)

        self.build_ui()

    def build_ui(self):
        header = tk.Label(
            self.window,
            text=f"{self.product[1] or 'Без направления'} | {self.product[2] or 'Без ФИО'}",
            font=font(FONT_SIZE_TITLE, bold=True),
            bg=COLOR_MAIN_BG, fg=COLOR_ACCENT
        )
        header.pack(pady=10)

        photo = get_product_image(self.product[6], size=(150, 150))
        if photo:
            img_label = tk.Label(self.window, image=photo, bg=COLOR_MAIN_BG)
            img_label.image = photo
            img_label.pack(pady=5)

        info = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        info.pack(fill="x", padx=20, pady=10)

        self._add_field(info, "Направление", self.product[1] or "-")
        self._add_field(info, "ФИО", self.product[2] or "-")
        self._add_field(info, "Стаж", f"{self.product[3]} лет" if self.product[3] is not None else "-")
        self._add_field(info, "Цена", f"{self.product[4]:g} руб.")
        self._add_field(info, "Свободно талонов", get_product_quantity(self.product[0]))

        qty_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        qty_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(qty_frame, text="Количество:", font=font(bold=True),
                 bg=COLOR_MAIN_BG).pack(side="left")

        self.qty_var = tk.StringVar(value="1")
        tk.Entry(qty_frame, textvariable=self.qty_var, width=10).pack(side="left", padx=10)

        btn_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", padx=20, pady=20)

        tk.Button(btn_frame, text="Записаться",
                  command=self.add_to_order,
                  bg=COLOR_ACCENT, fg="white", width=20).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Закрыть",
                  command=self.window.destroy,
                  bg=COLOR_SECONDARY_BG, fg="black", width=15).pack(side="left", padx=5)

    def _add_field(self, parent, label, value):
        row = tk.Frame(parent, bg=COLOR_MAIN_BG)
        row.pack(fill="x", pady=2)
        tk.Label(row, text=f"{label}:", font=font(bold=True), bg=COLOR_MAIN_BG,
                 width=15, anchor="w").pack(side="left")
        tk.Label(row, text=str(value), font=font(), bg=COLOR_MAIN_BG,
                 anchor="w").pack(side="left")

    def add_to_order(self):
        user = self.get_user() if self.get_user else None
        if not user:
            messagebox.showerror("Ошибка", "Сначала авторизуйся")
            return

        ok, result = validate_positive_int(self.qty_var.get(), "Количество")
        if not ok:
            messagebox.showerror("Ошибка ввода", result)
            return
        qty = result

        current_qty = get_product_quantity(self.product[0])
        if qty > current_qty:
            messagebox.showwarning("Ошибка", f"Доступно только {current_qty} шт.")
            return
        try:
            # раньше сюда попадало self.product[5] (весь остаток), а не введённое количество
            items = [(self.product[0], qty, self.product[4])]
            order_id = create_order(user[0], items)
            messagebox.showinfo("Успех", f"Заказ №{order_id} оформлен")
            if self.on_add_to_order:
                self.on_add_to_order()
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка заказа: \n{e}")
