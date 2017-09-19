#!/usr/bin/env python2

import argparse
import os
import sys
import sqlite3

class Sqlite:
    def __init__(self):
        self.open()

    def open(self):
        self.conn = sqlite3.connect( "=>replace me<=" )
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def create_table(self):
        try:
            self.cur.execute("""create table pyccd(
                    name text primary key,
                    path text
                )""")
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print e        

    def insert_path(self, name, path):
        path = os.path.abspath( os.path.realpath(path) )
        self.cur.execute("""insert into pyccd(name, path) values (?, ?)""", (name, path))
        self.commit()

    def update_path(self, name, path):
        path = os.path.abspath( os.path.realpath(path) )
        self.cur.execute("update pyccd set path = ? where name = ?", (path, name))
        self.commit()

    def delete_path(self, names):
        self.cur.executemany("delete from pyccd where name = ?", [(each_name,) for each_name in names])
        self.commit()

    def clear_path(self):
        self.cur.execute("delete from pyccd")
        self.commit()

    def list_all(self):
        for each in self.cur.execute("select * from pyccd"):
            yield each

    def list_similar(self, partial):
        for each in self.cur.execute("select * from pyccd where name like ?", ('%' + partial + '%', )):
            yield each
    
    def getpath(self, name):
        self.cur.execute("select path from pyccd where name = ?", (name, ))
        return self.cur.fetchone()



def error_exit(msg, exit_code=1):
    sys.stderr.write("[ERROR]: {}\n".format(msg))
    sys.exit( exit_code )

def handle_insert(args):
    if args.name[0] == '-':
        error_exit("<path name> should not starts with '-'")
    sql = Sqlite()
    sql.insert_path( args.name, args.path )
    sql.close()

def handle_delete(args):
    sql = Sqlite()
    sql.delete_path( args.name )
    sql.close()

def handle_avail(args):
    sql = Sqlite()
    if args.name:
        for each in sql.list_similar(args.name):
            print "{}: {}".format(each[0], each[1])
    else:
        for each in sql.list_all():
            print "{}: {}".format(each[0], each[1])
    sql.close()

def handle_clear(args):
    sql = Sqlite()
    sql.clear_path()
    sql.close()

def handle_create(args):
    sql = Sqlite()
    sql.create_table()
    sql.close()

def handle_update(args):
    sql = Sqlite()
    sql.update_path(args.name, args.path)
    sql.close()

def handle_getpath(args):
    sql = Sqlite()
    path = sql.getpath(args.name)
    sql.close()
    if path:
        print path[0]
    else:
        print

def parse_args():
    parser = argparse.ArgumentParser(description = "ccd python engine")
    subparsers = parser.add_subparsers(title = "subcmds", dest = "subcmd")

    parser_insert = subparsers.add_parser("insert", help="insert a convenient path")
    parser_insert.add_argument("name", help="path name")
    parser_insert.add_argument("path", help="path")

    parser_delete = subparsers.add_parser("delete", help="delete one or more paths by name")
    parser_delete.add_argument("name", nargs='+', help="path name(s)")

    parser_avail = subparsers.add_parser("avail", help="list available path names")
    parser_avail.add_argument("-n", "--name", help="get available similar path names")

    parser_clear = subparsers.add_parser("clear", help="clear all the paths")
    parser_create = subparsers.add_parser("create", help="create database")
    parser_update = subparsers.add_parser("update", help="update a path")
    parser_update.add_argument("name", help="path name")
    parser_update.add_argument("path", help="path")

    parser_getpath = subparsers.add_parser("getpath", help="get path by name")
    parser_getpath.add_argument("name", help="path name")

    return parser.parse_args()

def main():
    args = parse_args()
    subcommands = {"insert": handle_insert,
                   "delete": handle_delete,
                   "avail":  handle_avail,
                   "clear": handle_clear,
                   "create": handle_create,
                   "update": handle_update,
                   "getpath": handle_getpath}
    subcommands[ args.subcmd ]( args )

if __name__ == '__main__':
    main()
