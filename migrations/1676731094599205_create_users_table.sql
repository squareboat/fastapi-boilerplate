[up]
CREATE TABLE users (
    id INTEGER,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TRIGGER update_users_trigger
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE PROCEDURE on_update_timestamp();

[down]
DROP FUNCTION on_update_timestamp;
DROP TRIGGER update_users_trigger on users;
DROP TABLE users;
