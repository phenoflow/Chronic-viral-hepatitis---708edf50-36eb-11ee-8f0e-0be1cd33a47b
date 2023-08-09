# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"A703.00","system":"readv2"},{"code":"A707.00","system":"readv2"},{"code":"A707200","system":"readv2"},{"code":"A707300","system":"readv2"},{"code":"A70z000","system":"readv2"},{"code":"100834.0","system":"med"},{"code":"102565.0","system":"med"},{"code":"102568.0","system":"med"},{"code":"104243.0","system":"med"},{"code":"104341.0","system":"med"},{"code":"104346.0","system":"med"},{"code":"104572.0","system":"med"},{"code":"104892.0","system":"med"},{"code":"105664.0","system":"med"},{"code":"106642.0","system":"med"},{"code":"107896.0","system":"med"},{"code":"108343.0","system":"med"},{"code":"110411.0","system":"med"},{"code":"2413.0","system":"med"},{"code":"24813.0","system":"med"},{"code":"26367.0","system":"med"},{"code":"27174.0","system":"med"},{"code":"27175.0","system":"med"},{"code":"27191.0","system":"med"},{"code":"2834.0","system":"med"},{"code":"28568.0","system":"med"},{"code":"2860.0","system":"med"},{"code":"30586.0","system":"med"},{"code":"30884.0","system":"med"},{"code":"32277.0","system":"med"},{"code":"32657.0","system":"med"},{"code":"33316.0","system":"med"},{"code":"35589.0","system":"med"},{"code":"41096.0","system":"med"},{"code":"50245.0","system":"med"},{"code":"56066.0","system":"med"},{"code":"95926.0","system":"med"},{"code":"96085.0","system":"med"},{"code":"97735.0","system":"med"},{"code":"98903.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-viral-hepatitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hepatitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hepatitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hepatitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
