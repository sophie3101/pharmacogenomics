CREATE TABLE IF NOT EXISTS  staging.genes (
    "pharmgkb_accession_id" TEXT,
    "ncbi_gene_id" TEXT,
    "hgnc_id" TEXT,
    "ensembl_id" TEXT,
    "name" TEXT,"symbol" TEXT,
    "alternate_names" TEXT,
    "alternate_symbols" TEXT,
    "is_vip" TEXT,
    "has_variant_annotation" TEXT,
    "cross-references" TEXT,
    "has_cpic_dosing_guideline" TEXT,
    "chromosome" TEXT,
    "chromosomal_start_grch37" TEXT,
    "chromosomal_stop_grch37" TEXT,
    "chromosomal_start_grch38" TEXT,
    "chromosomal_stop_grch38" TEXT
)