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

Busco score with only transrate 1.0 filtering:
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

Busco score with only transrate 0.5 filtering:
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

Busco score with only transrate 2.0 filtering:
- C:91.0% [S:57.4%, D:33.6%], F:4.4%, M:4.6%, n:978
- 890     Complete BUSCOs (C)
- 561     Complete and single-copy BUSCOs (S)
- 329     Complete and duplicated BUSCOs (D)
- 43      Fragmented BUSCOs (F)
- 45      Missing BUSCOs (M)
- 978     Total BUSCO groups searched

## Investigating what is being filtered output

Because we are losing a lot of busco score through this filtering process (ideally we would not lose any content, only redundant transcripts and isoforms), we need to investigate further what is actually being lost, and if there is a way to preserve some of that content.

I incorporated a few lines into the filter_transrate.py script to retain the lines of the contig file whose score falls below 0.15 (the worst of the worst, which are being filtered out in all three scenarios above). We looked at the different metrics and are trying to figure out what might result in a score that low.

I've now incorporated a way of filtering that takes into account the tpm of the contig as well as its overall score. I'm trying it on the filter that uses 1 standard deviation below the median, and I'll use two different values to test. BUSCO to follow.

### 1 stddev below the median and at least 0.5 tpm

Number of transcripts above threshold: 127,520 (lost 4,483 contigs)

Busco score with transrate 1 stddev and 0.5 tpm filtering:
- C:93.3% [S:57.7%, D:35.6%], F:4.1%, M:2.6%, n:978
- 912     Complete BUSCOs (C)
- 564     Complete and single-copy BUSCOs (S)
- 348     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 1.0 tpm

Number of transcripts above threshold: 123,281 (lost 8,722 contigs)

Busco score with transrate 1 stddev and 1.0 tpm filtering:
- C:93.3% [S:57.9%, D:35.4%], F:4.1%, M:2.6%, n:978
- 912     Complete BUSCOs (C)
- 566     Complete and single-copy BUSCOs (S)
- 346     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 1.5 tpm

Number of transcripts above threshold: 119,527 (lost 12,476 contigs)

Busco score with transrate 1 stddev and 1.5 tpm filtering:
- C:93.3% [S:58.0%, D:35.3%], F:4.1%, M:2.6%, n:978
- 912     Complete BUSCOs (C)
- 567     Complete and single-copy BUSCOs (S)
- 345     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 2.0 tpm

Number of transcripts above threshold: 117,084 (lost 14,919 contigs)

Busco score with transrate 1 stddev and 2.0 tpm filtering:
- C:93.3% [S:58.3%, D:35.0%], F:4.1%, M:2.6%, n:978
- 912     Complete BUSCOs (C)
- 570     Complete and single-copy BUSCOs (S)
- 342     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 2.5 tpm

Number of transcripts above threshold: 115,272 (lost 16,731 contigs)

Busco score with transrate 1 stddev and 2.5 tpm filtering:
- C:93.3% [S:58.6%, D:34.7%], F:4.1%, M:2.6%, n:978
- 912     Complete BUSCOs (C)
- 573     Complete and single-copy BUSCOs (S)
- 339     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 3.0 tpm

Number of transcripts above threshold: 113,892 (lost 18,111 contigs)

Busco score with transrate 1 stddev and 3.0 tpm filtering:
- C:93.3% [S:58.7%, D:34.6%], F:4.1%, M:2.6%, n:978
- 912     Complete BUSCOs (C)
- 574     Complete and single-copy BUSCOs (S)
- 338     Complete and duplicated BUSCOs (D)
- 40      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 10.0 tpm

Number of transcripts above threshold: 108,409 (lost 23,594 contigs)

Busco score with transrate 1 stddev and 10.0 tpm filtering:
- C:92.2% [S:60.1%, D:32.1%], F:4.5%, M:3.3%, n:978
- 902     Complete BUSCOs (C)
- 588     Complete and single-copy BUSCOs (S)
- 314     Complete and duplicated BUSCOs (D)
- 44      Fragmented BUSCOs (F)
- 32      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 7.0 tpm

