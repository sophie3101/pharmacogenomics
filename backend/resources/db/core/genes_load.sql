SET search_path TO public;

-- load data into genes table
INSERT INTO genes( pharmgkb_accession_id, HGNC_ID, NCBI_Gene_ID ,Ensembl_ID, Symbol, Gene_Name)
SELECT 
	REGEXP_REPLACE(pharmgkb_accession_id, 'PA', '')::INT ,
    SPLIT_PART(hgnc_id, ':', 2)::INT AS HGNC_ID,
	ncbi_gene_id, 
	ensembl_id,
	symbol,
	"name"
FROM staging.genes
WHERE has_cpic_dosing_guideline='Yes' AND has_variant_annotation='Yes'
ON CONFLICT(Symbol) DO UPDATE SET
	pharmgkb_accession_id=EXCLUDED.pharmgkb_accession_id,
	hgnc_id=EXCLUDED.hgnc_id,
	ncbi_gene_id= EXCLUDED.ncbi_gene_id,
	ensembl_id = EXCLUDED.ensembl_id,
	gene_name = EXCLUDED.gene_name;


-- load data into gene_alternate_names
INSERT INTO gene_alternate_names (Gene_ID, Gene_Alternate_Name)
SELECT genes.gene_id, stg.alternate_names
FROM genes
JOIN staging.genes stg 
    ON stg.symbol = genes.symbol 
WHERE alternate_names IS NOT NULL
ON CONFLICT(Gene_ID ,Gene_Alternate_Name) DO UPDATE SET 
	Gene_Alternate_Name=EXCLUDED.Gene_Alternate_Name;

-- load data into gene_alternate_symbol
INSERT INTO gene_alternate_symbol (Gene_ID, Gene_Alternate_Symbol)
SELECT gene_id, TRIM(gene_symbol)
FROM (
	SELECT 
		genes.gene_id, 
		UNNEST(STRING_TO_ARRAY(stg.alternate_symbols, ',')) AS gene_symbol
	FROM genes
	JOIN staging.genes stg 
		ON stg.symbol = genes.symbol 
	WHERE stg.alternate_symbols IS NOT NULL
)
ON CONFLICT(Gene_ID ,Gene_Alternate_Symbol) DO UPDATE SET 
	Gene_Alternate_Symbol=EXCLUDED.Gene_Alternate_Symbol;
	;

-- load data into genetic_location_hg37
INSERT INTO genetic_location_hg37(Gene_ID , chromosome ,"start", "stop")
SELECT 
	genes.gene_id, 
	REGEXP_REPLACE(stg.chromosome,'chr', ''), 
	stg.chromosomal_start_grch37::INT, 
	chromosomal_stop_grch37::INT
FROM genes
JOIN staging.genes stg 
	ON stg.symbol = genes.symbol
ON CONFLICT(Gene_ID) DO UPDATE SET 
	 chromosome = EXCLUDED.chromosome,
	 "start" =  EXCLUDED.start,
	 "stop" = EXCLUDED.stop
 ;

-- load data into genetic_location_hg38
INSERT INTO genetic_location_hg38( Gene_ID, chromosome, "start", "stop")
SELECT 
	genes.gene_id, 
	REGEXP_REPLACE(stg.chromosome,'chr', ''), 
	stg.chromosomal_start_grch38::INT, 
	chromosomal_stop_grch38::INT
FROM genes
JOIN staging.genes stg 
	ON stg.symbol = genes.symbol
ON CONFLICT(Gene_ID) DO UPDATE SET 
	 chromosome = EXCLUDED.chromosome,
	 "start" =  EXCLUDED.start,
	 "stop"= EXCLUDED.stop;




