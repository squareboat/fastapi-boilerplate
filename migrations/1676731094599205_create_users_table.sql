[up]
CREATE TABLE users (
    id SERIAL,
    uuid VARCHAR(255),
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TRIGGER update_users_trigger
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE PROCEDURE on_update_timestamp();

[down]
DROP TRIGGER update_users_trigger on users;
DROP TABLE users;
