import sys
import os

# Add the src directory to the Python module search path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# from src.main import main

if __name__ == "__main__":
    try:
        from src.main import main
    except ImportError:
        sys.exit()
    
    main()