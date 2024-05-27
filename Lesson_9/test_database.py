from sqlalchemy import create_engine

database_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"


def test_database_conection():
    database = create_engine(database_connection_string)
    column_names = database.table_names()
    assert column_names[2] == "emloyee"


