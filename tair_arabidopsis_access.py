import os
import gzip
import arguably 
import wget
import requests
@pp.profile(sort_by='cumulative', out_lines=30) 
@pp.profile_by_line(exit=1) 
@pp.simple_timer(num=1)
snap = CodeSnap()
snap = CodeSnap(tracer="python") 
snap.start()
@arguably.Command
def tairStandlone(uniprot_agi = FALSE, 
                  agi_uniprot = FALSE,  
                  uniprot_tair = FALSE, 
                  tair_protein_models = FALSE,
                  all_ua_au_ut_tpm = FALSE)
"""
a streamline function to make the tair dataframe at 
your end for making the gosling maps for annotations
visualization. It gives several conversion utilities
and interacts directly with the TAIR database and 
also gives the AGI and the coordinates and all the information 
in one output as a nested dictionary. To search for a single id 
or multiple ids, please set all the options to TRUE to get the 
complete information. PATH to the tair_protein_models file is 
required for the analysis of the protein models.
"""
import wget
#uniprot_agi_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/Uniprot2AGI-JAN2023.txt"
#agi_uniprot_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/AGI2uniprot-JAN2023.txt"
#uniprot_tair_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/TAIR2UniprotMapping-JAN2023.txt"
if uniprot_agi:
    uniprot_agi_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/Uniprot2AGI-Jul2023.txt"
    wget.download(uniprot_agi_url)
    uniprot_agi = {}
    with open(os.path.abspath(os.path.join(os.getcwd(), "Uniprot2AGI-Jul2023.txt")), "r") as uni:
        for line in uni.readlines():
            uniprot_agi["uniprot", line.strip().split("\t")[0]] = \
                             {"AGI":line.strip().split("\t")[1:]}
    os.remove(os.path.abspath(os.path.join(os.getcwd(), "Uniprot2AGI-Jul2023.txt"))
if agi_uniprot:
    agi_uniprot_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/AGI2uniprot-Jul2023.txt"
    wget.download(agi_uniprot_url)
    agi_uniprot = {}
    with open(os.path.abspath(os.path.join(os.getcwd(), "AGI2uniprot-Jul2023.txt")), "r") as agi:
        for line in agi.readlines():
            agi_uniprot["AGI",line.strip().split("\t")[0]] = \
                              {"uniprot_identifier": line.strip().split("\t")[1:]}
    os.remove(os.path.join(os.getcwd(), "AGI2uniprot-Jul2023.txt"))                          
if uniprot_tair:
    uniprot_tair_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/TAIR2UniprotMapping-Jul2023.txt"
    wget.download(uniprot_tair_url)
    uniprot_tair = {}
    with open(os.path.abspath(os.path.join(os.getcwd(), "TAIR2UniprotMapping-Jul2023.txt")), "r") as tair:
        for line in tair.readlines():
            tair_uniprot["uniprot", line.strip().split("\t")[0]] = \
                            {"locus_tair_ID":line.strip().split("\t")[1:]}
    os.remove(os.path.join(os.getcwd(), "TAIR2UniprotMapping-Jul2023.txt"))                        
if tair_protein_models:
    tair_protein_models = {}
    with open(os.path.abspath(os.path.join(os.getcwd(), "Araport11_pep_20220914_representative_gene_model")), "r") as protein:
        for line in protein.readlines():
            if line.startswith(">"):
                tair_protein_models["AGI",line.strip().split("|")[0].replace(">", "")] = \
                       {"chromosome": line.strip().split("|")[3].replace(" ", "_").replace("LENGTH=", "")}              
    os.remove(os.path.join(os.getcwd(), "Araport11_pep_20220914_representative_gene_model"))
if all_ua_au_ut_tpm:
    for file in os.walk("directory"):
        for i in file:
            if i == "Uniprot2AGI-JAN2023.txt" and "AGI2uniprot-JAN2023.txt" and "TAIR2UniprotMapping-JAN2023.txt":
                print(f"Already the files to analyze from the TAIR are \
                           availables in the present working directory")
            if i !="Uniprot2AGI-JAN2023.txt" and "AGI2uniprot-JAN2023.txt" and "TAIR2UniprotMapping-JAN2023.txt":
                print(f"the annotation files from the TAIR are not present and fetching them for the analysis")
                uniprot_agi_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/Uniprot2AGI-Jul2023.txt"
                agi_uniprot_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/AGI2uniprot-Jul2023.txt"
                uniprot_tair_url = "https://www.arabidopsis.org/download_files/Proteins/Id_conversions/TAIR2UniprotMapping-Jul2023.txt"
                wget.download(uniprot_agi_url)
                wget.download(agi_uniprot_url)
                wget.download(uniprot_tair_url)
                print(f"{[i for files in os.walk(os.getcwd()) for i in files if i.endswith(".txt")]}")
uniprot_agi = {}
agi_uniprot = {}
uniprot_tair = {}
tair_protein_models = {}
with open(os.path.abspath(os.path.join(os.getcwd(), "Uniprot2AGI-Jul2023.txt")), "r") as uni:
        for line in uni.readlines():
            uniprot_agi["uniprot", line.strip().split("\t")[0]] = \
                             {"AGI":line.strip().split("\t")[1:]}
os.remove(os.path.abspath(os.path.join(os.getcwd(), "Uniprot2AGI-Jul2023.txt"))                             
with open(os.path.abspath(os.path.join(os.getcwd(), "AGI2uniprot-Jul2023.txt")), "r") as agi:
        for line in agi.readlines():
            agi_uniprot["AGI",line.strip().split("\t")[0]] = \
                                {"uniprot_identifier": line.strip().split("\t")[1:]}
os.remove(os.path.join(os.getcwd(), "AGI2uniprot-Jul2023.txt"))                                 
with open(os.path.abspath(os.path.join(os.getcwd(), "TAIR2UniprotMapping-Jul2023.txt")), "r") as tair:
        for line in tair.readlines():
            tair_uniprot["uniprot", line.strip().split("\t")[0]] = \
                            {"locus_tair_ID":line.strip().split("\t")[1:]}
os.remove(os.path.join(os.getcwd(), "TAIR2UniprotMapping-Jul2023.txt"))                             
with open(os.path.abspath(os.path.join(os.getcwd(), "Araport11_pep_20220914_representative_gene_model")), "r") as protein:
        for line in protein.readlines():
            if line.startswith(">"):
                tair_protein_models["AGI",line.strip().split("|")[0].replace(">", "")] = \
                       {"chromosome": line.strip().split("|")[3].replace(" ", "_").replace("LENGTH=", "")}
os.remove(os.path.join(os.getcwd(), "Araport11_pep_20220914_representative_gene_model"))
else:
    print("cant make an updated catalog of the tair database models")
snap.stop()
snap.save()
if __name__ == "__main__":
    arguably.run()
