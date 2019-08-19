import shutil
import pymysql
import os
from reportlab.lib.units import inch
from report import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from doc_test import *
from reportlab.platypus import *
from reportlab.lib import colors


def data_for_table(run_id):

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()

    cur.execute('select `id`,`distance`, `feature`, `joint` ,`length`, `depth` ,`width`, `angle` , `clock` , `remark` '
                'from inspection_feature_list where runId =%s', run_id)

    table_inspection = cur.fetchall()

    list_table_attributes = ['Id', 'Distance', 'Feature', 'Joint', 'Length', 'Depth', 'Width', 'Angle', 'O` clock', 'Remarks']
    table_inspection_list = list(table_inspection)
    color_to_use = [colors.lavender, colors.floralwhite]
    table_inspection_list.insert(0, list_table_attributes)
    t = Table(table_inspection_list, style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                            ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                            ('BACKGROUND', (0, 0), (9, 0), colors.grey),
                                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                            ])
    return t


def data_for_table_1():

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()

    cur.execute('select `parameter`,`parameter_value` '
                'from runsummary ')

    new_table = cur.fetchall()

    list_table_attributes = ['Parameter', 'Parameter Value']
    new_table = list(new_table)
    color_to_use = [colors.lavender, colors.floralwhite]
    new_table.insert(0, list_table_attributes)
    t = Table(new_table, colWidths=[3*inch]*2, style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                            ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
                                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                            ])
    return t


def data_for_table_14():

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()

    cur.execute('select `parameter`,`parameter_value` '
                'from primary_sensor_performace ')

    new_table = cur.fetchall()

    list_table_attributes = ['Parameter', 'Parameter Value']
    new_table = list(new_table)
    color_to_use = [colors.lavender, colors.floralwhite]
    new_table.insert(0, list_table_attributes)
    t = Table(new_table, colWidths=[3*inch]*2, style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                            ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
                                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                            ])
    return t


def data_for_table_15():

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()

    cur.execute('select `parameter`,`parameter_value` '
                'from inertial_sensor_performance ')

    new_table = cur.fetchall()

    list_table_attributes = ['Parameter', 'Parameter Value']
    new_table = list(new_table)
    color_to_use = [colors.lavender, colors.floralwhite]
    new_table.insert(0, list_table_attributes)
    t = Table(new_table, colWidths=[3*inch]*2, style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                            ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
                                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                            ])
    return t


def data_for_table_16():

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()

    cur.execute('select `parameter`,`parameter_value` '
                'from distance ')

    new_table = cur.fetchall()

    list_table_attributes = ['Parameter', 'Parameter Value']
    new_table = list(new_table)
    color_to_use = [colors.lavender, colors.floralwhite]
    new_table.insert(0, list_table_attributes)
    t = Table(new_table, colWidths=[3*inch]*2, style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                            ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
                                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                            ])
    return t


def data_for_table_17():

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()

    cur.execute('select `parameter`,`parameter_value`,`distance` '
                'from tool_velocity ')

    new_table = cur.fetchall()

    list_table_attributes = ['Parameter', 'Parameter Value']
    new_table = list(new_table)
    color_to_use = [colors.lavender, colors.floralwhite]
    t = Table(new_table, colWidths=[2*inch]*3, style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                            ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                            ('BACKGROUND', (0, 0), (2, 0), colors.grey),
                                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                            ])
    return t


def data_for_table_18():

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()

    cur.execute('select `parameter`,`parameter_value` '
                'from data_summary ')

    new_table = cur.fetchall()

    list_table_attributes = ['Parameter', 'Parameter Value']
    new_table = list(new_table)
    color_to_use = [colors.lavender, colors.floralwhite]
    new_table.insert(0, list_table_attributes)
    t = Table(new_table, colWidths=[3*inch]*2, style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                            ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
                                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                            ])
    return t

