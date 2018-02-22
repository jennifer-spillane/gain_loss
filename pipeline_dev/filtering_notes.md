# Filtering the assemblies in different ways

Using the Pelagia noctiluca to look at the different ways that filtering might affect the final set of genes/transcripts

Original busco score (at the end of the ORP):
> C:96.1%[S:60.1%,D:36.0%],F:4.0%,M:-0.1%,n:303
    291     Complete BUSCOs (C)
    182     Complete and single-copy BUSCOs (S)
    109     Complete and duplicated BUSCOs (D)
    12      Fragmented BUSCOs (F)
    0       Missing BUSCOs (M)
    303     Total BUSCO groups searched

Original number of transcripts at the end of the ORP: 132003

## cd-hit alone

Now I'll run cdhit with a cutoff of 0.99, just to see how many transcripts would be collapsed from the "raw" assembly
> cd-hit -i /mnt/lustre/macmaneslab/nah1004/finished_assemblies/peno.orthomerged.fasta -o orig_peno_cdhit -c 0.99 -T 24

Number of transcripts after cdhit: 120569

Running busco on this to determine how complete the transcriptome remains
> run_BUSCO.py -i orig_peno_cdhit.fasta -o cdhit_busco -l ../sponge_test/metazoa_odb9 -m tran -c 24

Busco score with only cdhit 0.99 filtering:
> C:96.1%[S:60.1%,D:36.0%],F:4.0%,M:-0.1%,n:303
    291     Complete BUSCOs (C)
    182     Complete and single-copy BUSCOs (S)
    109     Complete and duplicated BUSCOs (D)
    12      Fragmented BUSCOs (F)
    0       Missing BUSCOs (M)
    303     Total BUSCO groups searched

## Transrate thresholds

I can use the transrate scores (in the contigs.csv output file) of each transcript to get a distribution of them, then I'll discard all those that are below a threshold.
To get the scores isolated:
> cut -d ',' -f 9 contigs.csv > $HOME/peno_dist.txt

copying these to my Desktop:
> scp jlh1023@premise.sr.unh.edu:/mnt/lustre/macmaneslab/jlh1023/peno_dist.txt ~/Desktop

Then I can put them into R
> peno_dist <- read_csv("~/Desktop/peno_dist.txt")

And get a histogram and some basic stats
> hist(peno_dist$score)
summary(peno_dist$score)
sd(peno_dist$score)

Min: 0.01
Median: 0.6833
Mean: 0.6323
Max: 0.9972
SD: 0.247105

In this case, the threshold will be within 1 stddev of the median
So the threshold should be 0.436195, and it will discard 26,177 transcripts.

In this one, the threshold will be within 0.5 stddev of the median.
So the threshold should be 0.5597475, and it will discard 41,945 transcripts.

These are just numbers, I still have to actually filter them and then run busco on both to see how complete they still are. I'll run cdhit on them post-filtering also, to see if that step is redundant or interesting.
