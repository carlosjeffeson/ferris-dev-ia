import sys
import os
import unittest

# src-layout fix
sys.path.insert(0, os.path.abspath("src"))

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="modules", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
