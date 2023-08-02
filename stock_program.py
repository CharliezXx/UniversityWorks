test = {'test':10}
action_selector = 0
stock = {}

while action_selector == 0:
    action_selector =int(input('==================\nselect action \n1.) add item\n2.) remove item\n3.) check stock\n==================\n:'))
    #-------------------------------------------------------------------
    if action_selector == 1:
        loop_controller = 0
        while loop_controller == 0:
            i_n = input('Item name [type "stop" to finish]: ')
            if i_n == 'stop':
                loop_controller = 1
            else:
                i_v	= int(input('Item value [only integer]: '))
                while i_v == 0 :
                    print('Invalid number')
                    i_v	= int(input('Item value: '))
                else:
                    print(i_v,'of '+i_n+'(s) has been added')
                    stock.update({i_n:i_v})
        
    #-------------------------------------------------------------------    
    elif action_selector == 3:
        if stock == {}:
            print("nothing in stock")
        else:
            print('Item(s) in stock :')
            print(stock)
            
    #-------------------------------------------------------------------
    elif action_selector == 2:
        if stock == {}:
            print("nothing in stock")
        else:
            i_n = dict(input('Item name: '))
            if stock.keys() == i_n:
                stock.pop(i_n)
                print('item has been deleted!')                
            else:
                print('there are no '+i_n+' in the stock!')
    #-------------------------------------------------------------------
    else:
        print('cannot perform that action')
    action_selector = 0