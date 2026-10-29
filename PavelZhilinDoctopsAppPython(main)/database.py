from contextlib import contextmanager

import psycopg2

from config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


@contextmanager
def db_cursor():
    """Курсор с транзакцией: commit при успехе, rollback при ошибке, соединение закрывается."""
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                yield cur
    finally:
        conn.close()


def get_all_products():
    """Список врачей. Порядок полей:
    0 id, 1 специальность, 2 ФИО, 3 стаж, 4 цена, 5 свободных талонов, 6 фото."""
    with db_cursor() as cur:
        cur.execute("""
            SELECT d.id, s.name, d.full_name, d.experience_years,
                   CAST(d.price AS DOUBLE PRECISION), d.slots, d.photo
            FROM doctors d
            JOIN specialties s ON s.id = d.specialty_id
            ORDER BY d.id
        """)
        return cur.fetchall()


def get_product_quantity(product_id):
    """Свободных талонов у врача (число, а не кортеж)."""
    with db_cursor() as cur:
        cur.execute("SELECT slots FROM doctors WHERE id = %s", (product_id,))
        row = cur.fetchone()
        return row[0] if row else 0


def get_user_by_login(login):
    """(id, логин, ФИО, роль) или None."""
    with db_cursor() as cur:
        cur.execute("""
            SELECT u.id, u.login, u.full_name, r.name
            FROM users u
            JOIN roles r ON r.id = u.role_id
            WHERE u.login = %s
        """, (login,))
        return cur.fetchone()
