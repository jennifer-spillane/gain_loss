# Input data

Actual data are protein datasets that have already been translated using TransDecoder.
All have .pep names but differ from there.

Code that Dave gave me to convert headers into downstream-appropriate format:

This line changes each fasta header so that it is just ">count" eg >1, >2, >3, etc.
> awk '/^>/{print ">" ++i; next}{print}' < ./fastafile1.fa > genus_species.fa

This line replaces the greater than symbol with the string I provide.
It should be the genus and species separated by an underscore.
> perl -p -i -e 's/>/>genus_species|/g' genus_species.fa

I'll need to write out both of these lines for each dataset we have.
Example:
> awk '/^>/{print ">" ++i; next}{print}' < ./transdecoded_aas//Hormathia_digitata_pep.fa > Hormathia_digitata.fa
> perl -p -i -e 's/>/>Hormathia_digitata|/g' Hormathia_digitata.fa

It would be great to automate this step, but all the formats of the names are currently different.
Matt says he still knows a way to do it, so stay tuned for that update.
