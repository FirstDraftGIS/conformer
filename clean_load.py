from csv import DictReader
from re import search
from subprocess import call
from subprocess import CalledProcessError
from subprocess import check_output
from subprocess import PIPE
from subprocess import Popen
from subprocess import STDOUT
from time import sleep

with open("/tmp/conformed.tsv") as f:
    fieldnames = DictReader(f, delimiter="\t").fieldnames

sql_statement = "COPY appfd_place FROM '/tmp/conformed.tsv' WITH (FORMAT 'csv', DELIMITER E'\t', HEADER, NULL '');"
bash_statement = 'sudo -u postgres psql -c "' + sql_statement + '" conformer'
run_please = True
while run_please:
    sub = Popen(bash_statement, shell=True, stdout=PIPE, stderr=PIPE)
    output, error_output = sub.communicate()
    print("output:", [output])
    print("error_output:", [error_output])
    if error_output:
        print(error_output)
        if error_output.startswith(b'ERROR:  value too long for type'):
            line_number = search(b"(?<=line )\d+", error_output).group(0).decode()
            print("line_number:", line_number)
            #column_name = search(b"(?<=column )[a-z_]+(?=:)", error_output).group(0)
            #print("column_name:", column_name)
            #column_number = fieldnames.index(column_name.decode())
            #print("column_number:", column_number)
            deletion_command = "sed -i -e '" + line_number + "d' /tmp/conformed.tsv"
            print("deletion_command:", [deletion_command])
            call(deletion_command, shell=True)
        else:
            run_please = False
    else:
        run_please = False
    sleep(5)

print("finishing clean load")