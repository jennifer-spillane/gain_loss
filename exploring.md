# Exploring the sponge metagenomes (grand focal species)

## PALADIN

Basically using everything about PALADIN to try to get some info about these sequences.
Showing examples in amco (Amphimedon compressa), but scripts are the same for each species.
First the actual PALADIN run:
> paladin align /mnt/lustre/hcgs/shared/databases/uniref90/paladin/uniref90.fasta \
/mnt/lustre/macmaneslab/jlh1023/sponges/ill_data/171215/Sample_amco/amco_1.fastq.gz \
-t 24 \
-o amco_paladin \
-P http://premise.sr.unh.edu:3128

I tried it with another option also:
> paladin align /mnt/lustre/hcgs/shared/databases/uniref90/paladin/uniref90.fasta \
/mnt/lustre/macmaneslab/jlh1023/sponges/ill_data/171215/Sample_amco/amco_1.fastq.gz \
-t 24 \
-o amco_f0_paladin \
-P http://premise.sr.unh.edu:3128 \
-f 0

Then I played with some of the plugins:
Looking for GO terms
> paladin-plugins.py @@go -i amco_paladin_uniprot.tsv -q 20 @@write amco_paladin_max20.txt


## Size of Metagenome?

We want to know the size of these metagenomes that we sequenced, so that we can make coverage estimates and try to figure out how many more lanes of sequencing we need. This is difficult with metagenomes, so we'll try four independent methods.

### SGA - preqc
> sga preprocess --pe-mode 1 \
/mnt/lustre/macmaneslab/jlh1023/sponges/ill_data/171215/Sample_amco/amco_1.fastq.gz \
/mnt/lustre/macmaneslab/jlh1023/sponges/ill_data/171215/Sample_amco/amco_2.fastq.gz > amco_sga_genome.fasta

> sga index -a ropebwt --no-reverse -t 24 amco_sga_genome.fasta

> sga preqc -t 24 amco_sga_genome.fasta > amco_sga_genome.preqc

> sga-preqc-report.py amco_sga_genome.preqc \
/mnt/lustre/software/linuxbrew/colsa/Cellar/sga/0.10.15_1/libexec/examples/preqc/\*.preqc -o amco_report

(remove escape for asterisk before running as is in above command - was making my formatting wonky)

### Rarefaction with paladin

Subsampled reads to different amounts (1M, 10M, 20M, and 40M [at least to start])

> seqtk sample -s 23 \
/mnt/lustre/macmaneslab/jlh1023/sponges/ill_data/171215/Sample_amco/amco_1.fastq.gz \
1000000 > amco_sub1.fastq.gz

> paladin align /mnt/lustre/hcgs/shared/databases/uniref90/paladin/uniref90.fasta \
/mnt/lustre/macmaneslab/jlh1023/sponges/ill_data/171215/amco/amco_sub1.fastq.gz \
-t 24 \
-o amco_sub1_paladin \
-P http://premise.sr.unh.edu:3128

For the output, I wrote a script that pulls out the UniProtKB column of the tsv file, takes only the part before the underscore, and disregards any UPI entries. Then it finds just the unique ones and prints the number of these to the screen, as well as writing them to a file for later use (rarefy.py).

**amco**
1M: 27,935
10M: 137,543
20M: 214,957
40M: 330,771
Full (87M): 523,794

**apca**
1M: 94,980
10M: 494,582
20M: 722,235
40M: 1,003,289
Full (64M): 1,219,113


When I did it again, I used the same subsampling but changed my script to exclude all those genes that had a count of one read in the paladin output. (and then filtering at 2, 4, 6, and 8)

**amco**    | 1         | 2         | 4         | 6         | 8
1M:         | 6,967     | 3397      | 1274      | 680       | 426
10M:        | 48,072    | 30441     | 17970     | 12867     | 9990
20M:        | 78,882    | 50959     | 31376     | 23061     | 18291
40M:        | 128,930   | 83847     | 52631     | 39420     | 31812
Full (87M): | 221,011   | 144198    | 91200     | 69166     | 56640

