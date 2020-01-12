import csv

with open('test_predict_result.csv', 'r') as f:
    with open('triples_with_bootstrapping.tsv', 'r') as t:
        rdt = csv.reader(t, delimiter='\t')
        original_b1 = []
        original_b2 = []
        for rowt in rdt:
            if rowt[1] == 'Precedence':
                original_b1.append(rowt)
            if rowt[1] == 'Synchronous':
                original_b2.append(rowt)
        standard_var_match = [0, 1, 2, 1, 2, 0]
        standard_relation = ['Precedence', 'Synchronous', 'Synchronous']
        match_var = [0, 1, 2, 2, 2, 2]
        rule_var = []
        check_relation = True
        check_var_match = True
        check_exist = True
        rdf = csv.reader(f, delimiter='\t')
        count = 0
        next(rdf, None)
        for row in rdf:
            body1 = row[0:3]
            body2 = row[3:6]
            head = row[6:9]
            rule_var = [body1[0], body1[2], body2[0], body2[2], head[0], head[2]]

            for i in range(2, 6):
                if rule_var[i] == rule_var[0]:
                    match_var[i] = 0
                if rule_var[i] == rule_var[1]:
                    match_var[i] = 1

            if body1[1] != standard_relation[0] or body2[1] != standard_relation[1] or head[1] != standard_relation[2]:
                check_relation = False
                break

            elif match_var != standard_var_match:
                check_relation = False
                break

            elif (not(body1 in original_b1)) or (not(body2 in original_b2)):
                check_exist = False

            else:
                print('correct')
                count += 1

            if not(check_relation and check_var_match and check_exist):
                print(row)
                if not check_var_match:
                    print('wrong var match')
                elif not check_exist:
                    print('body not exist originally')
                else:
                    print('wrong relation')

        print(count)
