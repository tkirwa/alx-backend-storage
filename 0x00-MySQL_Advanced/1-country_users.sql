-- Create the users table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

-- Sample data
INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");
INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");
INSERT INTO users (email, name, country) VALUES ("john@dylan.com", "John", "US");
