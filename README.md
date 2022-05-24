**Note:** Please do not fork this repository. Just clone it.

# Overview

The provided project includes Python code to interact with a simple database schema (database.py). The database schema represents info on Git branches in a cloud build system.

There is a test_database.py file that is intended to contain tests for the database functions. This exercise involves adding tests for the database code to this file.

# Task 1

The provided Dockerfile installs Python, and then uses the Pytest library (https://docs.pytest.org/en/7.1.x/).

Improve the provided Dockerfile based on the following requirements:
1. Minimize the number of vulnerabilities reported by `docker scan` so that the only vulnerabilities reported are those from the base Ubuntu Docker image. (As the Ubuntu image has a number of vulnerabilities, avoiding these is not a requirement, but you should be able to remove vulnerabilities resulting from other dependencies, e.g. packages).
2. In particular, you should use a multi-stage Docker build so that the final image only contains the minimal dependencies required to run the tests.
3. Update the Dockerfile so that it uses a non-root user to run `pip3 install` and `pytest` in order to improve security.
4. Reduce the number of intermediate image layers in the build.

**Your improved Dockerfile should still use Python 3.10 built from source.**

# Task 2

The goal is to set up a simple automated testing system for the database code that could be run as a part of a continuous integration (CI) pipeline. This should use MySQL version 5.7.

We want to check a number of test cases. Your automated tests should cover:
- After creating an empty database using create_db(), there should be no rows in the database table.
- The get_build_target_by_branch() function should work correctly if a valid Git branch is specified.
- The add_build_target() function should fail if specifying a Git branch that already exists in the database.
- Updating the commit SHA for a branch using update_branch() should work correctly.

Please also implement two tests of your own design that you think would be useful.

Requirements:
1. Write a docker-compose file that starts a MySQL 5.7 Docker container (https://hub.docker.com/_/mysql), and alongside it starts the Docker image to run the database tests using the MySQL container.
2. Implement tests in test_database.py based on the test cases discussed above.
3. Each test should be a separate Python function using the Pytest framework.
4. At the start of each test, the database should be empty with no tables.
5. The whole testing process should be able to be run from a single CLI command on a developer’s local machine.
6. Tests should run as quickly as possible (e.g. creating a new database Docker container for every test case is not desirable).
7. If you write any SQL code for the tests, avoid using string formatting to build queries, in order to help protect against SQL injection.

*Technical notes:*
The requirements.txt file includes PyMySQL, so you can specify a database URI using the following format: mysql+pymysql://root:password@host:3306/database
For setting up tests, it may be helpful to use Pytest fixtures: https://docs.pytest.org/en/7.0.x/fixture.html
