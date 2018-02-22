gzip -cd SRR521358_2.fastq.gz | sed  's_ __' > SRR521358_2.fastq

transrate --assembly=leni_trinity.fasta --left=SRR3417190_1.fastq --right=SRR3417190_2.fastq --threads=24
