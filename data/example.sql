-- Drop tables if they already exist
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS logins;
DROP TABLE IF EXISTS messages;

-- Create tables
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    date_registered DATETIME
);

CREATE TABLE logins (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    timestamp DATETIME,
    ip_address VARCHAR(50),
    status VARCHAR(10) -- "success" or "failed"
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    timestamp DATETIME,
    message_text VARCHAR(255)
);

-- Insert data into users
INSERT INTO users (id, username, email, date_registered) VALUES
(1, 'alice', 'alice@example.com', '2023-01-15 10:00:00'),
(2, 'bob', 'bob@example.com', '2023-02-01 11:00:00'),
(3, 'charlie', 'charlie@example.com', '2023-03-10 12:00:00');

-- Insert data into logins
INSERT INTO logins (id, user_id, timestamp, ip_address, status) VALUES
(1, 1, '2024-12-01 12:00:00', '192.168.1.1', 'success'),
(2, 2, '2024-12-01 03:00:00', '10.0.0.1', 'success'),
(3, 2, '2024-12-01 03:05:00', '192.168.1.1', 'failed'),
(4, 3, '2024-12-01 22:00:00', '172.16.0.1', 'success');

-- Insert data into messages
INSERT INTO messages (id, user_id, timestamp, message_text) VALUES
(1, 1, '2024-12-01 13:00:00', 'Hey, how are you?'),
(2, 1, '2024-12-01 14:00:00', 'See you soon!'),
(3, 2, '2024-12-01 03:10:00', 'Send money now!'),
(4, 3, '2024-12-01 22:30:00', 'What’s up?');
