from sqlalchemy import create_engine
import os

if os.path.exists("some.db"):
    os.remove("some.db")
e = create_engine("sqlite:///some.db")
e.execute("""
    create table employee (
        emp_id integer primary key,
        emp_name varchar
    )
""")

e.execute("""
    create table employee_of_month (
        emp_id integer primary key,
        emp_name varchar
    )
""")

e.execute("""insert into employee(emp_name) values ('ed')""")
e.execute("""insert into employee(emp_name) values ('jack')""")
e.execute("""insert into employee(emp_name) values ('fred')""")
