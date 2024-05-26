# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"K0z..00","system":"readv2"},{"code":"792Dz00","system":"readv2"},{"code":"7926z00","system":"readv2"},{"code":"7928z00","system":"readv2"},{"code":"G3z..00","system":"readv2"},{"code":"G330z00","system":"readv2"},{"code":"Gyu6G00","system":"readv2"},{"code":"G301z00","system":"readv2"},{"code":"G34z.00","system":"readv2"},{"code":"ZV45L00","system":"readv2"},{"code":"7922z00","system":"readv2"},{"code":"G34yz00","system":"readv2"},{"code":"7924z00","system":"readv2"},{"code":"G305.00","system":"readv2"},{"code":"G6W..00","system":"readv2"},{"code":"G33zz00","system":"readv2"},{"code":"322Z.00","system":"readv2"},{"code":"7929z00","system":"readv2"},{"code":"G304.00","system":"readv2"},{"code":"G6X..00","system":"readv2"},{"code":"792Bz00","system":"readv2"},{"code":"G30z.00","system":"readv2"},{"code":"7927z00","system":"readv2"},{"code":"G30yz00","system":"readv2"},{"code":"792Cz00","system":"readv2"},{"code":"G31yz00","system":"readv2"},{"code":"Gyu6500","system":"readv2"},{"code":"7923z00","system":"readv2"},{"code":"323Z.00","system":"readv2"},{"code":"Gyu6300","system":"readv2"},{"code":"792z.00","system":"readv2"},{"code":"792Az00","system":"readv2"},{"code":"G311z00","system":"readv2"},{"code":"7920z00","system":"readv2"},{"code":"G308.00","system":"readv2"},{"code":"7921z00","system":"readv2"},{"code":"Gyu6600","system":"readv2"},{"code":"G33z.00","system":"readv2"},{"code":"7925z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('comorbidities-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["comorbidities-stenosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["comorbidities-stenosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["comorbidities-stenosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
