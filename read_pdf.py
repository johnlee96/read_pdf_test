from camelot import read_pdf,plot
tables = read_pdf('volume16.pdf',pages='6',flavor = 'stream',
        table_areas=['40,800,545,50'],columns=['63,155,213,274,323,381,431,490'],split_text=True
    )
plot(tables[0], kind='contour').show()
input("Press any key to terminate the program")
print("See you later.")