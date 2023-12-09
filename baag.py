
# from tkinter import *
# from tkinter import ttk
# import mysql.connector
# from tkinter import messagebox
# import datetime


# class LibraryManagementSystem:

#     def __init__(self, root):
#         self.root = root
#         self.root.title('Library Management System')
#         self.root.geometry('1550x800+0+0')

#         # -----------------------variable----------------------------

#         self.member_var = StringVar()
#         self.prn_var = StringVar()
#         self.title_var = StringVar()
#         self.firstname_var = StringVar()
#         self.lastname_var = StringVar()
#         self.address1_var = StringVar()
#         self.address2_var = StringVar()
#         self.postid_var = StringVar()
#         self.mobile_var = StringVar()
#         self.bookid_var = StringVar()
#         self.booktitle_var = StringVar()
#         self.auther_var = StringVar()
#         self.dateborrowed_var = StringVar()
#         self.datedue_var = StringVar()
#         self.days_var = StringVar()
#         self.latereturnfine_var = StringVar()
#         self.dateoverdue_var = StringVar()
#         self.finalprice_var = StringVar()

#         lbltitle = Label(
#             self.root,
#             text='Library Management System',
#             bg='powder blue',
#             fg='green',
#             bd=20,
#             relief=RIDGE,
#             font=('times new roman', 50, 'bold'),
#             padx=2,
#             pady=6,
#             )
#         lbltitle.pack(side=TOP, fill=X)

#         frame = Frame(self.root, bd=12, relief=RIDGE, padx=20,
#                     bg='powder blue')
#         frame.place(x=0, y=130, width=1530, height=400)

#         # -------------------------DataFrameLeft-------------

#         DataFrameLeft = LabelFrame(
#             frame,
#             text='Library Membership Information',
#             bg='powder blue',
#             fg='green',
#             bd=12,
#             relief=RIDGE,
#             font=('times new roman', 12, 'bold'),
#             )
#         DataFrameLeft.place(x=0, y=5, width=900, height=350)

#         lblMember = Label(
#             DataFrameLeft,
#             text='Member Type',
#             bg='powder blue',
#             font=('times new roman', 12, 'bold'),
#             padx=2,
#             pady=6,
#             )
#         lblMember.grid(row=0, column=0, sticky=W)

#         comMember = ttk.Combobox(DataFrameLeft, font=('times new roman'
#                                 , 12, 'bold'), width=29,
#                                 state='readonly',
#                                 textvariable=self.member_var)
#         comMember['values'] = ('Admin Staff', 'Student', 'Lecturer')
#         comMember.grid(row=0, column=1, sticky=W)

#         lblPRN_No = Label(
#             DataFrameLeft,
#             text='PRN No',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             padx=2,
#             pady=6,
#             )
#         lblPRN_No.grid(row=1, column=0, sticky=W)
#         txtPRN_NO = Entry(DataFrameLeft, textvariable=self.prn_var,
#                         font=('arial', 13, 'bold'), width=29)
#         txtPRN_NO.grid(row=1, column=1)  # Move padx and pady to here

#         # Id No

#         lblTitle = Label(
#             DataFrameLeft,
#             text='Id No',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             padx=2,
#             pady=6,
#             )
#         lblTitle.grid(row=2, column=0, sticky=W)

#         txtTitle = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                         width=29, textvariable=self.title_var)
#         txtTitle.grid(row=2, column=1)

#         # First Name

#         lblFirstName = Label(
#             DataFrameLeft,
#             text='First Name',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             textvariable=self.firstname_var,
#             padx=2,
#             )
#         lblFirstName.grid(row=3, column=0, sticky=W)

#         txtFirstName = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                             width=29, textvariable=self.firstname_var)
#         txtFirstName.grid(row=3, column=1)

#         # Last Name

#         lblLastName = Label(
#             DataFrameLeft,
#             text='Last Name',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             padx=2,
#             pady=6,
#             )
#         lblLastName.grid(row=4, column=0, sticky=W)

#         txtLastName = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                             textvariable=self.lastname_var, width=29)
#         txtLastName.grid(row=4, column=1)

