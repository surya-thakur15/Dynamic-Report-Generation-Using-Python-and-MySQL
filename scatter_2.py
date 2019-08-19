
from reportlab.graphics.charts.lineplots import ScatterPlot
from reportlab.graphics.samples.excelcolors import *
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.textlabels import Label
'1906181NMDA'


def scatter_plot(final_dis_angle, xname, yname):
    drawing = Drawing(400, 300)

    chart = ScatterPlot()

    chart.width = 450
    chart.height = 350

    chart.x = 32
    chart.y = 26

    chart.data = [final_dis_angle]

    chart.joinedLines = 0
    chart.fillColor = color03
    chart.lineLabelFormat = None
    chart.lineLabels.fontName = 'Helvetica'

    lab = Label()
    lab.setOrigin(130, 260)

    chart.xValueAxis.avoidBoundFrac = 1
    chart.xValueAxis.visibleGrid = 1
    chart.xValueAxis.tickDown = 2
    chart.xValueAxis.labels.fontName = 'Helvetica'
    chart.xValueAxis.labels.fontSize = 10
    chart.xValueAxis.labelTextFormat = '%d'
    chart.leftPadding = -32

    chart.xLabel = xname
    chart.xValueAxis.forceZero = 1

    chart.yValueAxis.avoidBoundFrac = 1
    chart.yValueAxis.visibleGrid = 1
    chart.yValueAxis.tickLeft = 2
    chart.yValueAxis.labels.fontName = 'Helvetica'
    chart.yValueAxis.labels.fontSize = 10
    chart.yValueAxis.labelTextFormat = '%d'

    chart.yLabel = yname
    chart.yLabel.center(10)
    chart.yValueAxis.forceZero = 0

    # Title = Label()
    # Title.fontName = 'Helvetica-Bold'
    # Title.fontSize = 10
    # Title.x = 100
    # Title.y = 550
    # Title._text = 'This is just a test chart'
    # Title.maxWidth = 20
    # Title.height = 100
    # Title.textAnchor = 'middle'

    # legend = Legend()
    # legend.colorNamePairs = [(color01, 'Widgets'), (color02, 'Sprockets')]
    # legend.fontName = 'Helvetica'
    # legend.fontSize = 8
    # legend.x = 470
    # legend.y = 470
    # legend.dxTextSpace = 4
    # legend.dy = 7
    # legend.dx = 7
    # legend.deltay = 4
    # legend.alignment = 'right'

    drawing.add(chart)
    return drawing


def scatter_plot_2(final_dis_clock, xname, yname):
    drawing = Drawing(400, 300)

    chart = ScatterPlot()

    chart.width = 450
    chart.height = 350

    chart.x = 32
    chart.y = 26

    chart.data = [final_dis_clock]

    chart.joinedLines = 0
    chart.fillColor = color03
    chart.lineLabelFormat = None
    chart.lineLabels.fontName = 'Helvetica'

    lab = Label()
    lab.setOrigin(130, 260)

    chart.xValueAxis.avoidBoundFrac = 1
    chart.xValueAxis.visibleGrid = 1
    chart.xValueAxis.tickDown = 2
    chart.xValueAxis.labels.fontName = 'Helvetica'
    chart.xValueAxis.labels.fontSize = 10
    chart.xValueAxis.labelTextFormat = '%d'
    chart.leftPadding = -32

    chart.xLabel = xname
    chart.xValueAxis.forceZero = 1

    chart.yValueAxis.avoidBoundFrac = 1
    chart.yValueAxis.visibleGrid = 1
    chart.yValueAxis.tickLeft = 2
    chart.yValueAxis.labels.fontName = 'Helvetica'
    chart.yValueAxis.labels.fontSize = 10
    chart.yValueAxis.labelTextFormat = '%s'

    chart.yValueAxis.valueMin = 0.0
    chart.yValueAxis.valueStep = 3.0
    chart.yValueAxis.valueMax = 9.0

    chart.yLabel = yname
    chart.yLabel.center(10)
    chart.yValueAxis.forceZero = 0

    # Title = Label()
    # Title.fontName = 'Helvetica-Bold'
    # Title.fontSize = 10
    # Title.x = 100
    # Title.y = 550
    # Title._text = 'This is just a test chart'
    # Title.maxWidth = 20
    # Title.height = 100
    # Title.textAnchor = 'middle'

    # legend = Legend()
    # legend.colorNamePairs = [(color01, 'Widgets'), (color02, 'Sprockets')]
    # legend.fontName = 'Helvetica'
    # legend.fontSize = 8
    # legend.x = 470
    # legend.y = 470
    # legend.dxTextSpace = 4
    # legend.dy = 7
    # legend.dx = 7
    # legend.deltay = 4
    # legend.alignment = 'right'

    drawing.add(chart)
    return drawing

def scatter_plot_3(final_dis_clock, xname, yname):
    drawing = Drawing(400, 300)

    chart = ScatterPlot()

    chart.width = 450
    chart.height = 350

    chart.x = 32
    chart.y = 26

    chart.data = [final_dis_clock]

    chart.joinedLines = 0
    chart.fillColor = color03
    chart.lineLabelFormat = None
    chart.lineLabels.fontName = 'Helvetica'

    lab = Label()
    lab.setOrigin(130, 260)

    chart.xValueAxis.avoidBoundFrac = 1
    chart.xValueAxis.visibleGrid = 1
    chart.xValueAxis.tickDown = 2
    chart.xValueAxis.labels.fontName = 'Helvetica'
    chart.xValueAxis.labels.fontSize = 10
    chart.xValueAxis.labelTextFormat = '%d'
    chart.leftPadding = -32

    chart.xLabel = xname
    chart.xValueAxis.forceZero = 1

    chart.yValueAxis.avoidBoundFrac = 1
    chart.yValueAxis.visibleGrid = 1
    chart.yValueAxis.tickLeft = 2
    chart.yValueAxis.labels.fontName = 'Helvetica'
    chart.yValueAxis.labels.fontSize = 10
    chart.yValueAxis.labelTextFormat = '%d'

    chart.yValueAxis.valueMin = 0
    chart.yValueAxis.valueStep = 60
    chart.yValueAxis.valueMax = 300

    chart.yLabel = yname
    chart.yLabel.center(10)
    chart.yValueAxis.forceZero = 0

    # Title = Label()
    # Title.fontName = 'Helvetica-Bold'
    # Title.fontSize = 10
    # Title.x = 100
    # Title.y = 550
    # Title._text = 'This is just a test chart'
    # Title.maxWidth = 20
    # Title.height = 100
    # Title.textAnchor = 'middle'

    # legend = Legend()
    # legend.colorNamePairs = [(color01, 'Widgets'), (color02, 'Sprockets')]
    # legend.fontName = 'Helvetica'
    # legend.fontSize = 8
    # legend.x = 470
    # legend.y = 470
    # legend.dxTextSpace = 4
    # legend.dy = 7
    # legend.dx = 7
    # legend.deltay = 4
    # legend.alignment = 'right'

    drawing.add(chart)
    return drawing


