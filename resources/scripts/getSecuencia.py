from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
import sys


def get_seqrecs(alignments, threshold):
    for aln in alignments:
        for hsp in aln.hsps:
            if hsp.expect < threshold and (hsp.identities/hsp.align_length) > 0.4:
                yield SeqIO.SeqRecord(Seq(hsp.sbjct), id=aln.accession)
                break


fasta_string = ""
with open(sys.argv[1], 'r') as pdb_file:
    for record in SeqIO.parse(pdb_file, 'pdb-atom'):
        fasta_string += '>' + record.id + "\n"
        fasta_string += record.seq

result_handle = NCBIWWW.qblast("blastp", "pdb", fasta_string, hitlist_size=10)
blast_record = NCBIXML.read(result_handle)

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        print('****Alignment****')
        print('sequence:', alignment.title)
        print('length:', alignment.length)
        print('score:', hsp.score)
        print('gaps:', hsp.gaps)
        print('Percent', (hsp.identities / hsp.align_length))
        print(hsp.query[0:90] + '...')
        print(hsp.match[0:90] + '...')
        print(hsp.sbjct[0:90] + '...')
        best_seqs = get_seqrecs(blast_record.alignments, 0.05)
        SeqIO.write(best_seqs, "./temp/egfr-family.fasta", "fasta")
