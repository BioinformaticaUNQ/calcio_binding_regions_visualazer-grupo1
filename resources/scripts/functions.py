from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline
from Bio.Graphics.ColorSpiral import get_colors
from Bio.Seq import Seq


def fasta(path_file):
    fasta_string =""
    with open(path_file, 'r') as pdb_file:
        for record in SeqIO.parse(pdb_file, 'pdb-atom'):
            fasta_string += '>' + record.id + "\n"
            fasta_string += record.seq
    return fasta_string

def get_seqrecs(alignments, threshold):
    for aln in alignments:
        for hsp in aln.hsps:
            if hsp.expect < threshold and (hsp.identities / hsp.align_length) > 0.4:
                yield SeqIO.SeqRecord(Seq(hsp.sbjct), id=aln.accession)
                break

def blast_pdb(target_sequence, num_hits=10):

    from Bio.Blast import NCBIWWW, NCBIXML
    result_handle = NCBIWWW.qblast("blastp", "pdb", target_sequence, hitlist_size=num_hits)
    blast_record = NCBIXML.read(result_handle)

    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('score:', hsp.score)
            print('gaps:', hsp.gaps)
            print('Percent',(hsp.identities / hsp.align_length))
            print(hsp.query[0:90] + '...')
            print(hsp.match[0:90] + '...')
            print(hsp.sbjct[0:90] + '...')
            best_seqs = get_seqrecs(blast_record.alignments, 0.05)
            SeqIO.write(best_seqs, "egfr-family.fasta", "fasta")
            #raficar_fasta(best_seqs)
def graficar_fasta2():
    from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

    from Bio.Phylo import draw
    from Bio import Phylo, AlignIO,Seq
    import subprocess
    import matplotlib
    import matplotlib.pyplot as plt

    input_file = '/Users/maximilianodiaz/Documents/Facu/calcio_binding_regions_visualazer-grupo1/resources/scripts/egfr-family.fasta'
    records = SeqIO.parse(input_file, 'fasta')
    records = list(records)  # make a copy, otherwise our generator
    # is exhausted after calculating maxlen
    maxlen = max(len(record.seq) for record in records)

    # pad sequences so that they all have the same length
    for record in records:
        if len(record.seq) != maxlen:
            sequence = str(record.seq).ljust(maxlen, '-')
            record.seq = Seq.Seq(sequence)
    assert all(len(record.seq) == maxlen for record in records)

    # write to temporary file and do alignment
    with open(input_file, 'w') as f:
        SeqIO.write(records, f, 'fasta')
    alignment = AlignIO.read(input_file, "fasta")

    alignment = AlignIO.read('/Users/maximilianodiaz/Documents/Facu/calcio_binding_regions_visualazer-grupo1/resources/scripts/egfr-family.fasta', 'fasta')  # reading the alignment file

    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)  # distance matrix

    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)  # build with neighbour joining algorithm a tree from dm
    tree.rooted = True
    Phylo.write(tree, 'TreeToCutOff.nwk', 'newick')

    plt.rc('font',
           size=8)  # controls default text sizes #HERE IS THE SETTING FOR THAT ALLOWS ME TO HIDE THE BRANCH TIP LABELS
    plt.rc('axes', titlesize=24)  # fontsize of the axes title
    plt.rc('xtick', labelsize=20)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=20)  # fontsize of the tick labels
    plt.rc('figure', titlesize=28)  # fontsize of the figure title

    Phylo.draw(tree)
    #plt.savefig("TreeToCutOff.svg", format='svg', dpi=1200)
