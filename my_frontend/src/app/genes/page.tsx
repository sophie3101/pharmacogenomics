import React from 'react';
import { createClient } from '@/lib/supabase_server';
import GeneTable from '@/components/tables/table';
// import PagePlaceholder from '@/components/page-placeholder';

// interface GeneRow {
//   symbol: string;
//   chr: string;
// }
export default async function Genes() {
  const supabase = await createClient();
  const { data: genes } = await supabase.from("gene").select().not('url', 'is', null); 
  const genes_ = genes.map((oneGene) => ({
        symbol: oneGene.symbol,
        chr: oneGene.chr,
        ensembleid : oneGene.ensemblid
      }));

  return (
      <div className="flex flex-1 py-4 h-screen sm:h-fit flex-col space-y-2 px-4">
         <GeneTable
          columns={["Symbol", "Chr", "EnsemblID"]}
          data={genes_}
          props={["symbol", "chr", "ensembleid"]}
        />
      </div>
      
   
  )
  // return <pre>{JSON.stringify(genes, null, 2)}</pre>
}