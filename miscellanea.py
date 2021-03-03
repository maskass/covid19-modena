import pandas as pd
import numpy as np

def importa_dati_italia(dataset):
    df = pd.read_csv(dataset)
    temp = df[['data','nuovi_positivi']].groupby(by='data').sum()
    ita = pd.Series(data=temp.nuovi_positivi.values, index=pd.to_datetime(temp.index).map(lambda x: x.replace(hour=0))) # imposta ora 0
    return ita

def importa_dati_emr(dataset):
    df = pd.read_csv(dataset)
    temp = df[df.denominazione_regione=='Emilia-Romagna']
    emr = pd.Series(data=temp.nuovi_positivi.values, index=pd.to_datetime(temp.data).map(lambda x: x.replace(hour=0))) # imposta ora 0
    return emr

def importa_dati_prov(dataset):
    df = pd.read_csv(dataset)
    temp = df[df.denominazione_provincia=='Modena'][['data','totale_casi']]
    mo = pd.Series(data=temp.totale_casi.diff().values.astype(int), index=pd.to_datetime(temp.data).map(lambda x: x.replace(hour=0))) # imposta ora 0
    return mo
    
def importa_dati_giornalieri(lista_file_comuni):
    '''Legge i file giornalieri e restituisce un dataframe'''
    dlist=[]   # lista di dictionary che conterranno i dati dei comuni
    daylist=[] # lista dei giorni (presi dal nome del file)
    for file in lista_file_comuni:
        with open(file) as f:
            d = {}
            for l in f.readlines():
                campi = l.rstrip().split(' ')

                # salta le linee vuote
                if len(campi[-1])==0:
                    continue

                # se l'ultimo campo è un numero, associa quel numero alla stringa precedente (Comune)
                # altrimenti prendi tutta la linea come Comune e associa il nr 0
                if campi[-1].isdigit():
                    comune = ' '.join(campi[:-1])
                    nuovi  = campi[-1]
                else:
                    comune = ' '.join(campi)
                    nuovi  = 0

                comune = comune.rstrip().lstrip()
                comune = adatta_nome(comune)
                d[comune]=nuovi

            dlist.append(d)
            daylist.append(file.split('_')[-1].split('.')[0])

    # crea dataframe
    dayindex = pd.to_datetime(daylist, format='%d-%m-%Y')
    df = pd.DataFrame(data=dlist, index=dayindex).sort_index()
    df = df.fillna(0).astype(int)
    return df


def date_mancanti(df):
    '''Analizza dataframe con indice temporale (giorni) e restituisce elenco giorni mancanti'''
    giorni = pd.Series(df.index, index=df.index).diff()
    for g in zip(giorni[giorni>pd.to_timedelta('1 day')].index, giorni[giorni>pd.to_timedelta('1 day')].values):
        print(f"{g[0].date()} --> mancano {g[1]/1e9 /3600/24 - 1 } giorni precedenti")


def adatta_nome(s):
    '''Adatta i nomi dei comuni secondo report AUSL e correggi errori'''
    replacing = {
        'Campogaliano'           : 'Campogalliano',
        'Non residenti in prov.' : 'Fuori provincia',
        'Non residenti in provincia': 'Fuori provincia',
        'Altra provincia'        : 'Fuori provincia',
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
