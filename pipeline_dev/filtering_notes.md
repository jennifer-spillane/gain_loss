# Filtering the assemblies in different ways

Using the Pelagia noctiluca to look at the different ways that filtering might affect the final set of genes/transcripts

Original busco score (at the end of the ORP):
- C:96.1%[S:60.1%,D:36.0%],F:4.0%,M:-0.1%,n:303
- 291     Complete BUSCOs (C)
- 182     Complete and single-copy BUSCOs (S)
- 109     Complete and duplicated BUSCOs (D)
- 12      Fragmented BUSCOs (F)
- 0       Missing BUSCOs (M)
- 303     Total BUSCO groups searched

Original number of transcripts at the end of the ORP: 132,003
> grep ">" /mnt/lustre/macmaneslab/nah1004/finished_assemblies/peno.orthomerged.fasta | wc -l

Just realized that the above busco scores are from the eukaryote database, not the metazoan one that I'm using for other things, so I'm re-running it:
> run_BUSCO.py -i /mnt/lustre/macmaneslab/nah1004/finished_assemblies/peno.orthomerged.fasta -o orig_peno_busco -l ../sponge_test/metazoa_odb9 -m tran -c 24

- C:93.3%[S:57.4%,D:35.9%],F:4.1%,M:2.6%,n:978
- 912     Complete BUSCOs (C)
- 561     Complete and single-copy BUSCOs (S)
- 351     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26       Missing BUSCOs (M)
- 978     Total BUSCO groups searched

## cd-hit alone

### cd-hit with 0.99 similarity filtering

Now I'll run cdhit with a cutoff of 0.99, just to see how many transcripts would be collapsed from the "raw" assembly
> cd-hit -i /mnt/lustre/macmaneslab/nah1004/finished_assemblies/peno.orthomerged.fasta -o orig_peno_cdhit99.fasta -c 0.99 -T 24

Number of transcripts after cdhit99: 120,569 (lost 11,434)
> grep ">" orig_peno_cdhit99.fasta | wc -l

Running busco on this to determine how complete the transcriptome remains
> run_BUSCO.py -i orig_peno_cdhit99.fasta -o cdhit_busco -l ../sponge_test/metazoa_odb9 -m tran -c 24

Busco score with only cdhit 0.99 filtering:
- C:93.2%[S:60.5%,D:32.7%],F:4.1%,M:2.7%,n:978
- 912     Complete BUSCOs (C)
- 592     Complete and single-copy BUSCOs (S)
- 320     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26       Missing BUSCOs (M)
- 978     Total BUSCO groups searched

### cd-hit with 1.0 similarity filtering

Also running cdhit with a cutoff of 1.0, to see how many collapse under that condition.
> cd-hit -i /mnt/lustre/macmaneslab/nah1004/finished_assemblies/peno.orthomerged.fasta -o orig_peno_cdhit1.fasta -c 1.0 -T 24

Number of transcripts after cdhit1: 126,512 (lost 5,491)
> grep ">" orig_peno_cdhit1.fasta | wc -l

Also running busco again, for good measure
> run_BUSCO.py -i orig_peno_cdhit1.fasta -o cdhit1_busco -l ../sponge_test/metazoa_odb9 -m tran -c 24

Busco score with only cdhit 1.0 filtering:
- C:93.3%[S:57.9%,D:35.4%],F:4.1%,M:2.6%,n:978
- 912     Complete BUSCOs (C)
- 566     Complete and single-copy BUSCOs (S)
- 346     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26       Missing BUSCOs (M)
- 978     Total BUSCO groups searched

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
> awk -F ',' '$9<.436195' /mnt/lustre/macmaneslab/nah1004/transcriptomes/reports/transrate_peno/peno.orthomerged/contigs.csv | wc -l

In this one, the threshold will be within 0.5 stddev of the median.
So the threshold should be 0.5597475, and it will discard 41,945 transcripts.
> awk -F ',' '$9<.5597475' /mnt/lustre/macmaneslab/nah1004/transcriptomes/reports/transrate_peno/peno.orthomerged/contigs.csv | wc -l

### script to filter: filter_transrate.py (see pipeline_dev repo)

The actual numbers are a little different when you let python calculate them from the scores.

### 1 stddev below the median

For 1 stddev below the median, the threshold is 0.436226... and we end up with 105,803 sequences left after filtering (26,200 weeded out)

Busco score with only cdhit 1.0 filtering:
- C:85.1% [S:58.0%, D:27.1%], F:5.3%, M:9.6%, n:978
- 832     Complete BUSCOs (C)
- 567     Complete and single-copy BUSCOs (S)
- 265     Complete and duplicated BUSCOs (D)
- 52      Fragmented BUSCOs (F)
- 94     Missing BUSCOs (M)
- 978     Total BUSCO groups searched

I'm also going to run cdhit on the filtered fasta, to see if it ends up being redundant
> cd-hit -i peno_trans1.fasta -o peno_trans1_cdhit1.fasta -c 1.0 -T 24

Number of transcripts after cd-hit filtering (1.0) the already filtered file: 101,931 (lost 3,872)
> grep ">" peno_trans1_cdhit1.fasta | wc -l

### 0.5 stddev below the median

for 0.5 stddev below the median, the threshold is 0.559779... and we end up with 90,049 sequences left after filtering (41,954 weeded out)

Busco score with only cdhit 0.5 filtering:
- C:77.9% [S:54.9%, D:23.0%], F:5.7%, M:16.4%, n:978
- 762     Complete BUSCOs (C)
- 537     Complete and single-copy BUSCOs (S)
- 225     Complete and duplicated BUSCOs (D)
- 56      Fragmented BUSCOs (F)
- 160     Missing BUSCOs (M)
- 978     Total BUSCO groups searched

I'm also going to run cdhit on the filtered fasta, to see if it ends up being redundant
> cd-hit -i peno_trans05.fasta -o peno_trans05_cdhit1.fasta -c 1.0 -T 24

Number of transcripts after cd-hit filtering (1.0) the already filtered file: 86,764 (lost 3,285)
> grep ">" peno_trans05_cdhit1.fasta | wc -l

### 2 stddev below the median

For 2 stddev below the median, the threshold is 0.189121... and we end up with 122,448 sequences left after filtering (9,555 weeded out)

Busco score with only cdhit 2.0 filtering:
- C:91.0% [S:57.4%, D:33.6%], F:4.4%, M:4.6%, n:978
- 890     Complete BUSCOs (C)
- 561     Complete and single-copy BUSCOs (S)
- 329     Complete and duplicated BUSCOs (D)
- 43      Fragmented BUSCOs (F)
- 45      Missing BUSCOs (M)
- 978     Total BUSCO groups searched
