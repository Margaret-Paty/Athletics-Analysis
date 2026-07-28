from src.retrieve_data import retrieve_data

from src.structure.structure_activities import structure_activities
from src.structure.structure_sleep import structure_sleep

from src.clean.clean_activity_data import clean_activities
from src.clean.clean_sleep_data import clean_sleep

from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    try: 
        logger.info("starting Garmin pipeline")

        logger.info("Retrieving Garmin data")
        retrieve_data()

        logger.info("Structuring activity data")
        structure_activities()

        logger.info("structuring sleep data")
        structure_sleep()

        logger.info("cleaning activity data")
        clean_activities()

        logger.info("cleaning sleep data")
        clean_sleep()

        logger.info("pipeline complete")
    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    main()
    
