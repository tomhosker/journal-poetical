""" This code defines and runs an "open_last" function. """

# Standard imports.
import os

#############
# FUNCTIONS #
#############

def open_last():
    """ Finds out what pages currently exist in the pages directory, and
    thereby opens the last one. """
    pages = os.listdir("pages/")
    pages.sort()
    last_filename = "pages/"+str(len(pages))+".md"
    os.system("gedit "+last_filename)

###################
# RUN AND WRAP UP #
###################

def run():
    open_last()

if __name__ == "__main__":
    run()
