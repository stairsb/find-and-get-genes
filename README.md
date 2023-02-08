# find-and-get-genes
This script takes an input of unalinged fasta nucleotide sequences of a gene of interest. This program builds Hidden Markov models from your inputs which are using in a similar fashion to blast but can typically obtain more accurate results. The input file can be made from sequences that you already have or sequences that are found from a species or multiple species obtained from NCBI. The output directory will contain matches to the found with the contig or chromosome (depending on your input) and the bp region where the DNA sequence was found. The name is the proposed gene of interest. Either the `-f` or `-c` option will need to be included, this allows for the user to enter a single assembly of interest or a directory of sequences containing assemblies for mutiple isolates or strains.

## Dependancies
Muscle and Hmmer should be added to your path so that they can be accessed anywhere you run this program. This can be done by making sure the executables are in `/usr/bin` or `/usr/local/bin`. If this doesn't work then use export `PATH=/path/to/folderwhereprogramsarelocated:$PATH`. The last option will only add them to your path until you logout and then the command will have to be rerun.
HMMER Documentation: http://eddylab.org/software/hmmer/Userguide.pdf

MUSCLE Documentaiton: https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-113

```
  python 3.7.2 or newer
  MUSCLE v3.8.31
  HMMER v3.3.2
```

## Usage
```
usage: getgenes [-h] [-f] [-c] -g  -o  -n  [-r]

Takes a contig fasta file or directory of fasta contigs (only one of those
options are needed) and input fasta contating a gene of interest which can be
one or mutiple sequences of a certain gene and searches for the gene in the
contig fasta file of contigs using

arguments:
  -g , --gene         Input gene of interest sequence file in fasta format
  -o , --output       Output directory
  -n , --name         Name of gene of interest
  
  optional arguments:
  -h, --help          show this help message and exit
  -f , --contig_f     Input single file of contig sequences
  -c , --contig_dir   Input directory of contig sequences
  -r , --remove       Remove combersome amount of intermediate files created
                      when using contig directory option
```

## Example commands
```
Python3 get_genes.py -c Pathto/contigs_directory/ -g pathto/geneofinterest.fasta -o found_sequences_output/ -n gene_name
Python3 get_genes.py -f pathto/contig_sequence.fasta -g pathto/geneofinterest.fasta -o found_sequences_output/ -n gene_name
```

More user friendly functionality is comming soon.

