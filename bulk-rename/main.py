import os

def arrange_files(files,ext):
    files_with_ext = [file for file in files if file.endswith(ext)]

    if not(os.path.exists('images')):
        os.mkdir('images')
    for i , file in enumerate(files_with_ext):
        os.rename(file,f'images/img-{i+1}{ext}')
    # i = 1
    # for file in files_with_ext:
    #     os.rename(file,f'img-{i}{ext}')
    #     i += 1

if __name__ == '__main__':
    files = os.listdir()
    arrange_files(files,'.jpg')

