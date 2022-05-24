import os
from contextlib import contextmanager

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import sql


engine = create_engine(os.environ['DATABASE_URI'])


@contextmanager
def transaction():
    with engine.begin() as conn:
        yield conn


def create_db():
    statement = sql.text('''
    CREATE TABLE IF NOT EXISTS buildtargets(
      id INTEGER PRIMARY KEY AUTO_INCREMENT,
      git_branch VARCHAR(255) UNIQUE NOT NULL,
      git_commit VARCHAR(255) NOT NULL,
      buildtarget_name VARCHAR(255) UNIQUE NOT NULL)
    ''')
    with transaction() as conn:
        conn.execute(statement)


def add_build_target(**values):
    statement = sql.text('''INSERT INTO buildtargets
        (git_branch, git_commit, buildtarget_name)
        VALUES (:git_branch, :git_commit, :buildtarget_name)
    ''')
    with transaction() as conn:
        conn.execute(statement, **values)


def get_build_target_by_branch(git_branch):
    statement = sql.text('SELECT * FROM buildtargets WHERE git_branch=:branch')
    with transaction() as conn:
        rs = conn.execute(statement, branch=git_branch)
        return rs.mappings().all()


def update_branch(git_branch, new_commit):
    statement = sql.text(
        'UPDATE buildtargets SET git_commit=:sha WHERE git_branch=:branch'
    )
    with transaction() as conn:
        conn.execute(statement, sha=new_commit, branch=git_branch)


def delete_buildtarget_for_branch(git_branch):
    statement = sql.text(
        'DELETE FROM buildtargets WHERE git_branch=:branch'
    )
    with transaction() as conn:
        conn.execute(statement, branch=git_branch)
