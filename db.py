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
          price DECIMAL,
          image_url TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    outfits_seed_data = [
        ("Cowboy", 1, 13.98, "https://m.media-amazon.com/images/I/51VmmRDO1EL.__AC_SX300_SY300_QL70_FMwebp_.jpg"),
        ("Rambo Dog", 2, 27.87, "https://m.media-amazon.com/images/I/7167FaSjkWL._AC_SY679_.jpg"),
        ("Cowboy", 2, 12.99, "https://m.media-amazon.com/images/I/41EakiB0FWL.__AC_SX300_SY300_QL70_FMwebp_.jpg")
    ]
    conn.executemany(
        """
        INSERT INTO outfits (name, animal_id, price, image_url)
        VALUES (?,?,?, ?)
        """,
        outfits_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()


def outfits_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM outfits
        """
    ).fetchall()
    return [dict(row) for row in rows]




def outfits_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM outfits
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)

def outfits_create(name, animal_id, price, image_url):
    conn = connect_to_db()
    row = conn.execute(
        """INSERT INTO outfits (name, animal_id, price, image_url)
        VALUES (?,?,?,?)
        RETURNING *
        """,
        (name, animal_id, price, image_url),
    ).fetchone()
    conn.commit()
    return dict(row)

def outfits_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from outfits
        WHERE id = ?
        """,
        id,
    )
    conn.commit()
    return {"message": "Outfit deleted meow meow"}


def outfits_update_by_id(id, name, animal_id, price, image_url):
    conn = connect_to_db() 
    row = conn.execute(
        """
       UPDATE outfits SET name = ?, animal_id = ?, price = ?, image_url = ?
       WHERE id = ?  
       RETURNING *
        """,
        (name, animal_id, price, image_url, id),
    ).fetchone()
    conn.commit()
    return dict(row)