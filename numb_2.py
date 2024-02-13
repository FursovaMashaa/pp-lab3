import os
import csv
import shutil
from typing import List


def create_dir(dir_name: str) -> None:
    """
    
    """
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

def name_change(past_name: str, new: str, file_types: List[str]) -> None:
    '''
   
    '''
    create_dir(new)
    abs_path = os.path.abspath(new)
    rel_path = os.path.relpath(new)
    for name in type:
        path = os.path.join(os.path.abspath(past_name), name)
        list_img = os.listdir(path)
        for img in list_img:
            shutil.copy(os.path.join(path, img), os.path.join(new, F'{name}_{img}'))


def create_csv2(dir_name: str, csv_name: str) -> None:
    """
    
    """
    abs_path = os.path.abspath(dir_name)
    rel_path = os.path.relpath(dir_name)
    img_f = os.listdir(dir_name)
    with open('annotation_2.csv', 'a') as f_csv:
        writer = csv.writer(f_csv, delimiter=',', lineterminator='\r')
        for img in img_f:
            writer.writerow([os.path.join(abs_path, img),
                             os.path.join(rel_path, img), img.split('_')[0]])               


def main() -> None:
    class_name = ['cat', 'dog']

    past_title = 'dataset_1'
    new_title = 'dataset_2'

    name_change(past_title, new_title, class_name)
    create_csv2(new_title, 'annotation2.csv')

if __name__ == "__main__":
    main()



