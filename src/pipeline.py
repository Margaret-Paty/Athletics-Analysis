from src.retrieve_data import retrieve_data

from src.structure.structure_activities import structure_activities
from src.structure.structure_sleep import structure_sleep

from src.clean.clean_activity_data import clean_activities
from src.clean.clean_sleep_data import clean_sleep

def main():
    print("=" * 50)
    print("Athletics Analysis Pipeline")
    print("=" * 50)

    print("\nretrieving data ")
    retrieve_data()

    print("\nstructuring activities ")
    structure_activities()

    print("\nstructuring sleep ")
    structure_sleep()

    print("\ncleaning activities ")
    clean_activities()

    print("\ncleaning sleep ")
    clean_sleep()

    print("\n pipeline complete")

if __name__ == "__main__":
    main()
    

