def total(filename, Year):

    totalInfo = dict()

    with open(filename) as file:
        line = file.readline()

        while line:
            line = line[:-1]
            parsedLine = line.split('\t')
            country = parsedLine[6]
            year = parsedLine[9]
            medal = parsedLine[14]

            if year == str(Year):
                if medal != 'NA':
                    if country in totalInfo:
                        if medal in totalInfo[country]:
                            totalInfo[country][medal]+=1
                        else:
                            totalInfo[country][medal]=1
                    else:
                        totalInfo[country]=dict()
                        totalInfo[country][medal] = 1
            line = file.readline()
    
    for countryName, results in totalInfo.items():
        print(f'{countryName}')
        for medal, count in results.items():
            print(f'\t{medal} - {count}')