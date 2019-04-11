import argparse
from argparse import ArgumentParser
import os.path
import sys

def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.exists(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x

import re
def stripComments(code):
    code = str(code)
    for line in lines:
        # Keep the Shebang line
        if line[0:2] == "#!":
            f.writelines(line)
    return re.sub(r'*', '', code)

parser = ArgumentParser(description="Please provide your Inputs as -i InputFile -o OutPutFile")
parser.add_argument("-i", dest="InputFile", required=True,    help="Provide your Input file name here, if file is on different path than where this script resides then provide full path of the file", metavar="FILE", type=extant_file)
parser.add_argument("-o", dest="OutputFile", required=False,    help="Provide your Output file name here, if file is on different path than where this script resides then provide full path of the file", metavar="FILE")

args = parser.parse_args()

#Input file madatory
InputFile = args.InputFile

#Output file checks
if args.OutputFile is None:
    OutputFile = str(InputFile) + ".strip"
    print ("Setting Ouput file as "+ OutputFile)
else:
    OutputFile = args.OutputFile

    
with open(OutputFile, 'w') as f2:
    with open(InputFile, 'r', encoding='utf-8') as f1:
        for line in f1:
            # Write the line only if the comment was after the code.
            #line = line.split('#')
            #stripped_string = line[0].rstrip()
            # Discard lines that only contain comments.
            #if stripped_string:
            #    line = stripped_string     
            # Keep the Shebang line
            if line[0] == 0x2d0a0d:
                continue
            if line[0] == chr(12):
                continue
            if line[0] == "*":
                continue
            if len(line) < 5:      
                continue
            if 'GLOBAL RELATIONSHIP BANKING CITIBANK N.A. - TAIWAN' in line:
                continue
            if 'CUSTOMER NAME               CIN                 ACCOUNT TYPE      ACCOUNT/GRB NUMBER       DATE        TIME      USER ID' in line:
                continue
            if 'CUSTOMER NAME             CIN              ACCOUNT TYPE ACCOUNT/GRB ENROLL EMAIL                         DATE       TIME    USER ID' in line:
                continue
            if 'ACCOUNTS' in line:
                continue
            if 'ENROLLED' in line:
                continue
            if 'CANCELLED' in line:
                continue
            if 'DAILY COUNT         MONTH-TO-DATE        YEAR-TO-DATE' in line:
                continue
            if 'TOTAL CUSTOMERS CANCELLED' in line:
                continue
            if 'CONSOLIDATED STATEMENTS' in line:
                continue    
            if 'CREDIT CARD  STATEMENTS' in line:
                continue    
            if 'CANCELLATION SUMMARY' in line:
                continue
            if '* * *  END OF REPORT  * * *' in line:
                continue
            if 'ENROLLMENT SUMMARY' in line:
                continue
            if 'TOTAL PUSH' in line:
                continue
            if 'TOTAL PULL' in line:
                continue    
            if 'EZRB167' in line:
                continue
            if 'EZRB168' in line:
                continue
            if 'PAGE:' in line:
                continue
            # But remove comments from other lines
            else:
                line = line.encode('utf8', 'strict').decode('utf8')
                f2.writelines(str(line))
 
