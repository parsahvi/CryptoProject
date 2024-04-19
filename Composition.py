def dataGetter(value):
    data=value
    for i in range(len(data)):
        if data[i]['name']==value[-1]['name']:
            data[i]['ask']=value[-1]['ask']
            data[i]['bids']=value[-1]['bids']
    print(data)
    # the getter function(data)