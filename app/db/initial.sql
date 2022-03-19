CREATE TABLE users(
    id serial PRIMARY KEY,
    name text,
    surname text,
    login text UNIQUE,
    hashed_password text
);
CREATE TABLE tags (
    id serial PRIMARY KEY,
    name text UNIQUE
);
CREATE TABLE tags_employee (
    tags_id integer,
    employee_id integer,
    FOREIGN KEY(tags_id) 
        REFERENCES tags(id),
    FOREIGN KEY(employee_id)
        REFERENCES users(id),
    UNIQUE(tags_id,employee_id)
);
CREATE TABLE employee_data (
    id serial PRIMARY KEY,
    github_url text,
    github_api_key text,
    google_api_key text
);
CREATE TABLE projects (
    id serial PRIMARY KEY,
    employee_id integer,
    name text,
    finished boolean,
    language text,
    FOREIGN KEY(employee_id)
        REFERENCES users(id)
);
CREATE TABLE messages (
    id serial PRIMARY KEY,
    from_user_id integer,
    to_user_id integer,
    message text,
    FOREIGN KEY(from_user_id)
        REFERENCES users(id),
    FOREIGN KEY(to_user_id)
        REFERENCES users(id),
    UNIQUE(from_user_id, to_user_id)
);
CREATE TABLE favorites (
    employee_id integer,
    employer_id integer,
    FOREIGN KEY(employee_id)
        REFERENCES users(id),
    FOREIGN KEY(employer_id)
        REFERENCES users(id),
    UNIQUE(employee_id,employer_id)
);