#         # Address1

#         lblAddress1 = Label(DataFrameLeft, text='Address1',
#                             bg='powder blue', font=('arial', 12, 'bold'
#                             ), padx=2)
#         lblAddress1.grid(row=5, column=0, sticky=W)

#         txtAddress1 = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                             width=29, textvariable=self.address1_var)
#         txtAddress1.grid(row=5, column=1)

#         # Address2

#         lblAddress2 = Label(
#             DataFrameLeft,
#             text='Address2',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             textvariable=self.address2_var,
#             padx=2,
#             pady=6,
#             )
#         lblAddress2.grid(row=6, column=0, sticky=W)

#         txtAddress2 = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                             width=29)
#         txtAddress2.grid(row=6, column=1)

#         # Post Code

#         lblPostCode = Label(
#             DataFrameLeft,
#             text='Post Code',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             textvariable=self.postid_var,
#             padx=2,
#             )
#         lblPostCode.grid(row=7, column=0, sticky=W)

#         txtPostCode = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                             width=29)
#         txtPostCode.grid(row=7, column=1)

#         # Mobile Number

#         lblMobileNumber = Label(
#             DataFrameLeft,
#             text='Mobile Number',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             padx=2,
#             pady=6,
#             )
#         lblMobileNumber.grid(row=8, column=0, sticky=W)

#         txtMobileNumber = Entry(DataFrameLeft, font=('arial', 13, 'bold'
#                                 ), textvariable=self.mobile_var,
#                                 width=29)
#         txtMobileNumber.grid(row=8, column=1)

#         # Book ID

#         lblBookID = Label(DataFrameLeft, text='Book ID', bg='powderblue'
#                         , font=('arial', 12, 'bold'), padx=2)
#         lblBookID.grid(row=0, column=2, sticky=W)

#         txtBookID = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                         textvariable=self.bookid_var, width=29)
#         txtBookID.grid(row=0, column=3)

#         # Book Title

#         lblBookTitle = Label(
#             DataFrameLeft,
#             text='Book Title',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             padx=2,
#             pady=4,
#             )
#         lblBookTitle.grid(row=1, column=2, sticky=W)

#         txtBookTitle = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                             textvariable=self.booktitle_var, width=29)
#         txtBookTitle.grid(row=1, column=3)

#         # Author Name

#         lblAuthorName = Label(DataFrameLeft, text='Author Name',
#                             bg='powder blue', font=('arial', 12,
#                             'bold'), padx=2)
#         lblAuthorName.grid(row=2, column=2, sticky=W)

#         txtAuthorName = Entry(DataFrameLeft, font=('arial', 13, 'bold'
#                             ), textvariable=self.auther_var, width=29)
#         txtAuthorName.grid(row=2, column=3)

#         # Date Borrowed

#         lblDateBorrowed = Label(
#             DataFrameLeft,
#             text='DateBorrowed',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             padx=2,
#             pady=4,
#             )
#         lblDateBorrowed.grid(row=3, column=2, sticky=W)

#         txtDateBorrowed = Entry(DataFrameLeft, font=('arial', 13, 'bold'
#                                 ), textvariable=self.dateborrowed_var,
#                                 width=29)
#         txtDateBorrowed.grid(row=3, column=3)

#         # Due Date

#         lblDueDate = Label(DataFrameLeft, text='Due Date',
#                         bg='powder blue', font=('arial', 12, 'bold'
#                         ), padx=2)
#         lblDueDate.grid(row=4, column=2, sticky=W)

#         txtDueDate = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
#                         textvariable=self.datedue_var, width=29)
#         txtDueDate.grid(row=4, column=3)

#         # Days On Book

#         lblDaysOnBook = Label(
#             DataFrameLeft,
#             text='Days On Book',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             padx=2,
#             pady=4,
#             )
#         lblDaysOnBook.grid(row=5, column=2, sticky=W)

#         txtDaysOnBook = Entry(DataFrameLeft, font=('arial', 13, 'bold'
#                             ), textvariable=self.days_var, width=29)
#         txtDaysOnBook.grid(row=5, column=3)

