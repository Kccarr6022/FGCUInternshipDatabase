import jaydebeapi as jdbc
from jaydebeapi import Error
import PySimpleGUI as sg

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
       :param conn: Connection object
       :param create_table_sql: a CREATE TABLE statement
       :return:
       """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\Users\ragyc\OneDrive\COP3710\Project\InterhsipDB\internshipDB.db"

    create_person_table = """ CREATE TABLE IF NOT EXISTS Person (
                                personID integer primary key,
                                firstName text NOT NULL,
                                middleName text,
                                lastName text NOT NULL,
                                gender char NOT NULL,
                                address text NOT NULL,
                                dateOfBirth date NOT NULL,
                                phoneNUmber integer NOT NULL,
                                email text NOT NULL,
                                );"""

    create_student_table = """CREATE TABLE IF NOT EXISTS Student(
                                studentID integer primary key,
                                skills text NOT NULL,
                                major text NOT NULL,
                                minor text NOT NULL,
                                FOREIGN KEY (studentID) REFERENCES Person (personID) );"""

    create_major_table = """CREATE TABLE IF NOT EXISTS Major(
                                majorID text primary key, 
                                minorID text primary key,
                                majorName text NOT NULL,
                                FOREIGN KEY (minorID) REFERENCES Major (majorID));"""

    """!!!!!we might need a job table or the internship id linked to this"""
    create_company_table = """CREATE TABLE IF NOT EXISTS Company(
                                companyID integer primary key,
                                companyNAme text NOT NULL,
                                address text NOT NULL,
                                linkToWeb text NOT NULL,
                                );"""

    create_internship_table = """CREATE TABLE IF NOT EXISTS Internship(
                                    internshipID integer primary key,
                                    jobTitle text NOT NULL,
                                    jobDesc text NOT NULL,
                                    salary float(2) NOT NULL,
                                    ft_or_pt text NOT NULL,
                                    os_or_re text NOT NULL,
                                    requirement text NOT NULL);"""

    """Relationship Tables"""
    create_takes_relTable = """CREATE TABLE IF NOT EXISTS Takes(
                                studentID integer primary key,
                                internshipID integer primary key,
                                FOREIGN KEY (studentID) REFERENCES Student (studentID),
                                FOREIGN KEY (internshipID) REFERENCES Internship (internshipID) );"""


    create_hires_relTable = """CREATE TABLE IF NOT EXISTS Hires(
                                studentID integer primary key,
                                companyID integer primary key,
                                startDate date NOT NULL,
                                endDate date NOT NULL,
                                FOREIGN KEY (studentID) REFERENCES Student (studentID),
                                FOREIGN KEY (companyID) REFERENCES Comapny (comapnyID)
                                );"""

    create_offers_relTable = """CREATE TABLE IF NOT EXISTS Offers(
                                    companyID integer primary key,
                                    internshipID integer primary key,
                                    FOREIGN KEY (companyID) REFERENCES Company (companyID),
                                    FOREIGN KEY (internshipID) REFERENCES Internship (internshipID));"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        #create person table
        create_table(conn, create_person_table)

        #create student table
        create_table(conn, create_student_table)

        #create major table
        create_table(conn, create_major_table)

        #create company table
        create_table(conn, create_company_table)

        #create internship table
        create_table(conn, create_internship_table)

        #create takes relationship table
        create_table(conn, create_takes_relTable)

        # create takes relationship table
        create_table(conn, create_hires_relTable)

        #create takes relationship table
        create_table(conn, create_offers_relTable)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()