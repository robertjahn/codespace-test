import os

print("hello world")
print("TEST_VAR1 = " + os.getenv("TEST_VAR1", ""))
print("TEST_VAR2 = " + os.getenv("TEST_VAR2", ""))
print("TEST_VAR3 = " + os.getenv("TEST_VAR3", ""))
