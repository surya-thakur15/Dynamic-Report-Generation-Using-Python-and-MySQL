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


def data_for_tool():
    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()
    cur.execute('select `parameter`,`parameter_value` '
                'from new_toolinsp')

    tool_info = cur.fetchall()
    tool_attributes = ['Parameter', 'Parameter Value']

    tool_info = list(tool_info)
    color_to_use = [colors.lavender, colors.floralwhite]
    tool_info.insert(0, tool_attributes)
    t = Table(tool_info, colWidths=[3*inch]*2, style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                            ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
                                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                            ])
    return t