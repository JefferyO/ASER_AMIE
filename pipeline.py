import argparse
from aser_table2tsv import aser2tsv
from mine_and_sort import m_n_s
from predict import derive_new_triples

if __name__ == "__main__":
    # arguments setting
    parser = argparse.ArgumentParser(description='API to handle the logic rule mining on ASER KB via AMIE+')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-wp", "--whole_pipeline", action="store_true", help="Run the whole pipeline.\n"
                                                                            + "Take the KB as input and output the sorted rule together with the found facts")
    group.add_argument("-a2t", "--aser2tsv", action="store_true", help="Extract triples (event1, relation, event2) from KB, store as tsv")
    group.add_argument("-m", "--mine_rule", action="store_true", help="Mine logic rule with AMIE+, tsv triples as input, output are sorted")
    group.add_argument("-p", "--predict", action="store_true", help="Predict new facts with mined rule")

    parser.add_argument("--db_path", type=str, help="/path/to/KG.db")
    parser.add_argument("--row_triples", type=str, help="/path/to/row_triples.tsv")
    parser.add_argument("--rule_path", type=str, help="/path/to/rule_you_provide.tsv")
    parser.add_argument("--new_prediction_path", type=str, help="/path/to/new_prediction.tsv")
    parser.add_argument("--amie_plus_path", type=str, help="/path/to/AMIE+/")
    parser.add_argument("--minhc", type=float, help="min head coverage threshold, default=0.01")
    parser.add_argument("--minc", type=float, help="min std confidence threshold, default=0.01")
    parser.add_argument("--minpca", type=float, help="min pca confidence threshold, default=0.01")

    args = parser.parse_args()

    if args.whole_pipeline:
        extracted_triples_path = aser2tsv(tsv_path=args.row_triples, db_path=args.db_path)
        sorted_rule_paths = m_n_s(tsv_source_path=extracted_triples_path, amie_path=args.amie_plus_path, minhc=args.minhc, minc=args.minc, minpca=args.minpca)
        derive_new_triples(mined_rules_path=sorted_rule_paths[0], original_triples_path=extracted_triples_path, new_triples_path=args.new_prediction_path)

    elif args.aser2tsv:
        aser2tsv(args.row_triples, args.db_path)

    elif args.mine_rule:
        m_n_s(tsv_source_path=args.row_triples, amie_path=args.amie_plus_path, minhc=args.minhc, minc=args.minc, minpca=args.minpca)

    elif args.predict:
        derive_new_triples(mined_rules_path=args.rule_path, original_triples_path=args.row_triples, new_triples_path=args.new_prediction_path)
