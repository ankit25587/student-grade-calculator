import sys
from pathlib import Path

# Add the root directory to sys.path so pytest can import grades module
sys.path.insert(0, str(Path(__file__).parent))
