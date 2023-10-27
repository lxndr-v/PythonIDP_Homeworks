CREATE TABLE IF NOT EXISTS projects (
    project_id serial PRIMARY KEY,
    project_name VARCHAR(50) UNIQUE NOT NULL,
    customers_country VARCHAR(50),
    project_type VARCHAR(50),
    number_of_devs FLOAT,
    number_of_qas FLOAT,
    project_duration FLOAT
);

CREATE TABLE IF NOT EXISTS results (
    result_id serial PRIMARY KEY,
    project_id INT NOT NULL,
    devs_price_per_month FLOAT,
    qas_price_per_month FLOAT,
    devs_and_qas_price_per_year FLOAT,
    project_info TEXT,
    CONSTRAINT fk_project
        FOREIGN KEY (project_id) 
        REFERENCES projects(project_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
