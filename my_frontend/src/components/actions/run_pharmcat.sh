#!/bin/bash
# input_file_name=pharmcat_tool/input_data/pharmcat.example.vcf
# destination_path=$2
input_file_name=$1

source ./venv/bin/activate
ls $input_file_name
./pharmcat_tool/pharmcat_pipeline $input_file_name #-o $destination_path

# if [ $? -ne 0 ]; then
#   echo "Tool failed to run. Exiting script."
#   exit 1
# fi