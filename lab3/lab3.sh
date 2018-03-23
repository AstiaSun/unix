#!/bin/bash

if [[ $# -ne 2 ]]; then echo -e "ERROR. Incorrect number of parameters.\nUsage:\n$0 path_to_reg_exp_file path_to_text_file"; exit 1; fi

read_file() {
	output=`cat $1`
	echo "$output"
}

re=$(read_file $1)

echo "${re}"

output=$(grep -oh "${re}" $2)

echo "Output file: "
read filename

echo "$output" > "$filename"
