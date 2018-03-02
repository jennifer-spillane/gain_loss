#script to go into a slurm for trying out filtering on different taxa.

#original before filtering
grep -c ">" /mnt/lustre/macmaneslab/nah1004/transcriptomes/assemblies/plsp.orthomerged.fasta

run_BUSCO.py -i /mnt/lustre/macmaneslab/nah1004/transcriptomes/assemblies/plsp.orthomerged.fasta \
-o plsp_orig_busco \
-l ../sponge_test/metazoa_odb9 -m tran -c 24

#tpm 1
../pipeline_scripts/filter_transrate.py \
-c /mnt/lustre/macmaneslab/nah1004/transcriptomes/reports/transrate_plsp/plsp.orthomerged/contigs.csv \
-p 1.0 \
-a /mnt/lustre/macmaneslab/nah1004/transcriptomes/assemblies/plsp.orthomerged.fasta \
-b plsp_trans1tpm1_rejected.txt \
-o plsp_trans1tpm1.fasta \
-t 1.0

run_BUSCO.py -i plsp_trans1tpm1.fasta -o plsp_trans1tpm1_busco \
-l ../sponge_test/metazoa_odb9 -m tran -c 24

#tpm 2
../pipeline_scripts/filter_transrate.py \
-c /mnt/lustre/macmaneslab/nah1004/transcriptomes/reports/transrate_plsp/plsp.orthomerged/contigs.csv \
-p 1.0 \
-a /mnt/lustre/macmaneslab/nah1004/transcriptomes/assemblies/plsp.orthomerged.fasta \
-b plsp_trans1tpm2_rejected.txt \
-o plsp_trans1tpm2.fasta \
-t 2.0

run_BUSCO.py -i plsp_trans1tpm2.fasta -o plsp_trans1tpm2_busco \
-l ../sponge_test/metazoa_odb9 -m tran -c 24

#tpm 3
../pipeline_scripts/filter_transrate.py \
-c /mnt/lustre/macmaneslab/nah1004/transcriptomes/reports/transrate_plsp/plsp.orthomerged/contigs.csv \
-p 1.0 \
-a /mnt/lustre/macmaneslab/nah1004/transcriptomes/assemblies/plsp.orthomerged.fasta \
-b plsp_trans1tpm3_rejected.txt \
-o plsp_trans1tpm3.fasta \
-t 3.0

run_BUSCO.py -i plsp_trans1tpm3.fasta -o plsp_trans1tpm3_busco \
-l ../sponge_test/metazoa_odb9 -m tran -c 24

#tpm 4
../pipeline_scripts/filter_transrate.py \
-c /mnt/lustre/macmaneslab/nah1004/transcriptomes/reports/transrate_plsp/plsp.orthomerged/contigs.csv \
-p 1.0 \
-a /mnt/lustre/macmaneslab/nah1004/transcriptomes/assemblies/plsp.orthomerged.fasta \
-b plsp_trans1tpm4_rejected.txt \
-o plsp_trans1tpm4.fasta \
-t 4.0

run_BUSCO.py -i plsp_trans1tpm4.fasta -o plsp_trans1tpm4_busco \
-l ../sponge_test/metazoa_odb9 -m tran -c 24

#tpm 7
../pipeline_scripts/filter_transrate.py \
-c /mnt/lustre/macmaneslab/nah1004/transcriptomes/reports/transrate_plsp/plsp.orthomerged/contigs.csv \
-p 1.0 \
-a /mnt/lustre/macmaneslab/nah1004/transcriptomes/assemblies/plsp.orthomerged.fasta \
-b plsp_trans1tpm7_rejected.txt \
-o plsp_trans1tpm7.fasta \
-t 7.0

run_BUSCO.py -i plsp_trans1tpm7.fasta -o plsp_trans1tpm7_busco \
-l ../sponge_test/metazoa_odb9 -m tran -c 24
