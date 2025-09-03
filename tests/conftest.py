import os
from pathlib import Path
import sys

current_dir = Path(__file__).resolve().parent

# Navigate up two levels to the project's root directory
# This brings you to C:\Users\nick\Desktop\LearningStuff\CodeBasics - Bootcamp\GymProgressTracker
project_root = current_dir.parent

# Add the project's root directory to the beginning of sys.path
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

print(f"Added to Python Path: {project_root}")