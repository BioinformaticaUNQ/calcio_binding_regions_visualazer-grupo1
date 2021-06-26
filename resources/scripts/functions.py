def fasta(path_file):
    fasta_string =""
    with open(path_file, 'r') as pdb_file:
        for record in SeqIO.parse(pdb_file, 'pdb-atom'):
            fasta_string += '>' + record.id + "\n"
            fasta_string += record.seq
    return fasta_string

def blast_pdb(target_sequence, num_hits=1000):

    from Bio.Blast import NCBIWWW, NCBIXML
    result_handle = NCBIWWW.qblast("blastp", "nr", target_sequence, hitlist_size=num_hits)
    blast_record = NCBIXML.read(result_handle)

    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print(hsp)
            print("***** RECORD ****")
            print("sequence:", alignment.title)
            print("E-value:", hsp.expect)