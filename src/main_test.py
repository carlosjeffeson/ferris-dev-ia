import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="src/modules", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)