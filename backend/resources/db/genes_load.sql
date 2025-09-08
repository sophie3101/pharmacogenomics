SET search_path TO public;

-- load data into genes table
INSERT INTO genes( HGNC_ID, NCBI_Gene_ID ,Ensembl_ID, Symbol, Gene_Name)
SELECT 
    SPLIT_PART(hgnc_id, ':', 2)::INT AS HGNC_ID,
	ncbi_gene_id, 
	ensembl_id,
	symbol,
	"name"
FROM staging.genes
WHERE has_cpic_dosing_guideline='Yes' AND has_variant_annotation='Yes';

INSERT INTO gene_alternate_names (Gene_ID ,Gene_Alternate_Name )
SELECT genes.gene_id, stg.alternate_names
FROM genes
JOIN staging.genes stg 
    ON stg.symbol = genes.symbol 
WHERE alternate_names IS NOT NULL;


INSERT INTO gene_alternate_symbol (Gene_ID , Gene_Alternate_Symbol )
SELECT genes.gene_id, stg.alternate_symbols
FROM genes
JOIN staging.genes stg 
    ON stg.symbol = genes.symbol 
WHERE stg.alternate_symbols IS NOT NULL;

-- INSERT INTO genetic_location_hg38(Gene_ID INT REFERENCES genes(Gene_ID),
--     chromosome TEXT,
--     START INT,
--     STOP INT)

