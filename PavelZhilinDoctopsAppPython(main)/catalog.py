import tkinter as tk
from styles import (
    COLOR_MAIN_BG, COLOR_HIGHLIGHT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, font
)
from resources import get_product_image

LOW_STOCK_LIMIT = 3  # врачи с количеством талонов <= 3 подсвечиваются


def create_product_card(parent, product, refresh=None, get_user=None):
    qty = product[5]
    bg_color = _get_card_color(qty)
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)
    _add_image(card, product, bg_color)
    _add_text_info(card, product, bg_color, qty)
    _bind_click(card, lambda e: _open_view(parent, product, refresh, get_user))


def _bind_click(widget, handler):
    """Клик срабатывает на карточке и на всех вложенных элементах."""
    widget.bind("<Button-1>", handler)
    for child in widget.winfo_children():
        _bind_click(child, handler)


def _get_card_color(qty):
    return COLOR_HIGHLIGHT if qty <= LOW_STOCK_LIMIT else COLOR_MAIN_BG


def _add_image(card, product, bg_color):
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)
    photo = get_product_image(product[6], size=(100, 100))
    if photo:
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo
        img_label.pack()
    else:
        tk.Label(img_frame, text="[НЕТ ФОТО]", bg=bg_color, width=10, height=5).pack()


def _add_text_info(card, product, bg_color, qty):
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    speciality = product[1] if product[1] else "[БЕЗ СПЕЦИАЛЬНОСТИ]"
    name = product[2] if product[2] else "[БЕЗ ФИО]"
    exp = product[3] if product[3] is not None else "[БЕЗ СТАЖА]"
    price = product[4] if product[4] is not None else 0
    _add_label(text_frame, f"{speciality} | {name}", bg_color, bold=True, size=FONT_SIZE_HEADER)
    _add_label(text_frame, f"Стаж: {exp} лет", bg_color, bold=False, size=FONT_SIZE_NORMAL)
    _add_label(text_frame, f"Свободных талонов: {qty}", bg_color, bold=False, size=FONT_SIZE_NORMAL)
    _add_label(text_frame, f"Цена: {price:g} руб.", bg_color, bold=True, size=FONT_SIZE_NORMAL, align="e")


def _add_label(parent, text, bg_color, bold=False, size=FONT_SIZE_NORMAL, align="w"):
    tk.Label(parent, text=text, font=font(size, bold=bold), bg=bg_color, anchor=align).pack(fill="x")


def _open_view(parent, product, refresh=None, get_user=None):
    from view_form import ViewForm
    ViewForm(parent, product, on_add_to_order=refresh, get_user=get_user)
