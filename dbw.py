from fnmatch import fnmatch
from doc_test import *
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


global destinationpath, sourcefiles, sourcepath




def data_fetch_from_key(s_name):
    """in this we use our key to use fetch dara from the sql"""
    db = pymysql.connect(host="localhost", user="root", password="root", db="test")
    cur = db.cursor()
    cur.execute('select * from inspection_main where searchName =%s', s_name)

    data = cur.fetchall()

    if len(data) == 0:
        messagebox.showinfo('Error', 'Invalid Code, Please Try Again')
        db.close()

    else:
            welcome_msg = '''Please Wait. Report Generation in progress...'''
            welcome_duration = 800
            top = Toplevel()
            top.geometry('300x100+500+500')
            top.title('Welcome')
            Message(top, text=welcome_msg, padx=20, pady=20).pack()
            top.after(welcome_duration, top.destroy)
            key = data[0][0]

            # cur.execute('select * from inspection_feature_list where runId = %s', key)
            # final_data = cur.fetchall()
            # generate_report(pdf_file_name, final_data, list(data))

            go(data, key, s_name)
            db.close()

            def merger(output_path, input_paths):
                """This function will merge two pdf"""
                pdf_merger = PdfFileMerger()

                for path in input_paths:
                    pdf_merger.merge(9, path)

                with open(output_path, 'wb') as fileobj:
                    pdf_merger.write(fileobj)
                pdf_merger.close()

            paths = glob.glob('*.pdf')
            paths.sort()
            merger(s_name+'.pdf', paths)

            """here we will delete the extra files"""

            for dirpath, dirnames, filenames in os.walk(os.curdir):
                for file in filenames:
                    if fnmatch(file, 'Temp.pdf'):
                        os.remove(os.path.join(dirpath, file))
                    if fnmatch(file, 'Last_Report.pdf'):
                        os.remove(os.path.join(dirpath, file))

            """here we are asking for the destination path and moving pdf to the final location"""

            filename = filedialog.askdirectory()
            sourcepath = 'D:\\Pixel_Panda'
            sourcefiles = os.listdir(sourcepath)
            destinationpath = filename

            for file in sourcefiles:
                if file.endswith('.pdf'):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
                    messagebox._show(title='Completed', message='PDF generated')
