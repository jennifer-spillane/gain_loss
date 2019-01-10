# Notes for when I pick this back up in a few weeks:

### Priorities to work on for the full dataset
1. The normalization script: this should take the busco score into account (the final busco score, after all filtering steps) and deplete the gene count (found in Orthogroups.GeneCount.csv) to reflect the percentage of buscos there.
2. Think about what other quality metrics we could employ: busco might tell us that we have a pretty complete animal genome or eukaryotic genome, but might not tell us we have a pretty good cnidarian genome, etc. so think about what else we could look at to test completeness.
3. Troubleshoot the /mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/dollo_model.py script: it is still sending out weirdly duplicated results and we'll need to address it for the final dataset. Current troubleshooting can be found here: /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/modeling







# notes on the eight orthogroups of sponges that are 1.3 standard deviations from the mean

## OG0000346 - absent
### Homo_sapiens_11349
MAALTDLSFMYRWFKNCNLVGNLSEKYVFITGCDSGFGNLLAKQLVDRGMQVLAACFTEE
short-chain dehydrogenase/reductase family 9C member 7 - This gene encodes a protein with similarity to the short-chain dehydrogenase/reductase (SDR) family but has not been shown to have retinoid or dehydrogenase activities.
They suggested that SDRO may catalyze the metabolism of another class of nuclear receptor ligands, or may regulate metabolism by binding substrates or products, or by serving as a regulatory factor.
### Homo_sapiens_30251
MWLYLAVFVGLYYLLHWYRERQVLSHLRDKYVFITGCDSGFGKLLARQLDARGLRVLAAC
sterol/retinol dehydrogenase - Restricted expression toward liver

## OG0000809
### Homo_sapiens_35304
MELRSTAAPRAEGYSNVGFQNEENFLENENTSGNNSIRSRAVQSREHTNTKQDEEQVTVE
solute carrier family 28 member 3 - Nucleoside transporters, such as SLC28A3, regulate multiple cellular processes, including neurotransmission, vascular tone, adenosine concentration in the vicinity of cell surface receptors, and transport and metabolism of nucleoside drugs. SLC28A3 shows broad specificity for pyrimidine and purine nucleosides (Ritzel et al., 2001 [PubMed 11032837]).[supplied by OMIM, Mar 2008]
It may be involved in the intestinal absorption and renal handling of pyrimidine nucleoside analogs used to treat acquired immunodeficiency syndrome (AIDS).
### Homo_sapiens_78005
MENDPSRRRESISLTPVAKGLENMGADFLESLEEGQLPRSDLSPAEIRSSWSEAAPKPFS
sodium/nucleoside cotransporter 1 isoform X11 - Biased expression in kidney (RPKM 9.5), small intestine (RPKM 9.4) and 2 other tissues

## OG0002105 - absent
### Drosophila_melanogaster_14145
MADGRIVENGRGGGGEGVAAAPSPRYAILDCDGGSDDAWALLLLLHAAKSHGIHLLAITT
PREDICTED: pyrimidine-specific ribonucleoside hydrolase RihA [Drosophila bipectinata]

## OG0003819 - absent
### Homo_sapiens_10265
MAALAPVGSPASRGPRLAAGLRLLPMLGLLQLLAEPGLGRVHHLALKDDVRHKVHLNTFG
protein GPR107 isoform 3 - Ubiquitous expression in thyroid (RPKM 20.9), brain (RPKM 13.5) and 25 other tissues
Involved in Golgi-to-ER retrograde transport. Functions as a host factor required for infection by Pseudomonas aeruginosa exotoxin A and Campylobacter jejuni CDT toxins.

## OG0004068 - absent
### Homo_sapiens_17769
MDENESNQSLMTSSQYPKEAVRKRQNSARNSGASDSSRFSRKSFKLDYRLEEDVTKSKKG
N-acyl-phosphatidylethanolamine-hydrolyzing phospholipase D isoform X4 - NAPEPLD is a phospholipase D type enzyme that catalyzes the release of N-acylethanolamine (NAE) from N-acyl-phosphatidylethanolamine (NAPE) in the second step of the biosynthesis of N-acylethanolamine
Ubiquitous expression in brain (RPKM 8.2), kidney (RPKM 8.2) and 25 other tissues
Gillum et al. (2008) found that NAPEs were secreted into the circulation from the small intestine in rats in response to ingested fat. Systemic administration of the most abundant circulating NAPE at physiologic doses decreased food intake in rats.
Leung et al. (2006) showed that Napepld-null mice had greatly reduced brain levels of long-chain saturated NAEs but retained wildtype levels of polyunsaturated NAEs, such as anandamide.

## OG0005462 - absent
### Homo_sapiens_4829
MSQAPGAQPSPPTVYHERQRLELCAVHALNNVLQQQLFSQEAADEICKRLAPDSRLNPHR
josephin-2 isoform 1 - This gene encodes a protein containing a Josephin domain. Josephin domain-containing proteins are deubiquitinating enzymes which catalyze the hydrolysis of the bond between the C-terminal glycine of the ubiquitin peptide and protein substrates. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene.
Ubiquitous expression in fat (RPKM 7.4), stomach (RPKM 6.8) and 25 other tissues

## OG0005616 - absent
### Homo_sapiens_96642
MDPTAGSKKEPGGGAATEEGVNRIAVPKPPSIEEFSIVKPISRGAFGKVYLGQKGGKLYA
serine/threonine-protein kinase greatwall isoform X10 - This gene encodes a microtubule-associated serine/threonine kinase. Mutations at this locus have been associated with autosomal dominant thrombocytopenia, also known as thrombocytopenia-2. Alternatively spliced transcript variants have been described for this locus.
Ubiquitous expression in bone marrow (RPKM 4.9), testis (RPKM 3.4) and 25 other tissues

## OG0005897
### Homo_sapiens_44509
MRRAELAGLKTMAWVPAESAVEELMPRLLPVEPCDLTEGFDPSVPPRTPQEYLRRVQIEA
survival of motor neuron protein interacting protein 1, isoform CRA_c - This gene encodes one of the proteins found in the SMN complex, which consists of several gemin proteins and the protein known as the survival of motor neuron protein. The SMN complex is localized to a subnuclear compartment called gems (gemini of coiled bodies) and is required for assembly of spliceosomal snRNPs and for pre-mRNA splicing. This protein interacts directly with the survival of motor neuron protein and it is required for formation of the SMN complex. A knockout mouse targeting the mouse homolog of this gene exhibited disrupted snRNP assembly and motor neuron degeneration.
Ubiquitous expression in testis (RPKM 5.8), lymph node (RPKM 4.5) and 25 other tissues




looking at ancestral states of all these different genes across all of holozoans
looking for shift as a way of identifying evol gene gain and loss
sponges are sig dif, but that does not mean that other nodes are not.

looking at how the patterns that we see in evol histories of these genes could tell us something about the sorts of genetic loci that we should be looking at to reconstruct the evol history of animals

these that are ephrin, (how nervous systems wire themselves) GPCRs absent in sponges
