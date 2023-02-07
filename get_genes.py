#! /local/cluster/bin/python3
import os
import argparse

#ask about try and except after class

#Initialize parser and arguments
parser = argparse.ArgumentParser(
		prog = 'getgenes',
		description = 'Takes a contig fasta file or directory of fasta contigs (only one of those options are needed) and input fasta contating a gene of interest which can be one or mutiple sequences of a certain gene and searches for the gene in the contig fasta file of contigs using')
parser.add_argument(
                '-f',
                '--contig_f',
                metavar = '',
                help = 'Input single file of contig sequences',
                action = 'store',
                required = False)
parser.add_argument(
		'-c', 
		'--contig_dir',
		metavar = '', 
		help = 'Input directory of contig sequences',
		action = 'store',
		required = False)
parser.add_argument(
		'-g', 
		'--gene',
		metavar = '', 
		help = 'Input gene of interest sequence file in fasta format',
		action = 'store',
		required = True)
parser.add_argument(
		'-o',
		'--output',
		metavar = '',
		help = 'Output directory',
		action = 'store',
		required = True)
parser.add_argument(
		'-n',
		'--name',
		metavar = '',
		help = 'Name of gene of interest',
		action = 'store',
		required = True)
parser.add_argument(
		'-r',
		'--remove',
		metavar = '',
		help = 'Remove combersome amount of intermediate files created when using contig directory option',
		action = 'store',
		required = False)

args = parser.parse_args()

#input argument as variables
contig_directory = args.contig_dir
contig_file = args.contig_f
gene_fasta = os.path.basename(args.gene)
out_dir = args.output
gene_name = args.name
inter_remove = args.remove
path_to_gene_f = args.gene

#prepping the inputs for analysis
cmd = "muscle -in " + path_to_gene_f + " -out alned" + gene_fasta
print(cmd)
os.system(cmd)

cmd1 = "esl-reformat stockholm alned" + gene_fasta + " > " + gene_name + ".sto"
print(cmd1)
os.system(cmd1)

cmd2 = "hmmbuild " + gene_name + ".hmm " + gene_name + ".sto"
print(cmd2)
os.system(cmd2)


#performs the genes prediction and outputs a fasta containing the predected genes
def gene_prediction(contig_fil, remove_extension):
#	current_file = open(contig_directory + contig_fil, "r")
	cmd3 = "nhmmer -A " + remove_extension + "hits.sto " + gene_name + ".hmm " + contig_directory + contig_fil
	print(cmd3)
	os.system(cmd3)

	cmd4 = "esl-reformat fasta " + remove_extension + "hits.sto > " + out_dir + remove_extension + "_"  + gene_name + ".fasta"
	print(cmd4)
	os.system(cmd4)
#	current_file.close()

def contig_file_prediction(contig_file):
	contig_fle = os.path.basename(contig_file)
	remove_extension = contig_fle.rsplit(".", 1 ) [0]
	print(contig_fle)
	print(remove_extension)
	gene_prediction(contig_fle, remove_extension)
#	if inter_remove == "T":
#		os.remove(remove_extension + "hits.sto ")
#	else:
#		print("don't remove")


#gets the name of the basename file from a directory and passes it into gene_predection
def contig_dir_prediction(contig_directory):
	for filename in os.listdir(contig_directory):
		f = os.path.join(contig_directory, filename)
		#make sure it is a file
		if os.path.isfile(f):
			contig_file = os.path.basename(f)
			#print(base_fname)
			remove_extension = contig_file.rsplit(".", 1 ) [0]
			#print("remove extension: " + remove_extension)
			gene_prediction(contig_file, remove_extension)
				
			if inter_remove == "T":
				os.remove(remove_extension + "hits.sto ")
			else:
				print("don't remove")


#This is where the option single file or mutiple is decedied depending on entry
if contig_file:
	contig_file_prediction(contig_file)
else:
	contig_dir_prediction(contig_directory)


