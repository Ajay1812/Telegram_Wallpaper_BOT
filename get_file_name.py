import os

def extract_movie_file_paths(base_dir):
    movie_extensions = ['.mkv', '.mp4', '.avi', '.mov']
    movie_files = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if any(file.endswith(ext) for ext in movie_extensions):
                movie_files.append(os.path.join(root, file).replace(base_dir, '').lstrip('/'))
                
    return movie_files


def extract_image_paths(base_dir):
    movie_extensions = ['.jpg','.png','.jpeg']
    movie_files = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if any(file.endswith(ext) for ext in movie_extensions):
                movie_files.append(os.path.join(root, file).replace(base_dir, '').lstrip('/'))
                
    return movie_files



# base_dir = '/Users/ajay/Documents/Personal/Movies'

# extracted_files = extract_movie_file_names(base_dir)

# print(extracted_files)
# for file_name in extracted_files:
#     print(file_name)

# with open('movie_file_names.txt', 'w') as f:
#     for file_name in extracted_files:
#         f.write(file_name + '\n')
