
CREATE TABLE IF NOT EXISTS genes (
    Gene_ID SERIAL PRIMARY KEY,  
    pharmgkb_accession_id INT,       
    HGNC_ID INT,
    NCBI_Gene_ID TEXT,
    Ensembl_ID TEXT,
    Symbol TEXT UNIQUE NOT NULL, 
    Gene_Name TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS gene_alternate_names (
    Gene_ID INT REFERENCES genes(Gene_ID) NOT NULL,
    Gene_Alternate_Name TEXT,
    UNIQUE(Gene_ID, Gene_Alternate_Name)
);

CREATE TABLE IF NOT EXISTS gene_alternate_symbol (
    Gene_ID INT REFERENCES genes(Gene_ID) NOT NULL,
    Gene_Alternate_Symbol TEXT,
    UNIQUE(Gene_ID, Gene_Alternate_Symbol)
);


CREATE TABLE IF NOT EXISTS genetic_location_hg38 (
    Gene_ID INT REFERENCES genes(Gene_ID) UNIQUE NOT NULL,
    chromosome TEXT,
    START INT,
    STOP INT
);


CREATE TABLE IF NOT EXISTS genetic_location_hg37 (
    Gene_ID INT REFERENCES genes(Gene_ID) UNIQUE NOT NULL,
    chromosome TEXT,
    START INT,
    STOP INT
);
