import gzip
import os

def unzip_gz_files(directory, dest_directory):
    # Unzip all .gz files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.gz'):
            
            # Set up all necessary paths
            filepath = os.path.join(directory, filename)
            base_name = os.path.basename(filepath)
            base_name = os.path.splitext(base_name)[0]
            output_filepath = os.path.join(dest_directory, base_name)
            
            # Decompress the .gz file to the output file
            with gzip.open(filepath, 'rb') as gz_file:
                with open(output_filepath, 'wb') as out_file:
                    out_file.write(gz_file.read())
            print(f"Decompressed: {filename} to {output_filepath}")
            

if __name__ == "__main__":
    directory_path = './data/'
    dest_directory = './data/unzipped_data'
    unzip_gz_files(directory_path, dest_directory)