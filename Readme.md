# Dati Covid19 provincia di Modena 

La repository contiene i dati dei **nuovi positivi** della provincia di Modena divisi per comune. I dati sono ricavati dalle pubblicazioni giornaliere del sito di  [sulpanaro.net](sulpanaro.net) ([qui](https://www.sulpanaro.net/2021/02/aggiornamento-coronavirus-28-2-nel-modenese-402-nuovi-casi/) ad esempio il report del 28/02), che a sua volta riporta il bollettino quotidiano emesso dall'AUSL di Modena non pubblico.

Nell'attesa che l'AUSL pubblichi uno storico strutturato e attendibile, ho deciso di raccolgiere i dati e metterli a disposizione.

Nella cartella **report_vari** si trovano (sia in formato Excel che csv):

* **nuovi_positivi_comuni_MO.xlsx**: nuovi positivi per ogni giorno per tutti i comuni della provincia
* **nuovi_positivi_rolling7gg_comuni_MO.xlsx**: somma mobile 7gg. dei dati di cui sopra

La cartella **giornaliero** contiene invece i dati di partenza. Si tratta di un file di testo per ogni giorno e corrisponde al testo contenuto nei bollettini periodici dell'AUSL riportati dal giornale sulpanaro.net all'interno delle proprie pagine online. In alcuni casi questo è stato fatto con degli screenshot e nella cartella si trova la corrispondente immagine (l'import di questi dati è ancora in corso, le immagini già processate sono nella sottocartella)


Nota: <font color=red>alcuni giorni mancano</font>. La raccolta sarà aggiornata costantemente ma al momento non tutti i giorni sono presenti. Il 2021 è quasi completo, ma il 2020 (i dati partono da metà settembre) ha molti buchi. 

Per qualsiasi richiesta o suggerimento: ![](./email.png)


### Grafici

L'idea di questa raccolta dati nasce da una discussione su un gruppo FB di Nonantola a proposito di un grafico che un consigliere comunale ha mostrato per mettere in evidenza l'aumento dei contagi a Nonantola rispetto al trend provinciale/regionale/nazionale. 

Nel far notare i limiti di quella visualizzazione, ho pensato di poter continuare quel lavoro raccogliando tutti i dati disponibili.

Questo è un grafico di esempio che riguarda appunto Nonantola. Il [Jupyter notebook](CovidNonantola_contesto.ipynb) usato per produrlo contiene anche le info sulla lettura dei dati e il modo in cui sono stati trattati.

![](./Nonantola.png)

### Emilia Romagna

Andamento dei positivi settimanali (somma mobile 7gg rapportata a 100 mila abitanti) per le province.
[Notebook](plot_provincia.ipynb).

![](./emilia_romagna.png)