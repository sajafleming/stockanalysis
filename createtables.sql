-- Creates tables in stockanalysis database
CREATE TABLE IF NOT EXISTS raw_data
(
security_name varchar(10),
date varchar(16),
closing_price float
);

CREATE TABLE IF NOT EXISTS analyzed_data
(
security_name varchar(10),
average_closing_price float,
low_closing_price float,
high_closing_price float,
st_dev_closing_price float
);