import logging
import sys

import masst_batch_client
import masst_utils

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

files = [
    #  (r"../examples/wender_plants.csv", "../output/example/feature"),
    # (r"../examples/input_spectra.mgf", "../output/examples/test"),
    # ("/Users/shipei/Documents/projects/conjugated_metabolome/identification/lac_eg/data/lac_ref_spec.tsv", 
    #  "/Users/shipei/Documents/projects/conjugated_metabolome/identification/lac_eg/data/masst_results/lac"),
    
    # ("/Users/shipei/Documents/projects/conjugated_metabolome/identification/phe_eg/data/phe_ref_spec.tsv", 
    #  "/Users/shipei/Documents/projects/conjugated_metabolome/identification/phe_eg/data/masst_results/phe"),
    
    # ("/Users/shipei/Documents/projects/multiplex_synthesis/target_drugs/all/target.tsv",
    #  "/Users/shipei/Documents/projects/multiplex_synthesis/target_drugs/all/masst_0.7_3/target")
    
    # ("/Users/shipei/Documents/projects/conjugated_metabolome/identification/PEA/steroid/data/targets.tsv",
    #  "/Users/shipei/Documents/projects/conjugated_metabolome/identification/PEA/steroid/data/masst_results/targets"),
    
    ("/Users/shipei/Documents/projects/conjugated_metabolome/identification/losartan/masst/target.tsv",
     "/Users/shipei/Documents/projects/conjugated_metabolome/identification/losartan/masst/masst_results/target"),

]

if __name__ == "__main__":
    for file, out_file in files:
        try:
            logger.info("Starting new job for input: {}".format(file))
            sep = "," if file.endswith("csv") else "\t"  # only used if tabular format not for mgf
            
            masst_batch_client.run_on_usi_list_or_mgf_file(
                in_file=file,
                out_file_no_extension=out_file,
                min_cos=0.7,
                mz_tol=0.05,
                precursor_mz_tol=0.05,
                min_matched_signals=4,
                database=masst_utils.DataBase.metabolomicspanrepo_index_nightly,
                parallel_queries=5,
                skip_existing=True,
                analog=False,
                sep=sep,
                usi_or_lib_id="usi",  # column name for USI or library ID in tabular format
                compound_name_header="name"  # column name for compound name (unique ID) in tabular format
            )
        except:
            pass
    # exit with OK
    sys.exit(0)
    