#         # Last Return Date

#         lblLastReturnDate = Label(DataFrameLeft, text='Last Return Date'
#                                 , bg='powder blue', font=('arial',
#                                 12, 'bold'), padx=2)
#         lblLastReturnDate.grid(row=6, column=2, sticky=W)

#         txtLastReturnDate = Entry(DataFrameLeft, font=('arial', 13,
#                                 'bold'),
#                                 textvariable=self.latereturnfine_var,
#                                 width=29)
#         txtLastReturnDate.grid(row=6, column=3)

#         # Date Overdue

#         lblDateOverdue = Label(
#             DataFrameLeft,
#             text='Date Overdue',
#             bg='powder blue',
#             font=('arial', 12, 'bold'),
#             padx=2,
#             pady=4,
#             )
#         lblDateOverdue.grid(row=7, column=2, sticky=W)

#         txtDateOverdue = Entry(DataFrameLeft, font=('arial', 13, 'bold'
#                             ), textvariable=self.dateoverdue_var,
#                             width=29)
#         txtDateOverdue.grid(row=7, column=3)

#         # Actual Price

#         lblActualPrice = Label(DataFrameLeft, text='Actual Price',
#                             bg='powder blue', font=('arial', 12,
#                             'bold'), padx=2)
#         lblActualPrice.grid(row=8, column=2, sticky=W)

#         txtActualPrice = Entry(DataFrameLeft, font=('arial', 13, 'bold'
#                             ), textvariable=self.finalprice_var,
#                             width=29)
#         txtActualPrice.grid(row=8, column=3)

#         # -------------------------DataFrameRight-------------

#         DataFrameRight = LabelFrame(
#             frame,
#             text='Book Details',
#             bg='powder blue',
#             fg='green',
#             bd=12,
#             relief=RIDGE,
#             font=('times new roman', 12, 'bold'),
#             )
#         DataFrameRight.place(x=910, y=5, width=540, height=350)

#         self.txtbox = Text(
#             DataFrameRight,
#             font=('arial', 13, 'bold'),
#             width=32,
#             height=16,
#             padx=2,
#             pady=6,
#             )
#         self.txtbox.grid(row=0, column=2)
#         listScrollBar = Scrollbar(DataFrameRight)
#         listScrollBar.grid(row=0, column=1, sticky='ns')
#         listbooks = [
#             'CodeCrafting Basics',
#             'PythonEssentials',
#             'JS Fundamentals',
#             'Java Programming',
#             'C++ Crash Course',
#             'Ruby Handbook',
#             'Swift Basics',
#             'HTML & CSS Essentials',
#             'SQL Fundamentals',
#             'Go Programming',
#             'Python Tricks: Better Code',
#             'JavaScript Mastery',
#             'Java in Action',
#             ]

#         def SelectBook(event=''):
#             value = str(listbox.get(listbox.curselection()))
#             x = value
#             if x == 'CodeCrafting Basics':
#                 self.bookid_var.set('BKID1451')
#                 self.booktitle_var.set('CodeCrafrafer')
#                 self.auther_var.set('Paul Berry')
#                 d1 = datetime.datetime.today()
#                 d2 = datetime.timedelta(days=15)
#                 d3 = d1 + d2
#                 self.dateborrowed_var.set(d1)
#                 self.datedue_var.set(d3)
#                 self.days_var.set(15)
#                 self.latereturnfine_var.set('TK:20')
#                 self.dateoverdue_var.set('NO')
#                 self.finalprice_var.set('TK: 250')
#             elif x == 'PythonEssentials':

#                 self.bookid_var.set('BKID1452')
#                 self.booktitle_var.set('Python')
#                 self.auther_var.set('MICHEAL')
#                 d1 = datetime.datetime.today()
#                 d2 = datetime.timedelta(days=15)
#                 d3 = d1 + d2
#                 self.dateborrowed_var.set(d1)
#                 self.datedue_var.set(d3)
#                 self.days_var.set(15)
#                 self.latereturnfine_var.set('TK:20')
#                 self.dateoverdue_var.set('NO')
#                 self.finalprice_var.set('TK: 550')
#             elif x == 'JS Fundamentals':

