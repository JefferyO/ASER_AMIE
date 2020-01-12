import pandas
import subprocess
import os


def m_n_s(tsv_source_path, amie_path, minhc=0.01, minc=None, minpca=None):
    amie_arg = "java -XX:-UseGCOverheadLimit -Xmx4G -jar " + amie_path + " " + tsv_source_path

    if minhc != 0.01 and minhc:
        amie_arg += " -minhc "
        amie_arg += str(minhc)
    if minc:
        amie_arg += " -minc "
        amie_arg += str(minc)
    if minpca:
        amie_arg += " -minpca "
        amie_arg += str(minpca)

    # tsv_target_path = "result_" + tsv_source_path
    open('result.txt', 'w').close()     # clean up the old content in result.txt
    amie_arg += " >>result.txt"
    print(amie_arg)
    os.system(amie_arg)

    cols = [[] for x in range(11)]
    with open("result.txt", 'r') as source:
        for line in source:
            if line[0] == '?':
                current_line = line.split()
                # print(current_line)
                if len(current_line) != 0:
                    current_rule = ''
                    if len(current_line) == 20:
                        for i in range(0, 10):
                            current_rule = current_rule + current_line[i] + ' '
                        cols[0].append(current_rule)

                        for j in range(10, 20):
                            if current_line[j][0] != '?':
                                cols[j - 9].append(float(current_line[j]))
                            else:
                                cols[j - 9].append(current_line[j])
                    else:
                        for i in range(0, 7):
                            current_rule = current_rule + current_line[i] + ' '
                        cols[0].append(current_rule)

                        for j in range(7, 17):
                            if current_line[j][0] != '?':
                                cols[j - 6].append(float(current_line[j]))
                            else:
                                cols[j - 6].append(current_line[j])

    df = pandas.DataFrame({
            'rule': cols[0],
            'v1': cols[1],
            'v2': cols[2],
            'v3': cols[3],
            'v4': cols[4],
            'v5': cols[5],
            'v6': cols[6],
            'v7': cols[7],
            'v8': cols[8],
            'v9': cols[9],
            'v10': cols[10],
        })

    current_dir = os.path.abspath(os.path.dirname("__file__"))

    pca_sorted_path = os.path.join(current_dir, "pca_sorted_rule.tsv")
    std_sorted_path = os.path.join(current_dir, "std_sorted_rule.tsv")
    sorted_by_pca = df.sort_values(by='v3', ascending=False)
    sorted_by_std = df.sort_values(by='v2', ascending=False)
    sorted_by_pca.to_csv(pca_sorted_path, sep='\t')
    sorted_by_std.to_csv(std_sorted_path, sep='\t')

    return pca_sorted_path, std_sorted_path
