# ASER_AMIE
A Python pipeline for using AMIE+ to mine logic rules and instantiate new facts.
Initially designed for mining new relations for [ASER](https://hkust-knowcomp.github.io/ASER/)
## Settings and Dependencies:
* Python 3.7
* [AMIE+](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/amie/)
## Usage:
* Show help message and descriptions of arguments
```Bash
python pipeline.py -h
```
* Run the whole pipeline (Only for [ASER Knowledge Graph](https://github.com/HKUST-KnowComp/ASER)):
```Bash
python pipeline.py -wp --row_triples /path/to/row_triples.tsv --db_path DB_PATH /path/to/KG.db --amie_plus_path /path/to/AMIE+.jar --new_prediction_path /path/to/new_prediction.tsv
```
With this command, the pipeline will first extract RDF triples from ASER format database into .tsv file. Then it will run AMIE+ on the .tsv file to mine all logical rules within preset threshold. Finally it will instantiate new RDF facts by grounding the mined rules to orignal triples. 

* Run pipeline for other knowledge base:

  * Mine logical rules with AMIE+:
  ```Bash
  python pipeline.py -m --row --row_triples /path/to/row_triples.tsv --amie_plus_path /path/to/AMIE+.jar 
  ```
  The mined rules will be sorted according to the PCA and STD confidence repectively and saved in "pca_sorted_rule.tsv" and     "std_sorted_rule.tsv" in the module directory.

  * Predict/Instantiate new facts with mined/provided rules:
  ```Bash
  python pipeline.py -p --rule_path /path/to/rule_you_provide.tsv --row_triples /path/to/row_triples.tsv ----new_prediction_path /path/to/new_prediction.tsv
  ```
