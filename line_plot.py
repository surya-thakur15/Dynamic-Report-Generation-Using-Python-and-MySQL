
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors
from reportlab.lib.units import inch


def line_plot(final_dis_angle):

    drawing = Drawing()
    data = [final_dis_angle]
    lp = LinePlot()
    lp.x = 0
    lp.y = -120
    lp.height = 300
    lp.width = 450
    lp.data = data
    lp.joinedLines = 0
    lp.lines[0].symbol = makeMarker('FilledCircle')
    lp.lines[1].symbol = makeMarker('Circle')
    lp.lineLabelFormat = '%2.0f'
    lp.strokeColor = colors.black
    # lp.xValueAxis.valueMin = 0
    # lp.xValueAxis.valueMax = 5
    # lp.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5]
    lp.xValueAxis.labelTextFormat = '%2.1f'
    # lp.yValueAxis.valueMin = 0
    # lp.yValueAxis.valueMax = 7
    # lp.yValueAxis.valueSteps = [1, 2, 3, 5, 6]
    drawing.add(lp)

    return drawing



