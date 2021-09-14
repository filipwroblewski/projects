# take away all subtitles (Disenchantment)

def odczyt_row():
        if (row[0].isalpha() or row[0] == '-'): 
            #print(row, end="")
            with open('Disenchantment subtitles S01E01.txt', 'a') as subtitles_file:
                subtitles_file.write(row)

    

i = 0
with open('Disenchantment.S01E01.WEB-DL.DDP5.1.x264-NTG_STRiFE.English-WWW.MY-SUBS.COM.srt') as plik:
    for row in plik:
        if i > 2:
            odczyt_row()
        i += 1
print('done')
