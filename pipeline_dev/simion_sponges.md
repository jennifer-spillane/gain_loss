# HMA or LMA?

Trying to figure out if the sponges from the Simion paper (2017) are high microbial abundance, or low microbial abundance by blasting them through the same process I used on the five genomes from the SICB poster (2018).

## Sponge DB blasting

I used the custom database I made last fall (contains 10 sponge species' genetic info) and blasted each of the five sponges in the Simion paper. Then I also blasted using the NCBI references for each different group of organisms.

I know that there is at least a little overlap between the inverts and the sponges (though not as much as one might think), so I'll adjust for that.

### Leuconia nivea

> cut -f 1 leni_por_blast.out | sort > leni_por_blast_sorted.out
> grep "invert" leni_blast.out | cut -f 1 | sort | comm  - leni_por_blast_sorted.out -1 -2 | wc -l

Then I subtract the number that overlap from the "inverts" category, as those are already encompassed in the "sponges" category.
Number overlapping: 1215

Number of contigs: 221,000
Sponges: 11,104
Inverts: 839
Bacteria: 2795
Archaea: 15
Virus: 9
Protozoan: 1022
Mammal: 1150
Total hits: 16,925
Unknown:

### Clathrina coriacea

> cut -f 1 clco_por_blast.out | sort > clco_por_blast_sorted.out
> grep "invert" clco_blast.out | cut -f 1 | sort | comm  - clco_por_blast_sorted.out -1 -2 | wc -l

Number overlapping:

Number of contigs: 144,182
Sponges: 2682
Inverts:
Bacteria:
Archaea:
Virus:
Protozoan:
Mammal:
Unknown:

### Grantia compressa

> cut -f 1 grco_por_blast.out | sort > grco_por_blast_sorted.out
> grep "invert" grco_blast.out | cut -f 1 | sort | comm  - grco_por_blast_sorted.out -1 -2 | wc -l

Number overlapping: 860

Number of contigs: 156,026
Sponges: 9325
Inverts: 429
Bacteria: 605
Archaea: 0
Virus: 5
Protozoan: 742
Mammal: 1078
Unknown:

### Plakina jani

> cut -f 1 plja_por_blast.out | sort > plja_por_blast_sorted.out
> grep "invert" plja_blast.out | cut -f 1 | sort | comm  - plja_por_blast_sorted.out -1 -2 | wc -l

Number overlapping:

Number of contigs: 160,287
Sponges: 2367
Inverts:
Bacteria:
Archaea:
Virus:
Protozoan:
Mammal:
Unknown:

### Pleraplysilla spinifera

> cut -f 1 plsp_por_blast.out | sort > plsp_por_blast_sorted.out
> grep "invert" plsp_blast.out | cut -f 1 | sort | comm  - plsp_por_blast_sorted.out -1 -2 | wc -l

Number overlapping:

Number of contigs: 144,724
Sponges: 3115
Inverts:
Bacteria:
Archaea:
Virus:
Protozoan:
Mammal:
Unknown:
