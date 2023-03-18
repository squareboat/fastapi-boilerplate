[up]
CREATE TABLE jobs (
    id SERIAL,
    uuid VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    created_by_id INTEGER,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TRIGGER update_jobs_trigger
BEFORE UPDATE ON jobs
FOR EACH ROW
EXECUTE PROCEDURE on_update_timestamp();

[down]
DROP TRIGGER update_jobs_trigger on jobs;
DROP TABLE jobs;