**apca**    | 1         | 2         | 4         | 6         | 8
1M:         | 16668     | 5998      | 1866      | 898       | 492
10M:        | 202532    | 113715    | 52774     | 31208     | 20833
20M:        | 353998    | 223528    | 117370    | 74413     | 52351
40M:        | 565600    | 393068    | 234798    | 161155    | 119149
Full (64M): | 740263    | 541358    | 349109    | 252954    | 194375

**nier**    | 1         | 2         | 4         | 6         | 8         | 10
1M:         | 19413     | 11884     | 5703      | 3294      | 2083      | 1436
10M:        | 75965     | 56499     | 40017     | 32155     | 27053     | 23365
20M:        | 107077    | 81030     | 58750     | 47724     | 40866     | 36189
40M:        | 150274    | 113730    | 83983     | 69307     | 59782     | 53178
Full (65M): | 190948    | 143720    | 106717    | 88866     | 77399     | 69402

**haca**    | 1         | 2         | 4         | 6         | 8         | 10
1M:         | 7534      | 3942      | 1912      | 1286      | 979       | 797
10M:        | 51092     | 34173     | 19978     | 13571     | 10161     | 8084
20M:        | 78416     | 55759     | 36054     | 26437     | 20417     | 16514
40M:        | 115067    | 84449     | 58493     | 45363     | 36962     | 31230
Full (60M): | 142712    | 105341    | 74653     | 59294     | 49649     | 42706

**xemu**    | 1         | 2         | 4         | 6         | 8         | 10
1M:         | 16015     | 6159      | 2070      | 1035      | 589       | 363
10M:        | 194118    | 107945    | 49041     | 29215     | 19871     | 14675
20M:        | 343222    | 213749    | 110831    | 69432     | 48654     | 36555
40M:        | 552733    | 379876    | 224751    | 152683    | 112013    | 86618
Full (71M): | 770254    | 564855    | 366439    | 266134    | 205543    | 164964


When I filter again, but this time increasing the number of reads mapping to that gene that make it acceptable. I was using 1 as the cuttoff before, so now I'm using **10** (then 100, then 1000)

**amco**    | 10    | 100   | 1000
1M:         | 285   | 9     | 3
10M:        | 8075  | 279   | 9
20M:        | 15261 | 830   | 23
40M:        | 26711 | 2519  | 59
Full (87M): | 48274 | 7058  | 210

**apca**    | 10        | 100   | 1000
1M:         | 318       | 14    | 0
10M:        | 15082     | 287   | 13
20M:        | 39337     | 1149  | 29
40M:        | 92573     | 3631  | 62
Full (87M): | 155448    | 7582  | 116


### Kmer counting with jellyfish

This is a normal way that we could look at genome size, but will be different and weird on a metagenome. We wanted to try it anyway, just to see what the distribution would look like.
I tried it with both 51mers and 31mers, though they looked pretty similar.

> jellyfish count -m 51 -s 2G -t 24 -C -o /dev/stdout amco_trim_1P.fastq \
| jellyfish histo /dev/stdin -o amco_count.histo

> scp jlh1023@premise.sr.unh.edu:/mnt/lustre/macmaneslab/jlh1023/sponges/ill_data/171215/amco/amco_count.histo ~/Desktop/

### Mapping reads to assembly

This method will rely on how much we trust these assemblies. Which is some, basically.

> bwa index -p amco_index amco_assembly/scaffolds.fasta

> bwa mem -t 24 amco_index amco_trim_1P.fastq amco_trim_2P.fastq \
| samtools view -sb -T amco_assembly/scaffolds.fasta -@24 -o mapped_amco.bam

> samtools flagstat mapped_amco.bam

> samtools sort -@ 24 -m 4Gb -o amco_sorted.bam mapped_amco.bam

> samtools depth mapped_amco.bam > amco_depth.out
