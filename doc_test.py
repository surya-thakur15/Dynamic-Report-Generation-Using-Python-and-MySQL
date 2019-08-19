import glob
import pymysql
from datetime import date
from functools import partial
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from line_plot import line_plot
from scatter_2 import scatter_plot
from test import *
from template_data_fetch import *
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import portrait, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageTemplate, Frame, KeepTogether, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from table_formatting import *
from pytyyh import *

'1906184NMDA'

PAGE_HEIGHT = 835
PAGE_WIDTH = 495
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
styleH2 = styles['Heading2']
styleH.alignment = TA_CENTER
style_right = ParagraphStyle(name='right', parent=styles['Normal'], alignment=TA_JUSTIFY)
Elements = []


def myFirstPage(c, doc, content):
    """function to maintain template of first page"""
    c.saveState()

    data = content
    # c.setFillColorRGB(1, 1, 1)
    c.setFont('Times-Bold', 33, leading=None)
    c.drawCentredString(300, 735, "FINAL INSPECTION REPORT")

    c.setFont('Times-Bold', 23, leading=None)
    c.drawString(135, 670, "Transpipe Integrity Solutions Pvt Ltd")

    head_logo = 'D:\\Pixel_Panda\\Images\\head_logo.png'
    c.drawImage(head_logo, 60, 645, width=71, height=71)

    tool_logo = 'tool.jpeg'  # pic of tool
    c.drawImage(tool_logo, 143, 345, width=300, height=300)

    # c.setFillColorRGB(1, 1, 1)

    data_merge = data[0][5] + "-" + data[0][6]
    c.drawCentredString(295, 300, data_merge)

    c.setFont('Times-Roman', 18, leading=None)
    c.drawRightString(8 * inch, 230, "Report Code")
    c.setFont('Times-Roman', 19, leading=None)
    c.drawRightString(8 * inch, 200, data[0][1])

    c.setFont('Times-Roman', 18, leading=None)
    c.drawRightString(8 * inch, 155, "Client Name")
    c.setFont('Times-Roman', 19, leading=None)
    c.drawRightString(8 * inch, 125, data[0][3])

    c.setFont('Times-Roman', 18, leading=None)
    c.drawRightString(8 * inch, 80, "Project Name")

    c.setFont('Times-Roman', 19, leading=None)
    proj_name_merged = data[0][2] + "-" + data[0][9]
    c.drawRightString(8 * inch, 50, proj_name_merged)

    c.showPage()   # Page break for the first page

    # c.setFillColorRGB(1, 1, 1)
    c.setFont('Times-Roman', 18, leading=None)
    c.drawString(72, 710, 'Client Name       :')
    c.drawString(250, 710, data[0][3])
    c.drawString(72, 685, 'Project name      :')
    c.drawString(250, 685, data[0][2])
    c.drawString(72, 660, 'Location             :')
    c.drawString(250, 660, data[0][4])
    c.drawString(72, 635, 'Inspection date   :')
    c.drawString(250, 635, str(data[0][7]))
    now = date.today()
    c.drawString(72, 610, 'Publication date :')
    c.drawString(250, 610, str(now))
    c.setFont('Times-Bold', 18, leading=None)

    c.setFont('Times-Roman', 18, leading=None)

    c.drawString(72, 535, 'Prepared By   :                      ________________')
    c.drawString(72, 485, 'Checked By   :                      ________________')
    c.drawString(72, 435, 'Approved By :                      ________________')
    c.setFont('Times-Bold', 18, leading=None)
    c.drawString(72, 350, ' ')
    c.setFont('Times-Roman', 16, leading=None)
    c.drawString(72, 325, ' ')
    c.drawString(72, 300, ' ')

    c.setFont('Times-Bold', 13, leading=None)
    c.drawString(72, 142, ' ')
    c.drawString(72, 122, ' ')
    # c.restoreState()
    c.showPage()    # Page break for the second page

    c.setFont('Times-Roman', 10)
    head_logo = 'D:\\Pixel_Panda\\Images\\head_logo.png'
    c.drawImage(head_logo, 1 * inch, 10.75 * inch, width=50, height=50)
    c.drawString(5.265 * inch, 10.8 * inch, " ")
    c.drawString(inch, 0.65 * inch, " ")
    pg = doc.page + 2
    c.drawString(6.92 * inch, 0.65 * inch, "Page %d" % pg)
    c.line(1 * inch, 10.69 * inch, 7.30 * inch, 10.69 * inch)
    c.line(1 * inch, 0.8 * inch, 7.30 * inch, 0.8 * inch)