#                 self.bookid_var.set('BKID1453')
#                 self.booktitle_var.set('JS Fundamentals')
#                 self.auther_var.set('John Doe')
#                 d1 = datetime.datetime.today()
#                 d2 = datetime.timedelta(days=15)
#                 d3 = d1 + d2
#                 self.dateborrowed_var.set(d1)
#                 self.datedue_var.set(d3)
#                 self.days_var.set('NO')
#                 self.latereturnfine_var.set('TK: 500')
#                 self.dateoverdue_var.set('NO')
#                 self.finalprice_var.set('TK:' + str(random.randint(200,
#                         800)))
#             elif x == 'Java Programming':

#                 self.bookid_var.set('BKID1454')
#                 self.booktitle_var.set('Java Programming')
#                 self.auther_var.set('Jane Smith')
#                 d1 = datetime.datetime.today()
#                 d2 = datetime.timedelta(days=15)
#                 d3 = d1 + d2
#                 self.dateborrowed_var.set(d1)
#                 self.datedue_var.set(d3)
#                 self.days_var.set('NO')
#                 self.latereturnfine_var.set('TK: 500')
#                 self.dateoverdue_var.set('NO')
#                 self.finalprice_var.set('TK:' + str(random.randint(200,
#                         800)))
#             elif x == 'C++ Crash Course':

#                 self.bookid_var.set('BKID1455')
#             self.booktitle_var.set('C++ Crash Course')
#             self.auther_var.set('Chris Anderson')
#             d1 = datetime.datetime.today()
#             d2 = datetime.timedelta(days=15)
#             d3 = d1 + d2
#             self.dateborrowed_var.set(d1)
#             self.datedue_var.set(d3)
#             self.days_var.set(15)
#             self.latereturnfine_var.set('TK:20')
#             self.dateoverdue_var.set('NO')
#             self.finalprice_var.set('TK: 450')

#         listbox = Listbox(DataFrameRight, font=('arial', 13, 'bold'),
#                         width=20, height=16)
#         listbox.bind('<<ListboxSelect>>', SelectBook)
#         listbox.grid(row=0, column=0, padx=4)
#         listScrollBar.config(command=listbox.yview)
#         for item in listbooks:
#             listbox.insert(END, item)

#     # -------------------------Buttons Frame-------------

#         framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20,
#                             bg='powder blue')
#         framebutton.place(x=0, y=530, width=1530, height=70)

#     # Add Data Button

#         btnAddData = Button(
#             framebutton,
#             command=self.add_data,
#             text='Add Data',
#             font=('arial', 13, 'bold'),
#             width=23,
#             bg='blue',
#             fg='white',
#             )

#     # Show Data Button

#         btnShowData = Button(
#             framebutton,
#             command=self.showData,
#             text='Show Data',
#             font=('arial', 13, 'bold'),
#             width=23,
#             bg='green',
#             fg='white',
#             )
#         btnShowData.grid(row=0, column=1)

#     # Update Button

#         btnUpdate = Button(
#             framebutton,
#             text='Update',
#             font=('arial', 13, 'bold'),
#             width=23,
#             bg='orange',
#             fg='white',
#             )
#         btnUpdate.grid(row=0, column=2)

#     # Delete Button

#         btnDelete = Button(
#             framebutton,
#             text='Delete',
#             font=('arial', 13, 'bold'),
#             width=23,
#             bg='red',
#             fg='white',
#             )
#         btnDelete.grid(row=0, column=3)

#     # Reset Button

#         btnReset = Button(
#             framebutton,
#             text='Reset',
#             font=('arial', 13, 'bold'),
#             width=23,
#             bg='purple',
#             fg='white',
#             )
#         btnReset.grid(row=0, column=4)

#     # Exit Button

#         btnExit = Button(
#             framebutton,
#             text='Exit',
#             font=('arial', 13, 'bold'),
#             width=23,
#             bg='gray',
#             fg='white',
#             )
#         btnExit.grid(row=0, column=5)

#     # -------------------------Information-------------

