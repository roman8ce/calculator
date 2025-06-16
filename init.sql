CREATE EXTENSION IF NOT EXISTS "uuid-ossp";               

CREATE TABLE IF NOT EXISTS calculation_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    expression VARCHAR(100) NOT NULL, 
    result NUMERIC, error_message TEXT, 
    date_and_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );