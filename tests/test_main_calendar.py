import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)

from src import main_calendar as mcal

# INSERT_ANY_TEST_HERE