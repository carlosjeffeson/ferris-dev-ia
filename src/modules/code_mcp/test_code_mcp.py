# src/modules/code_mcp/test_code_mcp.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import unittest
from .code_mcp_client import list_files, execute_command

class TestCodeMCPClient(unittest.TestCase):

    def test_list_files(self):
        files = list_files()
        self.assertIsInstance(files, list)
        self.assertTrue(all(isinstance(file, str) for file in files))

    def test_execute_command(self):
        output = execute_command("echo Hello MCP!")
        self.assertIn("Hello MCP!", output)

if __name__ == "__main__":
    unittest.main()