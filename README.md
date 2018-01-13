# unix_tree_command
Given a path to a directory, recursively print the contents of that directory

Example:

$ python tree_directory.py /tmp/somedir

somedir
|--- subdir1
|      |--- file1.txt
|      |--- image1.png
|--- subdir2
|     |--- file2.txt
|     |--- image2.png
|--- file.txt
|--- image.png

$ python tree_directory.py /tmp/somedir --rtl

                                  somedir
                             subdir1 ---|
                     file1.txt  ---|    |
                    image1.png  ---|    |
                             subdir2 ---|
                     file2.txt  ---|    |
                    image2.png  ---|    |
                            file.txt ---|
                           image.png ---|
