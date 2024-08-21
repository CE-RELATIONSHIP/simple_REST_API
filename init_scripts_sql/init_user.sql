-- Debug Message
SELECT 'Starting table creation...' AS Status;

-- Table Creation
CREATE TABLE IF NOT EXISTS USERS (
    uid VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE,
    name TEXT(255) NOT NULL,
    age INT NOT NULL
);

-- Debug Message
SELECT 'Table created or already exists.' AS Status;

-- Check the structure
DESCRIBE USERS;

-- Debug Message
SELECT 'Script execution completed.' AS Status;