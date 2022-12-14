def interactive(filename):
    while True:
        print('Введіть назву країни або код(exit для виходу):')
        value =  input('->')
        if value=='exit':
            break
        
        countryTotalInfo=dict()
        with open(filename) as file:
            line = file.readline()
            while line:
                line = line[:-1]
                parsedLine = line.split('\t')
                country = parsedLine[6]
                code = parsedLine[7]
                year = parsedLine[9]
                place = parsedLine[11]
                medal = parsedLine[14]
                
                if value == country or value == code:
                    if year not in countryTotalInfo:
                        countryTotalInfo[year]=dict()
                        countryTotalInfo[year]['Gold'] = 0
                        countryTotalInfo[year]['Silver'] = 0
                        countryTotalInfo[year]['Bronze'] = 0
                        countryTotalInfo[year]['total'] = 0
                    countryTotalInfo[year]['place']=place
                    if medal != 'NA':
                        countryTotalInfo[year]['total'] += 1
                        if medal in countryTotalInfo[year]:
                            countryTotalInfo[year][medal]+=1
                        else:
                            countryTotalInfo[year][medal]=1

                line = file.readline()
        
        countryTotalInfo=dict(sorted(countryTotalInfo.items()))

        theFirstYear = 3000
        theFirstYearPlace = ''

        theBest = 0
        theBestYear = 0
        theWorst = 99999
        theWorstYear = 0

        totalMedals={
            'Gold':0,
            'Silver':0,
            'Bronze':0,
            'total':0
        }
        counter = 0
        
        for y, results in countryTotalInfo.items():
            if theFirstYear > int(y):
                theFirstYear = int(y)
                theFirstYearPlace = results['place']
                
            print(f"{y}  - {results['place']}")
            for medal , count in results.items():
                print(f"\t{medal}  - {count}")
                if medal!='place':
                    totalMedals[medal]+=count
            if results['total'] > theBest:
                theBest = results['total']
                theBestYear = y
            if results['total'] < theWorst:
                theWorst = results['total']
                theWorstYear = y

            counter+=1

        print(f'Всередньому на кожній олімпіаді: ')
        print(f'золотих :{totalMedals["Gold"]/counter}')
        print(f'срібних :{totalMedals["Silver"]/counter}')
        print(f'бронзових :{totalMedals["Bronze"]/counter}')
        print(f'загально :{totalMedals["total"]/counter}')

        print(f'найгірший рік {theWorstYear} - {theWorst} медалей')
        print(f'найкращий рік {theBestYear} - {theBest} медалей')

        print(f'перший рік {theFirstYear} - {theFirstYearPlace}')
