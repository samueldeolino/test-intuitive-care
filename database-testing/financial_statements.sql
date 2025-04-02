-- Creating the table
CREATE TABLE IF NOT EXISTS financial_statements (
    data_registro DATE NOT NULL,
    reg_ans VARCHAR(20) NOT NULL,
    cd_conta_contabil VARCHAR(30) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    vl_saldo_inicial DOUBLE(15,2),
    vl_saldo_final DOUBLE(15,2)
);

-- Inserting the data --
-- 2023 --
LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/financial-statements-files/2023/1T2023.csv'
INTO TABLE `financial_statements`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/financial-statements-files/2023/2t2023.csv'
INTO TABLE `financial_statements`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/financial-statements-files/2023/3T2023.csv'
INTO TABLE `financial_statements`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/financial-statements-files/2023/4T2023.csv'
INTO TABLE `financial_statements`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

-- 2024 --
LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/financial-statements-files/2024/1T2024.csv'
INTO TABLE `financial_statements`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/financial-statements-files/2024/2T2024.csv'
INTO TABLE `financial_statements`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/financial-statements-files/2024/3T2024.csv'
INTO TABLE `financial_statements`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/financial-statements-files/2024/4T2024.csv'
INTO TABLE `financial_statements`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS