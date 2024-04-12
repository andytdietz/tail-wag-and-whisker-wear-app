import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS outfits;
        """
    )
    conn.execute(
        """
        CREATE TABLE outfits (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          animal_id INTEGER,
          price DECIMAL
          image_url TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    outfits_seed_data = [
        ("Cowboy", "1", 13.98, "https://m.media-amazon.com/images/I/51VmmRDO1EL.__AC_SX300_SY300_QL70_FMwebp_.jpg"),
        ("Rambo Dog", "2", 27.87, "https://m.media-amazon.com/images/I/7167FaSjkWL._AC_SY679_.jpg"),
        ("Cowboy", "2", 12.99, "https://m.media-amazon.com/images/I/41EakiB0FWL.__AC_SX300_SY300_QL70_FMwebp_.jpg")
    ]
    conn.executemany(
        """
        INSERT INTO outfits (name, animal_id, price)
        VALUES (?,?,?)
        """,
        outfits_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()