def myLaterPages(canvas, doc):
    """this function will data on later pages"""
    canvas.saveState()
    canvas.setFont('Times-Roman', 10)
    head_logo = 'D:\\Pixel_Panda\\Images\\head_logo.png'
    canvas.drawImage(head_logo, 1 * inch, 10.75 * inch, width=50, height=50)
    canvas.drawString(5.265 * inch, 10.8 * inch, " ")
    canvas.drawString(inch, 0.65 * inch, " ")
    pg = doc.page + 2
    canvas.drawString(6.92 * inch, 0.65 * inch, "Page %d" % pg)
    canvas.line(1 * inch, 10.69 * inch, 7.30 * inch, 10.69 * inch)
    canvas.line(1 * inch, 0.8 * inch, 7.30 * inch, 0.8 * inch)
    canvas.restoreState()


def go(data, key, s_name):
    """this function will have whole template of report"""
    doc = SimpleDocTemplate('Last_Report.pdf')

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()
    cur.execute('select `distance`, `joint` from inspection_feature_list where runId = %s', key)
    graph_data1 = cur.fetchall()
    # print("data for dis, joint and depth: \n")
    # print(graph_data1)

    cur.execute('select `distance`, `angle`, `clock`, `depth` from inspection_feature_list '
                'where runId = %s and feature = "Dent"', key)

    graph_data2 = cur.fetchall()

    final_dis_depth = []
    ls = []
    for i in graph_data2:
        val1 = int(i[0])
        ls.append(val1)
        val2 = i[3]
        if val2 == 'None' or val2 == NONE:
            ls.append(0)
        else:
            val2 = int(val2)
            ls.append(val2)
        final_dis_depth.append(ls)
        ls = []

    final_dis_angle = []
    ls = []
    for i in graph_data2:
        val1 = int(i[0])
        val2 = int(i[1])
        ls.append(val1)
        ls.append(val2)
        final_dis_angle.append(ls)
        ls = []

    final_dis_clock = []
    ls2 = []
    for i in graph_data2:
        val1 = i[0]
        val2 = i[2]
        ls2.append(val1)
        ls = val2.split(":")
        b = int(ls[1])
        b = int(b * (5/3))
        b = str(b)
        ans = ls[0] + "." + b
        fin_ans = float(ans)
        ls2.append(fin_ans)
        final_dis_clock.append(ls2)
        ls2 = []

    cur.execute('select `feature` from inspection_feature_list '
                'where runId = %s', key)
    pie_data = cur.fetchall()
    pi_list = []
    for i in pie_data:
        pi_list.append(i[0])

    """here is table of content"""
    Elements.append(Spacer(0, 0.1 * inch))
    heading2_22 = "TABLE OF CONTENTS"
    p_222 = Paragraph(heading2_22, styleH)
    Elements.append(p_222)
    Elements.append(Spacer(0, 0.02 * inch))

    list_info = [['Serial No.', 'Title', 'Page No'],
                 ['01', 'Executive Summary', '04'],
                 ['02', 'Feature Distribution Chart', '06'],
                 ['03', 'Dent Depth Graph', '07'],
                 ['04', 'Dent Clock Orientation Graph', '08'],
                 ['05', 'Dent Angle Orientation Graph', '09'],
                 # ['06', 'Dent Marked Templates', ' '],
                 ['06', 'Speed Graphs', '10'],
                 ['07', 'Parameter Definition', '11'],
                 ['08', 'Full Registry Table', '12'],
                 ['09', 'Disclaimer', '15']
                 ]

    color_to_use = [colors.lavender, colors.floralwhite]
    t = Table(list_info, colWidths=[1 * inch, 4 * inch, 1 * inch], style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black),
                                                          ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                                          ('BACKGROUND', (0, 0), (2, 0), colors.grey)
                                                          ])
    Elements.append(t)
    Elements.append(PageBreak())

    Elements.append(Spacer(0, 0.1 * inch))
    heading2_22 = "EXECUTIVE SUMMARY"
    p_222 = Paragraph(heading2_22, styleH)
    Elements.append(p_222)
    # Elements.append(Spacer(0, 0.1 * inch))
    heading2_2 = "TOOL INFORMATION"
    Elements.append(Spacer(0, 0.1 * inch))
    p_22 = Paragraph(heading2_2, styleH2)
    t_1 = data_for_tool()
    ls = [p_22, t_1]
    tab = KeepTogether(ls)
    Elements.append(tab)

    # Elements.append(PageBreak())
    Elements.append(Spacer(0, 0.1 * inch))
    heading2_3 = "RUN SUMMARY"
    Elements.append(Spacer(0, 0.20 * inch))
    p_23 = Paragraph(heading2_3, styleH2)
    t_23 = data_for_table_1()
    ls_23 = [p_23, t_23]
    tab_23 = KeepTogether(ls_23)
    Elements.append(tab_23)

    Elements.append(PageBreak())
    Elements.append(Spacer(0, 0.1 * inch))
    heading1_4 = "Primary Sensor Performance"
    Elements.append(Spacer(0, 0.1 * inch))
    p_14 = Paragraph(heading1_4, styleH2)
    t_14 = data_for_table_14()
    ls14 = [p_14, t_14]
    tab14 = KeepTogether(ls14)
    Elements.append(tab14)

    Elements.append(Spacer(0, 0.1 * inch))
    heading1_5 = "Inertial Sensor Performance"
    Elements.append(Spacer(0, 0.20 * inch))
    p_15 = Paragraph(heading1_5, styleH2)
    t_15 = data_for_table_15()
    ls_15 = [p_15, t_15]
    tab_15 = KeepTogether(ls_15)
    Elements.append(tab_15)

    Elements.append(Spacer(0, 0.1 * inch))
    heading1_6 = "Distance"
    Elements.append(Spacer(0, 0.20 * inch))
    p_16 = Paragraph(heading1_6, styleH2)
    t_16 = data_for_table_16()
    ls_16 = [p_16, t_16]
    tab_16 = KeepTogether(ls_16)
    Elements.append(tab_16)

    Elements.append(Spacer(0, 0.1 * inch))
    heading1_7 = "Tool Velocity"
    Elements.append(Spacer(0, 0.20 * inch))
    p_17 = Paragraph(heading1_7, styleH2)
    t_17 = data_for_table_17()
    ls_17 = [p_17, t_17]
    tab_17 = KeepTogether(ls_17)
    Elements.append(tab_17)

    Elements.append(Spacer(0, 0.1 * inch))
    heading1_8 = "Data Non-Conformance Summary"
    Elements.append(Spacer(0, 0.20 * inch))
    p_18 = Paragraph(heading1_8, styleH2)
    t_18 = data_for_table_18()
    ls_18 = [p_18, t_18]
    tab_18 = KeepTogether(ls_18)
    Elements.append(tab_18)

    heading2 = "Feature Distribution"
    p = Paragraph(heading2, styleH)
    Elements.append(Spacer(0, 1.4 * inch))
    Elements.append(p)
    chart_test = pie_test(pi_list)
    Elements.append(Spacer(0, 1.2 * inch))
    Elements.append(chart_test)
    Elements.append(PageBreak())

    """scatter graph is here"""

    heading2 = "Dent Depth vs Distance"
    p = Paragraph(heading2, styleH)
    Elements.append(Spacer(0, 1.4 * inch))
    Elements.append(p)
    scatter_chart = scatter_plot(final_dis_depth, 'Distance ->', 'Dent Depth ->')
    Elements.append(Spacer(0, 1.35 * inch))
    Elements.append(scatter_chart)
    Elements.append(PageBreak())

    heading2 = "Dent Clock Orientation vs Distance"
    p = Paragraph(heading2, styleH)
    Elements.append(Spacer(0, 1.4 * inch))
    Elements.append(p)
    scatter_chart = scatter_plot_2(final_dis_clock, 'Distance ->', "Dent Clock Orientation->")
    Elements.append(Spacer(0, 1.35 * inch))
    Elements.append(scatter_chart)
    Elements.append(PageBreak())

    heading2 = "Dent Angle Orientation vs Distance"
    p = Paragraph(heading2, styleH)
    Elements.append(Spacer(0, 1.4 * inch))
    Elements.append(p)
    scatter_chart = scatter_plot_3(final_dis_angle, 'Distance ->', 'Dent Angle Orientation ->')
    Elements.append(Spacer(0, 1.35 * inch))
    Elements.append(scatter_chart)

    list_im = []
    paths = glob.glob('D:\\speedGraph\\*.jpg')
    paths.sort()
    for i in paths:
        im = Image(i, 6.4 * inch, 4.4 * inch)
        list_im.append(im)

    keep_ls = KeepTogether(list_im)
    Elements.append(keep_ls)

    """here is table below:"""

    list_info = [['Parameter', 'Unit'],
                 ['ID', 'Each feature is provided with a unique ID to assist the user of the software.'],
                 ['Distance', 'It is the distance measured by tool odometers from the Launcher.'],
                 ['Feature', 'It is the category of detected feature i.e. Valve, Weld, Tee, Dent, Flange etc.'],
                 ['Joint', 'It is the distance between two consecutive welds.'],
                 ['Length', 'It is the axial length of the specified feature.'],
                 ['Width', 'It is the circumferential length of the specified feature.'],
                 ['Depth', 'It is the maximum deformation recorded by tool.'],
                 ['Angle', 'It is the angle orientation of that defect in downstream direction.'],
                 ["O' clock", 'It is the O Clock orientation of that defect in downstream direction.'],
                 ['Remarks', 'Additional notes related to the particular feature.']]

    color_to_use = [colors.lavender, colors.floralwhite]
    t = Table(list_info, colWidths=[1 * inch, 5 * inch], style=[('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black,),
                                                          ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                                                          ('BACKGROUND', (0, 0), (1, 0), colors.grey),
                                                          ('ROWBACKGROUNDS', (0, 1), (-1, -1), color_to_use),
                                                          ])
    Elements.append(Spacer(0, 0.45 * inch))
    heading43 = "Parameter Definition"
    p43 = Paragraph(heading43, styleH)
    ls43 = [p43, t]
    tab43 = KeepTogether(ls43)

    Elements.append(tab43)

    heading2 = "Full Registry Listing"
    p = Paragraph(heading2, styleH)
    t = data_for_table(key)
    ls = [p, t]
    tab = KeepTogether(ls)
    Elements.append(tab)
    Elements.append(PageBreak())

    Elements.append(Spacer(0, 0.1 * inch))
    heading_1 = 'DISCLAIMER'
    p1 = Paragraph(heading_1, styleH)
    Elements.append(p1)
    Elements.append(Spacer(0, 0.1 * inch))

    heading_2 = """ ...................................................................................................
     .......................................................................................
     ...............................................................................
     ........................................................................................
     ................................................................................"""

    p_2 = Paragraph(heading_2, style_right)
    Elements.append(p_2)

    Elements.append(Spacer(0, 0.3 * inch))
    heading_3 = """ ...................................................................................................
     .......................................................................................
     ...............................................................................
     ........................................................................................
     ................................................................................"""
    p_3 = Paragraph(heading_3, style_right)
    Elements.append(p_3)

    Elements.append(PageBreak())

    thk = Image('D:\\Pixel_Panda\\Images\\thank.png', 7.2 * inch, 5 * inch)
    Elements.append(Spacer(0, 2.5 * inch))
    Elements.append(thk)

    template(s_name)

    doc.build(Elements, onFirstPage=partial(myFirstPage, content=data), onLaterPages=myLaterPages)

    print("\nThank you !!")




