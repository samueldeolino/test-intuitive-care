-- Creating the table --
CREATE TABLE IF NOT EXISTS active_health_plan_operators (
    registro_ans VARCHAR(20) NOT NULL,
    cnpj CHAR(14) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep CHAR(8),
    ddd CHAR(2),
    telefone VARCHAR(15),
    fax VARCHAR(15),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao TEXT,
    data_registro_ans DATE
);

-- Inserting the data --
LOAD DATA LOCAL INFILE '/home/samuel-deolino/Desktop/test-intuitive-care/database-testing/csv-active-operators-files/Relatorio_cadop.csv'
INTO TABLE `active_health_plan_operators`
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS