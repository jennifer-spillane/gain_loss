#! bin/bash
echo "Type the path to the directory containing the fasta files"
read dir_name
#echo ""
cd $dir_name
for file_name in *.pep
do
    awk '/^>/{print ">" ++i; next}{print}' < ./$file_name > genus_species.fa
done
