import pymysql
from reportlab.lib.colors import *
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from math import radians, sin, cos
from reportlab.lib.pagesizes import A4, landscape
pymysql.install_as_MySQLdb()


def template(s_name):

    def start(s_name):
        db = pymysql.connect(host="localhost", user="root", password="root", db="test")
        cur = db.cursor()
        cur.execute('select * from inspection_main where searchName =%s', s_name)
        data = cur.fetchall()
        key = data[0][0]
        cur.execute("CREATE TABLE midtable AS SELECT * FROM inspection_feature_list where runId = %s", key)
        db.close()

    def max():
        db = pymysql.connect(host="localhost", user="root", password="root", db="test")
        cur = db.cursor()
        cur.execute("select max(depth) as maximun from midtable")
        maxdepth = cur.fetchone()
        maxdepth = maxdepth[0]

        cur.execute("select max(distance) as maximun from midtable")
        maxdistance = cur.fetchone()
        max_distance = maxdistance[0]

        cur.execute("select `id`,`distance`, `angle`, `clock`, `length`, `Depth` from midtable where depth=%s", maxdepth)
        max_row = cur.fetchall()

        max_row_final = max_row[0]

        id_max = max_row_final[1]

        cur.execute("select `distance`, `joint` from midtable where distance < %s and feature = 'Weld' ", id_max)
        welds_backward = cur.fetchall()
        final_back_welds = welds_backward[-3:]

        cur.execute("select `distance`, `joint` from midtable where distance > %s and feature = 'Weld' ", id_max)
        welds_forward = cur.fetchmany(3)

        cur.execute("delete from midtable where distance = %s", id_max)
        cur.fetchall()

        db.commit()

        db.close()

        return final_back_welds, welds_forward, max_row_final, max_distance

    def hi_fi():

        db = pymysql.connect(host="localhost", user="root", password="root", db="test")
        cur = db.cursor()
        cur.execute('drop table midtable')
        cur.fetchall()
        db.close()

    def hello(c, tup_bef, tup_after, max_row_data, max_distance):

        c.translate(inch, inch)

        c.setStrokeColorRGB(0, 0, 0)
        c.setFillGray(0.8)
        c.ellipse(645, 300, 685, 400, stroke=1, fill=1)

        c.setStrokeColorRGB(0, 0, 0)
        c.setFillGray(0.8)
        c.roundRect(25, 300, 640, 100, 0, stroke=1, fill=1)

        c.setStrokeColorRGB(0, 0, 0)
        c.setFillGray(0.9)
        c.ellipse(5, 300, 45, 400, stroke=1, fill=1)

        c.setLineWidth(3)
        c.setStrokeGray(0.8)
        c.line(665, 300, 665, 400)

        c.setLineWidth(1)
        c.setStrokeColorRGB(0, 0, 0)
        c.line(25, 300, 665, 300)
        c.line(25, 400, 665, 400)

        # c.translate(inch, inch)
        c.setStrokeColorRGB(0, 0, 0)
        c.setFillGray(1)
        c.roundRect(60, 30, 220, 150, 3, stroke=1, fill=1)
        c.line(170, 30, 170, 180)
        c.line(60, 60, 280, 60)
        c.line(60, 90, 280, 90)
        c.line(60, 120, 280, 120)
        c.line(60, 150, 280, 150)

        c.setLineWidth(3)
        c.setFillColor(fidred)
        c.circle(345, 350, 5, stroke=1, fill=1)

        c.setLineWidth(1)
        c.line(105, 300, 105, 400)
        c.line(185, 300, 185, 400)
        c.line(265, 300, 265, 400)
        c.line(425, 300, 425, 400)
        c.line(505, 300, 505, 400)
        c.line(585, 300, 585, 400)

        c.setFillColor(black)
        c.drawCentredString(105, 410, "Weld")
        c.drawCentredString(185, 410, "Weld")
        c.drawCentredString(265, 410, "Weld")
        c.drawCentredString(425, 410, "Weld")
        c.drawCentredString(505, 410, "Weld")
        c.drawCentredString(585, 410, "Weld")

        c.setLineWidth(2)
        c.line(-40, 350, 0, 350)
        c.line(-10, 360, 0, 350)
        c.line(-10, 340, 0, 350)
        c.line(690, 350, 730, 350)
        c.line(720, 360, 730, 350)
        c.line(720, 340, 730, 350)

        c.setLineWidth(2)
        c.line(105, 260, 105, 290)
        c.line(185, 260, 185, 290)
        c.line(265, 260, 265, 290)
        c.line(425, 260, 425, 290)
        c.line(505, 260, 505, 290)
        c.line(585, 260, 585, 290)

        c.setLineWidth(3)
        c.line(325, 420, 345, 440)
        c.line(365, 420, 345, 440)

        c.setFillColor(skyblue)
        c.setLineWidth(1)
        c.circle(505, 100, 60, stroke=1, fill=1)

        degreeAngle = max_row_data[2]
        degreeAngle = int(degreeAngle)
        angle = radians(degreeAngle)
        x = 505 + (60 * sin(angle))
        y = 100 + (60 * cos(angle))
        c.setFillColor(red)
        c.circle(x, y, 5, stroke=1, fill=1)
        c.drawCentredString(505, -5, "Clock is: " + max_row_data[3] + "")

        c.setLineWidth(2)
        c.setDash(array=[4])
        c.setStrokeColor(red)
        c.line(505, 100, x, y)

        c.setDash(array=[4])
        c.setLineWidth(1)
        c.setStrokeColor(black)
        c.line(345, 260, 345, 440)
        c.line(425, 100, 585, 100)
        c.line(505, 30, 505, 180)

        c.setFillColor(black)
        c.setFont('Times-Roman', 17)
        c.drawCentredString(505, 15, "Cross-Sectional View")

        c.setFillColor(darkred)
        c.setFont('Helvetica-Bold', 14)
        c.drawCentredString(355, 450, "Dent(Anomaly)")

        c.setFont('Times-Roman', 14)
        c.setFillColor(black)
        c.drawCentredString(0, 440, "US Valve Distance")
        c.drawCentredString(690, 440, "DS Valve Distance")

        c.setFont('Helvetica-Bold', 14)
        c.drawCentredString(170, 190, "Dent Specification")

        c.setFont('Times-Roman', 14)
        c.drawCentredString(115, 160, "Location ")
        location = str(max_row_data[1])
        c.drawCentredString(225, 160, ""+location+"")

        c.drawCentredString(115, 130, "Size (Depth)")
        depth = str(max_row_data[5])
        c.drawCentredString(225, 130, ""+depth+"")

        c.drawCentredString(115, 100, "Length (mm)")

        lt = max_row_data[4]
        if lt or lt is not None:
            lenth = max_row_data[4]
        else:
            lenth = '0'
        c.drawCentredString(225, 100, ""+lenth+"")

        c.drawCentredString(115, 70, "Width")
        c.drawCentredString(225, 70, "(NULL)")

        c.drawCentredString(115, 40, "Angle (degrees)")
        ang = str(max_row_data[2])
        c.drawCentredString(225, 40, ""+ang+"")

        value_ls_0 = []
        value_joint_0 = []

        if len(tup_bef) > 2:
            for i in range(3):
                a_val = tup_bef[i][0]
                j_val = tup_bef[i][1]
                af_val = str(a_val)
                jf_val = str(j_val)
                value_ls_0.append(af_val)
                value_joint_0.append(jf_val)

        elif len(tup_bef) == 2:
            value_ls_0.append("0")
            value_joint_0.append("0")
            for i in range(2):
                a_val = tup_bef[i][0]
                j_val = tup_bef[i][1]
                af_val = str(a_val)
                jf_val = str(j_val)
                value_ls_0.append(af_val)
                value_joint_0.append(jf_val)

        elif len(tup_bef) == 1:
            for i in range(2):
                value_ls_0.append("0")
                value_joint_0.append("0")
            for i in range(1):
                a_val = tup_bef[i][0]
                j_val = tup_bef[i][1]
                af_val = str(a_val)
                jf_val = str(j_val)
                value_ls_0.append(af_val)
                value_joint_0.append(jf_val)

        else:
            for i in range(3):
                value_ls_0.append("0")
                value_joint_0.append("0")

        c.drawCentredString(70, 310, "(" + value_ls_0[0] + ")m")

        j_data_bf_1 = float(value_ls_0[1]) - float(value_ls_0[0])
        j_data_bf_1 = str(j_data_bf_1)
        c.drawCentredString(145, 310, "(" + j_data_bf_1 + ") m")

        j_data_bf_2 = float(value_ls_0[2]) - float(value_ls_0[1])
        j_data_bf_2 = str(j_data_bf_2)
        c.drawCentredString(225, 310, "(" + j_data_bf_2 + ") m")

        d_data1 = float(max_row_data[1]) - float(value_ls_0[2])
        d_data1 = str(d_data1)
        c.drawCentredString(305, 310, "("+d_data1+") m")

        c.drawCentredString(110, 247, "(" + value_ls_0[0] + ")m")
        c.drawCentredString(190, 247, "(" + value_ls_0[1] + ")m")
        c.drawCentredString(270, 247, "(" + value_ls_0[2] + ")m")

        val = max_row_data[1]
        st_val = str(val)
        c.drawCentredString(350, 247, "(" + st_val + ")m")

        value_ls = []
        value_joint = []
        if len(tup_after) > 2:
            for i in range(3):
                a_val = tup_after[i][0]
                j_val = tup_after[i][1]
                af_val = str(a_val)
                jf_val = str(j_val)
                value_ls.append(af_val)
                value_joint.append(jf_val)

        elif len(tup_after) == 2:
            for i in range(2):
                a_val = tup_after[i][0]
                j_val = tup_after[i][1]
                af_val = str(a_val)
                jf_val = str(j_val)
                value_ls.append(af_val)
                value_joint.append(jf_val)
            value_ls.append("0")
            value_joint.append("0")

        elif len(tup_after) == 1:
            for i in range(1):
                a_val = tup_after[i][0]
                j_val = tup_after[i][1]
                af_val = str(a_val)
                jf_val = str(j_val)
                value_ls.append(af_val)
                value_joint.append(jf_val)

            for i in range(2):
                value_ls.append("0")
                value_joint.append("0")

        else:
            for i in range(3):
                value_ls.append("0")
                value_joint.append("0")

        """ls has value after the dent """
        d_data2 = float(value_ls[0]) - float(max_row_data[1])
        d_data2 = str(d_data2)
        c.drawCentredString(385, 310, "("+d_data2+") m")

        j_data_af_1 = float(value_ls[1]) - float(value_ls[0])
        j_data_af_1 = str(j_data_af_1)
        c.drawCentredString(465, 310, "("+j_data_af_1+") m")

        j_data_af_2 = float(value_ls[2]) - float(value_ls[1])
        j_data_af_2 = str(j_data_af_2)
        c.drawCentredString(545, 310, "(" + j_data_af_2 + ") m")

        c.drawCentredString(430, 247, "(" + value_ls[0] + ")m")
        c.drawCentredString(510, 247, "(" + value_ls[1] + ")m")
        c.drawCentredString(590, 247, "(" + value_ls[2] + ")m")

        # print(max_distance, type(max_distance))

        max_distance_str = str(max_distance)
        c.drawCentredString(625, 310, "(" + max_distance_str + ") m")

        end_value = max_distance - max_row_data[1]
        end_value_str = str(end_value)

        c.drawCentredString(690, 420, "("+end_value_str+") m")

        c.drawCentredString(0, 420, "("+st_val+") m")

        pg = c.getPageNumber()
        pg = pg
        c.drawCentredString(320, -35, "Template %d" % pg)
        c.showPage()

###########################################################################################################

    c = canvas.Canvas("Temp.pdf", pagesize=landscape(A4))

    start(s_name)

    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cursor = db.cursor()
    cursor.execute('select count(feature) from midtable where not depth = 0')
    no_of_dent = cursor.fetchall()
    db.close()
    no_of_dent_int = no_of_dent[0][0]

    if no_of_dent_int >= 10:
        for i in range(10):
            tup_bef, tup_after, max_row_data, max_distance = max()
            hello(c, tup_bef, tup_after, max_row_data, max_distance)

    else:
        for i in range(no_of_dent_int):
            tup_bef, tup_after, max_row_data, max_distance = max()
            hello(c, tup_bef, tup_after, max_row_data, max_distance)

    hi_fi()

    c.save()

