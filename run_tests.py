import subprocess
from argparse import ArgumentParser
#import("test_summary")

parser = ArgumentParser()
parser.add_argument("-f", "--files", nargs="+", dest="files", help="Define a .csproj file list.")

args = parser.parse_args()

for f in args.files:
	proc = subprocess.Popen('dotnet', stdout=subprocess.PIPE)
	tmp = str(proc.communicate()[0])
	subprocess.call("dotnet" +  " test " + '"' + f + '"')
