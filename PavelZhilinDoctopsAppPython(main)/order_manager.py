from database import db_cursor


def get_all_orders():
    """(id, дата, ФИО клиента)"""
    with db_cursor() as cur:
        cur.execute("""
            SELECT o.id, o.order_date, u.full_name
            FROM orders o
            JOIN users u ON u.id = o.client_id
            ORDER BY o.id DESC
        """)
        return cur.fetchall()


def get_order(order_id):
    """(id, дата, ФИО клиента) или None"""
    with db_cursor() as cur:
        cur.execute("""
            SELECT o.id, o.order_date, u.full_name
            FROM orders o
            JOIN users u ON u.id = o.client_id
            WHERE o.id = %s
        """, (order_id,))
        return cur.fetchone()


def get_order_item(order_id):
    """Позиции заказа (JOIN): id позиции, специальность, ФИО врача, стаж, дата, цена, количество."""
    with db_cursor() as cur:
        cur.execute("""
            SELECT oi.id, s.name, d.full_name, d.experience_years,
                   o.order_date, CAST(oi.price AS DOUBLE PRECISION), oi.quantity
            FROM order_items oi
            JOIN orders o      ON o.id = oi.order_id
            JOIN doctors d     ON d.id = oi.doctor_id
            JOIN specialties s ON s.id = d.specialty_id
            WHERE oi.order_id = %s
            ORDER BY oi.id
        """, (order_id,))
        return cur.fetchall()


def get_order_total(order_id):
    with db_cursor() as cur:
        cur.execute("""
            SELECT SUM(quantity * price) FROM order_items WHERE order_id = %s
        """, (order_id,))
        row = cur.fetchone()
        return float(row[0]) if row and row[0] is not None else 0.0


def create_order(client_id, items):
    """Создаёт заказ одной транзакцией.
    items: список (doctor_id, quantity, price). Возвращает id заказа.
    Если талонов не хватает — ValueError, ничего не сохраняется (rollback)."""
    with db_cursor() as cur:
        cur.execute("INSERT INTO orders (client_id) VALUES (%s) RETURNING id", (client_id,))
        order_id = cur.fetchone()[0]

        for doctor_id, quantity, price in items:
            # FOR UPDATE блокирует строку врача, пока идёт транзакция — защита от двойной записи
            cur.execute("SELECT slots FROM doctors WHERE id = %s FOR UPDATE", (doctor_id,))
            row = cur.fetchone()
            if not row or row[0] < quantity:
                raise ValueError(f"Недостаточно свободных талонов (врач id={doctor_id})")
            cur.execute("""
                INSERT INTO order_items (order_id, doctor_id, quantity, price)
                VALUES (%s, %s, %s, %s)
            """, (order_id, doctor_id, quantity, price))
            cur.execute("UPDATE doctors SET slots = slots - %s WHERE id = %s",
                        (quantity, doctor_id))
        return order_id


def delete_order(order_id):
    """Удаляет заказ и возвращает талоны врачам (позиции удалятся каскадом)."""
    with db_cursor() as cur:
        # суммируем по врачу: UPDATE ... FROM применяется только один раз на строку,
        # поэтому если врач встречается в заказе дважды, считаем сумму заранее
        cur.execute("""
            UPDATE doctors AS d
            SET slots = d.slots + t.qty
            FROM (SELECT doctor_id, SUM(quantity) AS qty
                  FROM order_items WHERE order_id = %s GROUP BY doctor_id) t
            WHERE t.doctor_id = d.id
        """, (order_id,))
        cur.execute("DELETE FROM orders WHERE id = %s", (order_id,))
        return cur.rowcount > 0


def update_order_date(order_id, new_date):
    with db_cursor() as cur:
        cur.execute("UPDATE orders SET order_date = %s WHERE id = %s", (new_date, order_id))
        return cur.rowcount > 0


def delete_order_item(item_id):
    """Удаляет позицию заказа и возвращает талоны врачу."""
    with db_cursor() as cur:
        cur.execute("SELECT doctor_id, quantity FROM order_items WHERE id = %s", (item_id,))
        row = cur.fetchone()
        if not row:
            return False
        doctor_id, quantity = row
        cur.execute("DELETE FROM order_items WHERE id = %s", (item_id,))
        cur.execute("UPDATE doctors SET slots = slots + %s WHERE id = %s", (quantity, doctor_id))
        return True
