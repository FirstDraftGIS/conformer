from csv import DictReader
from re import search
from subprocess import call
from subprocess import check_output
from subprocess import PIPE
from subprocess import Popen
from time import sleep

with open("/tmp/conformed.tsv") as f:
    fieldnames = DictReader(f, delimiter="\t").fieldnames

sql_statement = "COPY appfd_place FROM '/tmp/conformed.tsv' WITH (FORMAT 'csv', DELIMITER E'\t', HEADER, NULL '');"
bash_statement = 'sudo -u postgres psql -c "' + sql_statement + '" conformer'
run_please = True
while run_please:
    sub = Popen(bash_statement, shell=True, stdout=PIPE, stderr=PIPE)
    output, error_output = sub.communicate()
    print("output:", output)
    print("error_output:", error_output)
    if error_output:
        print(error_output)
        if b'ERROR:  value too long for type' in error_output:
            line_number = search(b"(?<=line )\d+", error_output).group(0).decode()
            deletion_command = "sed -i -e '" + line_number + "d' /tmp/conformed.tsv"
            print("running: " + deletion_command)
            deletion_output = check_output(deletion_command, shell=True)
            print(deletion_output)
        else:
            run_please = False
    else:
        run_please = False
    sleep(1)

print("finishing clean load")
