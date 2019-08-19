# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import *
# from reportlab.platypus import Image
# from datetime import datetime
#
#
# def generate_report(pdf_file_name, final_data, data):
#     """this function will generate the pdf page"""
#     # print("data is getting pass correctly\n")   # checking for the data pass
#     # start_time = datetime.now()
#
#     c = canvas.Canvas(pdf_file_name, pagesize=portrait(A4))
#     c.setFont('Times-Bold', 30, leading=None)
#     c.drawCentredString(300, 735, "PIPELINE INSPECTION REPORT")
#
#     c.setFont('Times-Bold', 20, leading=None)
#     c.drawString(175, 670, " ")
#
#     head_logo = 'head_logo.png'
#     c.drawImage(head_logo, 100, 647, width=61, height=61)
#     #
#     tool_logo = 'tool.jpeg'
#
#     c.drawImage(tool_logo, 143, 345, width=300, height=300)
#     data_merge= data[0][5] +"-"+ data[0][6]
#
#     c.drawString(150,300,data_merge)
#
#
#     c.setFont('Times-Roman', 20, leading=None)
#     c.drawString(72, 255, "Report Code")
#     c.setFont('Times-Roman', 24, leading=None)
#
#     c.drawString(72,225,data[0][1])
#
#     c.setFont('Times-Roman', 20, leading=None)
#     c.drawString(72, 175, "Client Name")
#     c.setFont('Times-Roman', 24, leading=None)
#     c.drawString(72,145,data[0][3])
#
#     c.setFont('Times-Roman', 20, leading=None)
#     c.drawString(72, 95, "Project Name")
#
#     c.setFont('Times-Roman', 24, leading=None)
#     proj_name_merged= data[0][2] +"-" + data[0][9]
#     c.drawString(72,65,proj_name_merged)
#     c.showPage()
#
#     c.drawString(72, 760, 'Client Name')
#     c.save()
#
#     # move_dir_function()
#
#     # tool_logo = 'side.jpg'
#     # c.drawImage(tool_logo, 580, 842, width=15, height=842)
#
#     # for i in len(data):
#     #     if emx % 400 == 0:
#     #         c.showPage()
#     #     c.drawString(25, emx, "{}".format(data[0:5]))
#     #     emx -= 50
#     #     print("\n")
#     # c.drawString(50, 700, "{}".format(data[4:11]))
#     # print("date from the list is here \n", data[7])
#
#     # c.showPage()
#     # dist = 700
#     # for row in final_data:
#     #     if dist % 400 == 0:
#     #         c.showPage()
#     #         dist = 700
#     #     c.drawCentredString(300, dist, "{}".format(row[0:11]))
#     #     print("\n")
#     #     dist -= 50
#
#     # c.showPage()
#     # c.setFont('Helvetica', 24, leading=None)
#     # c.drawCentredString(300, 650, "total rows of the matched data {}".format(len(final_data)))
#     # seal = 'jpg.jpg'
#     # c.drawImage(seal, 82, 200, width=400, height=400)
#     # c.showPage()
#     # """here we'll call the function for the plotting"""
#     # c.save()
#     # # time_taken = datetime.now() - start_time
#     # # print(time_taken)
