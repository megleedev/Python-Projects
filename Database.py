import sqlite3

connector = sqlite3.connect('database.db')

# Creates a table called tbl_txt that will hold the file list
# The table has two columns - 
# an ID column that increments by one
# and a col_filename string column
with connector:
    cursor = connector.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_txt( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    connector.commit()

# Tuple of file names with different file extensions
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Uses a for loop to identify files that end with .txt
# Adds the .txt files to the database in col_filename
# Prints the file names to the console
for x in fileList:
    if x.endswith ('.txt'):
        with connector:
            cursor = connector.cursor()
            cursor.execute ("INSERT INTO tbl_txt (col_filename) VALUES (?)", (x,))
            print (x)

connector.close()