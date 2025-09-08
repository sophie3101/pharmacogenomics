
CREATE TABLE IF NOT EXISTS genes (
    Gene_ID SERIAL PRIMARY KEY,          
    HGNC_ID INT,
    NCBI_Gene_ID TEXT,
    Ensembl_ID TEXT,
    Symbol TEXT NOT NULL, 
    Gene_Name TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS gene_alternate_names (
    Gene_ID INT REFERENCES genes(Gene_ID),
    Gene_Alternate_Name TEXT
);

CREATE TABLE IF NOT EXISTS gene_alternate_symbol (
    Gene_ID INT REFERENCES genes(Gene_ID),
    Gene_Alternate_Symbol TEXT
);


CREATE TABLE IF NOT EXISTS genetic_location_hg38 (
    Gene_ID INT REFERENCES genes(Gene_ID),
    chromosome TEXT,
    START INT,
    STOP INT
);


CREATE TABLE IF NOT EXISTS genetic_location_hg37 (
    Gene_ID INT REFERENCES genes(Gene_ID),
    chromosome TEXT,
    START INT,
    STOP INT
);
