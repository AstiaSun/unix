#!/bin/bash

find_files(){
	search_dir=$1
	if [[ $search_dir != */ ]]; then  search_dir="${search_dir}/"; fi
        files=()
	for dir in $(find $search_dir -type d); do
		for file in ${dir}/$2*; do
			if [ -e "$file" ]; then
				files=("${files[@]}" "$dir")
				break
			fi
		done
	done 
}


if [[ $# -ne 2 ]]; then	echo "Error: incorrect amount of parameters"; exit 1; fi

find_files $1 $2
echo "File name?"
read -r -p "" filename
echo "$filename"
> "$filename"
for f in ${files[@]}; do
	echo "${f}" >> "$filename"
done
