CREATE TABLE comiverse_db.transactions (
    transaction_id VARCHAR(15),
    transaction_date VARCHAR(50),
    quantity INT,
    unit_cost VARCHAR(10),
    customer_id VARCHAR(15),
    comic_id INT,
    total_amount VARCHAR(10)
);

CREATE TABLE comiverse_db.customers (
    customer_id VARCHAR(15),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    address VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    zip VARCHAR(10),
    phone_number VARCHAR(20),
    loyalty_id INT,
    loyalty_points INT
);

CREATE TABLE comiverse_db.comics (
    comic_id INT,
    title VARCHAR(255),
    binding VARCHAR(10),
    publishing_format VARCHAR(20),
    year_published INT,
    publisher_id INT,
    publisher_name VARCHAR(50),
    unit_cost VARCHAR(10)
);

CREATE TABLE comiverse_db.inventory (
    comic_id INT,
    publisher_id INT,
    unit_cost VARCHAR(10),
    current_stock INT
);