#         frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20,
#                             bg='powder blue')
#         frameDetails.place(x=0, y=600, width=1530, height=210)

#         Table_frame = Frame(frameDetails, bd=6, relief=RIDGE,
#                             bg='powder blue')
#         Table_frame.place(x=0, y=2, width=1460, height=190)
#         xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
#         yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

#         self.library_table = ttk.Treeview(Table_frame, columns=(
#             'memberType',
#             'prnno',
#             'title',
#             'firstname',
#             'lastname',
#             'address1',
#             'address2',
#             'postid',
#             'mobile',
#             'bookid',
#             'booktitle',
#             'auther',
#             'dateborrowed',
#             'datedue',
#             'days',
#             'latereturnfine',
#             'dateoverdue',
#             'finalprice',
#             ), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
#         xscroll.pack(side=BOTTOM, fill=X)
#         yscroll.pack(side=RIGHT, fill=Y)

#         xscroll.config(command=self.library_table.xview)
#         yscroll.config(command=self.library_table.yview)

#         self.library_table.heading('memberType', text='Member     Type')
#         self.library_table.heading('prnno', text='PRN No')
#         self.library_table.heading('title', text='Title')
#         self.library_table.heading('firstname', text='First     Name')
#         self.library_table.heading('lastname', text='Last Name')
#         self.library_table.heading('address1', text='Address1')
#         self.library_table.heading('address2', text='Address2')
#         self.library_table.heading('postid', text='Post Code')
#         self.library_table.heading('mobile', text='Mobile     Number')
#         self.library_table.heading('bookid', text='Book ID')
#         self.library_table.heading('booktitle', text='Book     Title')
#         self.library_table.heading('auther', text='Author')
#         self.library_table.heading('dateborrowed',
#                                 text='Date     Borrowed')
#         self.library_table.heading('datedue', text='Due Date')
#         self.library_table.heading('days', text='Days')
#         self.library_table.heading('latereturnfine',
#                                 text='Late     Return Fine')
#         self.library_table.heading('dateoverdue',
#                                 text='Date     Overdue')
#         self.library_table.heading('finalprice', text='Final     Price')

#         self.library_table['show'] = 'headings'
#         self.library_table.pack(fill=BOTH, expand=1)

#     # Set column widths

#         columns = [
#             'memberType',
#             'prnno',
#             'title',
#             'firstname',
#             'lastname',
#             'address1',
#             'address2',
#             'postid',
#             'mobile',
#             'bookid',
#             'booktitle',
#             'auther',
#             'dateborrowed',
#             'datedue',
#             'days',
#             'latereturnfine',
#             'dateoverdue',
#             'finalprice',
#             ]

#         for col in columns:
#             self.library_table.column(col, width=100)

#             self.fetch_data()
#             self.library_table.bind('<<>ButtonRelease-1>',
#                                     self.get_cursor)


#     # ... (previous code)

# def add_data(self):
#     conn = mysql.connector.connect(host='localhost', username='root',
#                                 password='ASdf12@#',
#                                 database='edulibrarydb')
#     my_cursor = conn.cursor()
#     my_cursor.execute('insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#                     , (
#         self.member_var.get(),
#         self.prn_var.get(),
#         self.title_var.get(),
#         self.firstname_var.get(),
#         self.lastname_var.get(),
#         self.address1_var.get(),
#         self.address2_var.get(),
#         self.postid_var.get(),
#         self.mobile_var.get(),
#         self.bookid_var.get(),
#         self.booktitle_var.get(),
#         self.auther_var.get(),
#         self.dateborrowed_var.get(),
#         self.datedue_var.get(),
#         self.days_var.get(),
#         self.latereturnfine_var.get(),
#         self.dateoverdue_var.get(),
#         self.finalprice_var.get(),
#         ))

#     conn.commit()
#     self.fetch_data()
#     conn.close()


# # Show message after add

# messagebox.showinfo('Success', 'Member has been inserted Successfully')

# if __name__ == '__main__':
#     root = Tk()
#     obj = LibraryManagementSystem(root)
#     root.mainloop()