Number of transcripts above threshold: 109,434 (lost 22,569 contigs)

Busco score with transrate 1 stddev and 7.0 tpm filtering:
- C:92.9% [S:59.5%, D:33.4%], F:4.4%, M:2.7%, n:978
- 909     Complete BUSCOs (C)
- 582     Complete and single-copy BUSCOs (S)
- 327     Complete and duplicated BUSCOs (D)
- 43      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 5.0 tpm

Number of transcripts above threshold: 110,768 (lost 21,235 contigs)

Busco score with transrate 1 stddev and 5.0 tpm filtering:
- C:93.1% [S:59.1%, D:34.0%], F:4.2%, M:2.7%, n:978
- 911     Complete BUSCOs (C)
- 578     Complete and single-copy BUSCOs (S)
- 333     Complete and duplicated BUSCOs (D)
- 41      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


### 1 stddev below the median and at least 4.0 tpm

Number of transcripts above threshold: 111,913 (20,090 lost  contigs)

Busco score with transrate 1 stddev and 4.0 tpm filtering:
- C:93.2% [S:58.8%, D:34.4%], F:4.2%, M:2.6%, n:978
- 911     Complete BUSCOs (C)
- 575     Complete and single-copy BUSCOs (S)
- 336     Complete and duplicated BUSCOs (D)
- 41      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched

I ran the filtered fasta file that came from this process through cdhit with 1.0 filtering
> cd-hit -i peno_trans1tpm4.fasta -o peno_trans1tpm4_cdhit.fasta -c 1.0 -T 6

It returned 107,875 contigs (4038 lost after transrate filtering, 24,128 lost overall)
I also ran busco after this step, to make sure it wasn't affecting the completeness.

Busco score with transrate 1 stddev, 4.0 tpm filtering, and cdhit 1.0:
- C:93.1% [S:58.3%, D:33.8%], F:4.2%, M:2.7%, n:978
- 911     Complete BUSCOs (C)
- 580     Complete and single-copy BUSCOs (S)
- 331     Complete and duplicated BUSCOs (D)
- 41      Fragmented BUSCOs (F)
- 26      Missing BUSCOs (M)
- 978     Total BUSCO groups searched




### Grantia compressa testing

I want to test this process on more species to make sure it's consistent.

The original dataset has 156,026 contigs.

Busco score for original assembly:
- C:89.1% [S:60.9%, D:28.2%], F:4.9%, M:6.0%, n:978
- 872     Complete BUSCOs (C)
- 596     Complete and single-copy BUSCOs (S)
- 276     Complete and duplicated BUSCOs (D)
- 48      Fragmented BUSCOs (F)
- 58      Missing BUSCOs (M)
- 978     Total BUSCO groups searched

# filtering with 1 standard deviation below the median, or at least 4 tpm

Number of transcripts above threshold: 134,777 (lost 21,249 contigs)

Busco score with transrate 1 stddev and 4.0 tpm filtering:
- C:88.7% [S:61.6%, D:27.1%], F:5.3%, M:6.0%, n:978
- 867     Complete BUSCOs (C)
- 602     Complete and single-copy BUSCOs (S)
- 265     Complete and duplicated BUSCOs (D)
- 52      Fragmented BUSCOs (F)
- 59      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 7 tpm

Number of transcripts above threshold: 130,958 (lost 25,068 contigs)

Busco score with transrate 1 stddev and 7.0 tpm filtering:
- C:88.3% [S:62.1%, D:26.2%], F:5.4%, M:6.3%, n:978
- 863     Complete BUSCOs (C)
- 607     Complete and single-copy BUSCOs (S)
- 256     Complete and duplicated BUSCOs (D)
- 53      Fragmented BUSCOs (F)
- 62      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 1 tpm

Number of transcripts above threshold: 148,087 (lost 7,939 contigs)

