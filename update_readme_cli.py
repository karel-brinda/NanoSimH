#! /usr/bin/env python3

import argparse
import os
import sys
import re
import subprocess

def rest_cli(command):
	p=subprocess.check_output(command)
	out=p.decode('unicode_escape')
	s=out.split("\n")
	s=list(map(lambda x: "	"+x, s))
	return "\n.. code-block::\n\n" + "\n".join(s) + "\n"


def main():

	out=[]

	command_mode=False

	with open('README.rst', 'r') as readme:
		for x in readme:
			if len(x)>0:
				x=x[:-1]
			if command_mode==False:
				out.append(x)
				if x.find(".. command: ")==0:
					command=x.replace(".. command: ","")
					out.append(rest_cli(command.split(" ")))
					command_mode=True
			else:
				if x.find(".. end"):
					out.append(x)
					command_mode=False
	print("\n".join(out))


if __name__ == "__main__":
	main()