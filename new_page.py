""" This code defines and runs a "new_page" function. """

# Standard imports.
import os
import pathlib

#############
# FUNCTIONS #
#############

def new_page():
    """ Finds out what pages currently exist in the pages directory, and
    thereby comes up with an appropriately named new .md file, which is then
    opened in Gedit. """
    pages = os.listdir("pages/")
    pages.sort()
    for i in range(1, len(pages)+1):
        expected_filename = str(i)+".md"
        if pages[i-1] != expected_filename:
            raise Exception("Bad filename: "+pages[i-1])
    new_filename = "pages/"+str(len(pages)+1)+".md"
    pathlib.Path(new_filename).touch()
    os.system("gedit "+new_filename)

###################
# RUN AND WRAP UP #
###################

def run():
    new_page()

if __name__ == "__main__":
    run()