Busco score with transrate 1 stddev and 1.0 tpm filtering:
- C:89.1% [S:61.1%, D:28.0%], F:4.9%, M:6.0%, n:978
- 872     Complete BUSCOs (C)
- 598     Complete and single-copy BUSCOs (S)
- 274     Complete and duplicated BUSCOs (D)
- 48      Fragmented BUSCOs (F)
- 58      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 2 tpm

Number of transcripts above threshold: 141,174 (lost 14,852 contigs)

Busco score with transrate 1 stddev and 2.0 tpm filtering:
- C:89.2% [S:61.5%, D:27.7%], F:4.9%, M:5.9%, n:978
- 872     Complete BUSCOs (C)
- 601     Complete and single-copy BUSCOs (S)
- 271     Complete and duplicated BUSCOs (D)
- 48      Fragmented BUSCOs (F)
- 58      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 3 tpm

Number of transcripts above threshold: 137,358 (lost 18,668 contigs)

Busco score with transrate 1 stddev and 3.0 tpm filtering:
- C:88.9% [S:61.5%, D:27.4%], F:5.1%, M:6.0%, n:978
- 869     Complete BUSCOs (C)
- 601     Complete and single-copy BUSCOs (S)
- 268     Complete and duplicated BUSCOs (D)
- 50      Fragmented BUSCOs (F)
- 59      Missing BUSCOs (M)
- 978     Total BUSCO groups searched



### Pleraplysilla spinifera

The original dataset has 144,724 contigs

Busco score for original dataset:
- C:92.6% [S:46.2%, D:46.4%], F:3.1%, M:4.3%, n:978
- 906     Complete BUSCOs (C)
- 452     Complete and single-copy BUSCOs (S)
- 454     Complete and duplicated BUSCOs (D)
- 30      Fragmented BUSCOs (F)
- 42      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 1 tpm

Number of transcripts above threshold: 138,404 (lost 6320 contigs)

Busco score for original dataset:
- C:92.6% [S:46.4%, D:46.2%], F:3.1%, M:4.3%, n:978
- 906     Complete BUSCOs (C)
- 454     Complete and single-copy BUSCOs (S)
- 452     Complete and duplicated BUSCOs (D)
- 30      Fragmented BUSCOs (F)
- 42      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 2 tpm

Number of transcripts above threshold: 132,251 (lost 12,473 contigs)

Busco score for original dataset:
- C:92.5% [S:46.4%, D:46.1%], F:3.2%, M:4.3%, n:978
- 905     Complete BUSCOs (C)
- 454     Complete and single-copy BUSCOs (S)
- 451     Complete and duplicated BUSCOs (D)
- 31      Fragmented BUSCOs (F)
- 42      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 3 tpm

Number of transcripts above threshold: 128,273 (lost 16,451 contigs)

Busco score for original dataset:
- C:92.5% [S:46.6%, D:45.9%], F:3.2%, M:4.3%, n:978
- 905     Complete BUSCOs (C)
- 456     Complete and single-copy BUSCOs (S)
- 449     Complete and duplicated BUSCOs (D)
- 31      Fragmented BUSCOs (F)
- 42      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 4 tpm

Number of transcripts above threshold: 125,732 (lost 18,992 contigs)

Busco score for original dataset:
- C:92.5% [S:47.1%, D:45.4%], F:3.2%, M:4.3%, n:978
- 905     Complete BUSCOs (C)
- 461     Complete and single-copy BUSCOs (S)
- 444     Complete and duplicated BUSCOs (D)
- 31      Fragmented BUSCOs (F)
- 42      Missing BUSCOs (M)
- 978     Total BUSCO groups searched


# filtering with 1 standard deviation below the median, or at least 7 tpm

Number of transcripts above threshold: 121,944 (lost 22,780 contigs)

Busco score for original dataset:
- C:92.5% [S:47.9%, D:44.6%], F:3.2%, M:4.3%, n:978
- 904     Complete BUSCOs (C)
- 468     Complete and single-copy BUSCOs (S)
- 436     Complete and duplicated BUSCOs (D)
- 31      Fragmented BUSCOs (F)
- 43      Missing BUSCOs (M)
- 978     Total BUSCO groups searched
