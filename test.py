from reportlab.graphics.charts.piecharts import Pie
from line_plot import *
from scatter_2 import *


def pie_test(pi_list):
    """this function will has pie chart"""
    d = Drawing()
    pc = Pie()
    cnt_Bend = pi_list.count('Bend')
    cnt_Weld = pi_list.count('Weld')
    cnt_Dent = pi_list.count('Dent')
    cnt_Tee = pi_list.count('Tee')
    cnt_Flange = pi_list.count('Flange')
    total = cnt_Bend + cnt_Dent + cnt_Flange + cnt_Tee + cnt_Weld

    p_Bend = (cnt_Bend / total) * 100
    p_Dent = (cnt_Dent / total) * 100
    p_Flange = (cnt_Flange / total) * 100
    p_Tee = (cnt_Tee / total) * 100
    p_Weld = (cnt_Weld / total) * 100

    rp_Bend = str(round(p_Bend, 2))
    rp_Dent = str(round(p_Dent, 2))
    rp_Flange = str(round(p_Flange, 2))
    rp_Tee = str(round(p_Tee, 2))
    rp_Weld = str(round(p_Weld, 2))

    # print(rp_Bend, rp_Dent, rp_Flange, rp_Tee, rp_Weld)

    pc.data = [cnt_Bend, cnt_Weld, cnt_Flange, cnt_Tee, cnt_Dent]
    pc.labels = ['BEND (' + rp_Bend + '% )', 'WELD (' + rp_Weld + '% )', 'FLANGE (' + rp_Flange + '% )',
                 'TEE (' + rp_Tee + '% )', 'DENT (' + rp_Dent + '% )']

    pc.x = 90
    pc.y = -50

    pc.width = 300
    pc.height = 300
    pc.startAngle = 0

    pc.sideLabels = 1

    pc.slices.strokeWidth = 0.5
    pc.slices[0].popout = 10
    pc.slices[1].popout = 10
    pc.slices[2].popout = 10
    pc.slices[3].popout = 10

    pc.slices[4].popout = 10
    pc.slices[4].strokeWidth = 2
    pc.slices[4].strokeDashArray = [2, 2]
    pc.slices[4].labelRadius = 1.20
    pc.slices[4].fontColor = colors.red
    d.add(pc)

    return d
