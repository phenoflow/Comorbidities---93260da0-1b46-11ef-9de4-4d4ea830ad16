# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"G38..00","system":"readv2"},{"code":"G301100","system":"readv2"},{"code":"G380.00","system":"readv2"},{"code":"3233","system":"readv2"},{"code":"G311000","system":"readv2"},{"code":"G311.00","system":"readv2"},{"code":"G30y200","system":"readv2"},{"code":"G384.00","system":"readv2"},{"code":"3232","system":"readv2"},{"code":"G312.00","system":"readv2"},{"code":"G350.00","system":"readv2"},{"code":"G35..00","system":"readv2"},{"code":"G310.00","system":"readv2"},{"code":"G353.00","system":"readv2"},{"code":"G307000","system":"readv2"},{"code":"G309.00","system":"readv2"},{"code":"14A4.00","system":"readv2"},{"code":"G381.00","system":"readv2"},{"code":"G307.00","system":"readv2"},{"code":"G32..00","system":"readv2"},{"code":"G30y.00","system":"readv2"},{"code":"14A3.00","system":"readv2"},{"code":"G301000","system":"readv2"},{"code":"G301.00","system":"readv2"},{"code":"14AH.00","system":"readv2"},{"code":"G30..00","system":"readv2"},{"code":"323..00","system":"readv2"},{"code":"G30y000","system":"readv2"},{"code":"3235","system":"readv2"},{"code":"G351.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('comorbidities-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["comorbidities-preinfarction---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["comorbidities-preinfarction---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["comorbidities-preinfarction---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
