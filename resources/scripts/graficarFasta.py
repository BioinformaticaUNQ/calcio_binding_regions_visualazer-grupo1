from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import SeqIO
from Bio.Phylo import draw
from Bio import Phylo, AlignIO, Seq
import subprocess
import matplotlib
import matplotlib.pyplot as plt

input_file = './temp/egfr-family.fasta'
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

alignment = AlignIO.read('./temp/egfr-family.fasta', 'fasta')  # reading the alignment file

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
