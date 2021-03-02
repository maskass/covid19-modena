import glob
import pandas as pd
from miscellanea import importa_abitanti, importa_dati_giornalieri


comuni = glob.glob('giornaliero/*.txt')
dfcomuni = importa_dati_giornalieri(comuni)

abitanti = importa_abitanti('abitanti_provincia_di_Modena.txt')

roll = dfcomuni.rolling(7, center=True).sum()

dfcomuni.to_excel('report_vari/nuovi_positivi_comuni_MO.xlsx')
roll.to_excel('report_vari/nuovi_positivi_rolling7gg_comuni_MO.xlsx')

lista_output = [ comune for comune in dfcomuni.columns if (comune!='Fuori provincia')&(comune!='TOTALE') ]

for comune in lista_output :
    nome_file = comune.replace(' ','').replace('.','').replace('/','') # crea nomi di file semplici
    temp_df = pd.concat((dfcomuni[comune], roll[comune], roll[comune]/abitanti[comune]*100000), axis=1)
    temp_df.columns = ['nuovi pos.', 'somma mobile 7gg.', 'somma mobile 7gg. per 100mila abitanti']
    temp_df.to_excel('report_vari/comuni/' + nome_file + '.xlsx')
    temp_df.to_csv('report_vari/comuni/' + nome_file + '.csv')