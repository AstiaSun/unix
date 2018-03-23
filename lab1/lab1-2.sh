#!/bin/bash

if [[ $# -ne 2 ]]; then echo -e "ERROR. Incorrect number pf parameters.\nUsage:\n$0 [source_directory] [target_directory]\n"; exit 1; fi

source_dir=$1
target_dir=$2

process_errors_in_dir_name(){
	local dir=$1
	if [[ $dir != */ ]]; then dir="${dir}/"; fi
	echo ${dir}
}

source_dir=$(process_errors_in_dir_name ${source_dir})
target_dir=$(process_errors_in_dir_name ${target_dir})

if [[ $source_dir -eq $target_dir ]]; then echo "ERROR. Source and target directory coincides."; exit 1; fi

echo "Enter symbols how the filenames starts:"
read prefix

echo "Enter max size in bytes:"
read max_size

re='^[0-9]+$'
if ! [[ "$max_size" =~ $re ]]; then echo "ERROR. Invalid input. Specify a digit."; exit 1; fi

total_size=0
number_of_files=0
for file in ${source_dir}$prefix*; do
	if [ -e "$file" ]; then
		size=$(stat -c%s "$file")
		if [[ $size -le $max_size ]]; then 
			cp "${file}" "${target_dir}."
			total_size=$((total_size + size))
			((number_of_files++))
		fi
	fi
done
echo -e "Files transfered:\t$number_of_files"
echo -e "Bytes transfered:\t$total_size"
