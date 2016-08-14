#! /usr/bin/python3
"""Setup module
"""

import model

def main():
    print("Creating the database structure:")
    model.Base.metadata.create_all(model.engine)


if __name__ == "__main__":
    main()
