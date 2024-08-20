-- Debug Message
SELECT 'Starting table creation...' AS Status;

-- Table Creation
CREATE TABLE IF NOT EXISTS USERS (
    uid VARCHAR(255) PRIMARY KEY,
    username TEXT(255),
    age INT
);

-- Debug Message
SELECT 'Table created or already exists.' AS Status;

-- Check the structure
DESCRIBE USERS;

-- Debug Message
SELECT 'Script execution completed.' AS Status;