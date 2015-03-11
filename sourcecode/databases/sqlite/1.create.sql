CREATE TABLE category (name TEXT NOT NULL);

INSERT INTO category (name) VALUES
    ('Тапки'),
    ('Самолёты'),
    ('Ноутбуки');


CREATE TABLE product (
    name TEXT NOT NULL,
    price NUMERIC NOT NULL,
    category REFERENCES category(rowid)
);

INSERT INTO product (name, price, category) VALUES
    ('Босоножки', 1.17, 1),
    ('Вьетнамки', 2.36, 1),
    ('Макасины', 4.99, 1),
    ('ИЛ-2', 556000, 2),
    ('Суперджет 100', 1500000, 2),
    ('Ту-160', 25000000, 2),
    ('Dell', 590, 3),
    ('Lenovo', 200, 3),
    ('Sony', 437, 3);
