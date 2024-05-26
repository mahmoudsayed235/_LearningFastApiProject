def createDict(firstname, lastname, age):
    '''
    dic=dict()
    dic['firstname']=firstname
    dic['lastname']=lastname
    dic['age']=age
    '''
    dic={
        "firstname" : firstname,
        "lastname" : lastname,
        "age" : age
    }
    '''
    
    '''

    return dic


new_dic=createDict('Mahmoud','Hassan',30)
for x, y in new_dic.items():
    print(x,y)