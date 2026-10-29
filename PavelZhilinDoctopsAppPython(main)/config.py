import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Параметры подключения к PostgreSQL.
# Можно переопределить переменными окружения (PGHOST, PGPORT, PGDATABASE, PGUSER, PGPASSWORD),
# чтобы не хранить пароль в коде.
DB_CONFIG = {
    "host": os.getenv("PGHOST", "localhost"),
    "port": int(os.getenv("PGPORT", "5432")),
    "dbname": os.getenv("PGDATABASE", "clinic_db"),
    "user": os.getenv("PGUSER", "postgres"),
    "password": os.getenv("PGPASSWORD", "224466"),
}

COMPANY_NAME = "Поликлиника"
APP_TITLE = f"Запись к врачу - {COMPANY_NAME}"
