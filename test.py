import logging
from gtf_to_genes import *
import pdb


if __name__=="__main__":

    fn_idx = "/global/scratch/psudmant/genomes/ensembl/release-75/gtf.index"

    logger = logging.getLogger("./log.txt")
    ID = "Rattus_norvegicus:75"
    s_id, path, genes = get_indexed_genes_for_identifier(fn_idx, logger, ID)
    print(genes) 
    pdb.set_trace()

