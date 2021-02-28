def adatta_nome(s):
    '''Adatta i nomi dei comuni secondo report AUSL e correggi errori'''
    replacing = {
        'Campogaliano'           : 'Campogalliano',
        'Non residenti in prov.' : 'Fuori provincia',
        'MODENA'                 : 'Modena',
        'Pavullo nel Frignano'   : 'Pavullo',
        'Fiorano Modenese'       : 'Fiorano M.',
        'Prignano sulla Secchia' : 'Prignano',
        'San Cesario sul Panaro' : 'San Cesario S/P',
        'Savignano sul Panaro'   : 'Savignano S/P',
        'Concordia sulla Secchia': 'Concordia',
        'San Felice sul Panaro'  : 'San Felice S/P',
        'Castelfranco Emilia'    : 'Castelfranco E.',
        'Castelnuovo Rangone'    : 'Castelnuovo R.',
        'Castelvetro di Modena'  : 'Castelvetro',
        'Marano sul Panaro'      : 'Marano',
        'Novi di Modena'         : 'Novi'
    }
    
    for it in replacing.items():
        s = s.replace(it[0],it[1])
    return s


def importa_abitanti(file):
    '''Lettura abitanti da tabella https://www.tuttitalia.it/emilia-romagna/provincia-di-modena/70-comuni/popolazione/ 
    Riportano come fonte dati ISTAT 31/12/2019'''
    abitanti={}
    with open(file) as f:
        for lines in f.readlines():
            l = lines.replace('.','').rstrip().split('\t')
            if l[0].replace(' ','').isdigit():
                comune = adatta_nome(l[1])
                numero = int(l[2])
                abitanti[comune] = numero
                                     
    return abitanti
