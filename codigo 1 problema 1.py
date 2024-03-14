# Autor: Luiz Felipe Santana Sena
# Componente Curricular: Algoritmos I
# Concluído em: 04/04/2023
# Declaro que este código foi elaborado por mim de forma individual e não contém
# nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
# código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

chrome_segunda = 0
chrome_terca = 0
chrome_quarta = 0
chrome_quinta = 0
chrome_sexta = 0
chrome_sabado = 0
chrome_domingo = 0
facebook_segunda = 0
facebook_terca = 0
facebook_quarta = 0
facebook_quinta = 0
facebook_sexta = 0
facebook_sabado = 0
facebook_domingo = 0
instagram_segunda = 0
instagram_terca = 0
instagram_quarta = 0
instagram_quinta = 0
instagram_sexta = 0
instagram_sabado = 0
instagram_domingo = 0
whatsapp_segunda = 0
whatsapp_terca = 0
whatsapp_quarta = 0
whatsapp_quinta = 0
whatsapp_sexta = 0
whatsapp_sabado = 0
whatsapp_domingo = 0
outros_segunda = 0
outros_terca = 0
outros_quarta = 0
outros_quinta = 0
outros_sexta = 0
outros_sabado = 0
outros_domingo = 0

total_chrome_segunda = 0
total_chrome_terca = 0
total_chrome_quarta = 0
total_chrome_quinta = 0
total_chrome_sexta = 0
total_chrome_sabado = 0
total_chrome_domingo = 0
total_facebook_segunda = 0
total_facebook_terca = 0
total_facebook_quarta = 0
total_facebook_quinta = 0
total_facebook_sexta = 0
total_facebook_sabado = 0
total_facebook_domingo = 0
total_instagram_segunda = 0
total_instagram_terca = 0
total_instagram_quarta = 0
total_instagram_quinta = 0
total_instagram_sexta = 0
total_instagram_sabado = 0
total_instagram_domingo = 0
total_whatsapp_segunda = 0
total_whatsapp_terca = 0
total_whatsapp_quarta = 0
total_whatsapp_quinta = 0
total_whatsapp_sexta = 0
total_whatsapp_sabado = 0
total_whatsapp_domingo = 0
total_outros_segunda = 0
total_outros_terca = 0
total_outros_quarta = 0
total_outros_quinta = 0
total_outros_sexta = 0
total_outros_sabado = 0
total_outros_domingo = 0

x = 0
while x == 0:
    codigo = int(0)
    print("menu: \n1 para chrome \n2 para facebook \n3 para instagram \n4 para whatsapp \n5 para outros")
    while 1 > codigo or codigo > 5:
        codigo = int(input("digite o codigo para o aplicativo, das opções acima"))
    dia = int(0)
    print("menu: \n1 para segunda \n2 para terça \n3 para quarta \n4 para quinta \n5 para sexta \n6 para sabado \n7 para domingo")
    while 1 > dia or dia > 7:
        dia = int(input("digite o dia da semana, das opções acima"))
    bytes = float(-10)
    while bytes <= 0:
        bytes = float(input("digite o numero correspondente a quantidade de bytes que foi gasto"))
    # 1-1
    if codigo == 1 and dia == 1:
        chrome_segunda += bytes
    elif codigo == 2 and dia == 1:
        facebook_segunda += bytes
    elif codigo == 3 and dia == 1:
        instagram_segunda += bytes
    elif codigo == 4 and dia == 1:
        whatsapp_segunda += bytes
    elif codigo == 5 and dia == 1:
        outros_segunda += bytes
    # 2-1
    elif codigo == 1 and dia == 2:
        chrome_terca += bytes
    elif codigo == 2 and dia == 2:
        facebook_terca += bytes
    elif codigo == 3 and dia == 2:
        instagram_terca += bytes
    elif codigo == 4 and dia == 2:
        whatsapp_terca += bytes
    elif codigo == 5 and dia == 2:
        outros_terca += bytes
    # 3-1
    elif codigo == 1 and dia == 3:
        chrome_quarta += bytes
    elif codigo == 2 and dia == 3:
        facebook_quarta += bytes
    elif codigo == 3 and dia == 3:
        instagram_quarta += bytes
    elif codigo == 4 and dia == 3:
        whatsapp_quarta += bytes
    elif codigo == 5 and dia == 3:
        outros_quarta += bytes
    # 4-1
    elif codigo == 1 and dia == 4:
        chrome_quinta += bytes
    elif codigo == 2 and dia == 4:
        facebook_quinta += bytes
    elif codigo == 3 and dia == 4:
        instagram_quinta += bytes
    elif codigo == 4 and dia == 4:
        whatsapp_quinta += bytes
    elif codigo == 5 and dia == 4:
        outros_quinta += bytes
    # 5-1
    elif codigo == 1 and dia == 5:
        chrome_sexta += bytes
    elif codigo == 2 and dia == 5:
        facebook_sexta += bytes
    elif codigo == 3 and dia == 5:
        instagram_sexta += bytes
    elif codigo == 4 and dia == 5:
        whatsapp_sexta += bytes
    elif codigo == 5 and dia == 5:
        outros_sexta += bytes
    # 6-1
    elif codigo == 1 and dia == 6:
        chrome_sabado += bytes
    elif codigo == 2 and dia == 6:
        facebook_sabado += bytes
    elif codigo == 3 and dia == 6:
        instagram_sabado += bytes
    elif codigo == 4 and dia == 6:
        whatsapp_sabado += bytes
    elif codigo == 5 and dia == 6:
        outros_sabado += bytes
    # 7-1
    elif codigo == 1 and dia == 7:
        chrome_domingo += bytes
    elif codigo == 2 and dia == 7:
        facebook_domingo += bytes
    elif codigo == 3 and dia == 7:
        instagram_domingo += bytes
    elif codigo == 4 and dia == 7:
        whatsapp_domingo += bytes
    elif codigo == 5 and dia == 7:
        outros_domingo += bytes
    #adicionar as acumulativas
    total_chrome_segunda += chrome_segunda
    total_chrome_terca += chrome_terca
    total_chrome_quarta += chrome_quarta
    total_chrome_quinta += chrome_quinta
    total_chrome_sexta += chrome_sexta
    total_chrome_sabado += chrome_sabado
    total_chrome_domingo += chrome_domingo
    total_facebook_segunda += facebook_segunda
    total_facebook_terca += facebook_terca
    total_facebook_quarta += facebook_quarta
    total_facebook_quinta += facebook_quinta
    total_facebook_sexta += facebook_sexta
    total_facebook_sabado += facebook_sabado
    total_facebook_domingo += facebook_domingo
    total_instagram_segunda += instagram_segunda
    total_instagram_terca += instagram_terca
    total_instagram_quarta += instagram_quarta
    total_instagram_quinta += instagram_quinta
    total_instagram_sexta += instagram_sexta
    total_instagram_sabado += instagram_sabado
    total_instagram_domingo += instagram_domingo
    total_whatsapp_segunda += whatsapp_segunda
    total_whatsapp_terca += whatsapp_terca
    total_whatsapp_quarta += whatsapp_quarta
    total_whatsapp_quinta += whatsapp_quinta
    total_whatsapp_sexta += whatsapp_sexta
    total_whatsapp_sabado += whatsapp_sabado
    total_whatsapp_domingo += whatsapp_domingo
    total_outros_segunda += outros_segunda
    total_outros_terca += outros_terca
    total_outros_quarta += outros_quarta
    total_outros_quinta += outros_quinta
    total_outros_sexta += outros_sexta
    total_outros_sabado += outros_sabado
    total_outros_domingo += outros_domingo
    # fazendo os calculos dos dados pedidos 
    chrome_semana = total_chrome_segunda + total_chrome_terca + total_chrome_quarta + total_chrome_quinta + total_chrome_sexta + total_chrome_sabado + total_chrome_domingo
    facebook_semana = total_facebook_segunda + total_facebook_terca + total_facebook_quarta + total_facebook_quinta + total_facebook_sexta + total_facebook_sabado + total_facebook_domingo
    instagram_semana = total_instagram_segunda + total_instagram_terca + total_instagram_quarta + total_instagram_quinta + total_instagram_sexta + total_instagram_sabado + total_instagram_domingo
    whatsapp_semana = total_whatsapp_segunda + total_whatsapp_terca + total_whatsapp_quarta + total_whatsapp_quinta + total_whatsapp_sexta + total_whatsapp_sabado + total_whatsapp_domingo
    outros_semana = total_outros_segunda + total_outros_terca + total_outros_quarta + total_outros_quinta + total_outros_sexta + total_outros_sabado + total_outros_domingo

    total_segunda = total_chrome_segunda + total_facebook_segunda + total_instagram_segunda + total_whatsapp_segunda + total_outros_segunda
    total_terca = total_chrome_terca + total_facebook_terca + total_instagram_terca + total_whatsapp_terca + total_outros_terca
    total_quarta = total_chrome_quarta + total_facebook_quarta + total_instagram_quarta + total_whatsapp_quarta + total_outros_quarta
    total_quinta = total_chrome_quinta + total_facebook_quinta + total_instagram_quinta + total_whatsapp_quinta + total_outros_quinta
    total_sexta = total_chrome_sexta + total_facebook_sexta + total_instagram_sexta + total_whatsapp_sexta + total_outros_sexta
    total_sabado = total_chrome_sabado + total_facebook_sabado + total_instagram_sabado + total_whatsapp_sabado + total_outros_sabado
    total_domingo = total_chrome_domingo + total_facebook_domingo + total_instagram_domingo + total_whatsapp_domingo + total_outros_domingo

    total_todos_os_apps_semana = total_segunda + total_terca + total_quarta + total_quinta + total_sexta + total_sabado + total_domingo

    media_diaria_semana_total = (total_todos_os_apps_semana/7)

    media_diaria_semana_chrome = chrome_semana/7
    media_diaria_semana_facebook = facebook_semana/7
    media_diaria_semana_instagram = instagram_semana/7
    media_diaria_semana_whatsapp = whatsapp_semana/7
    media_diaria_semana_outros = outros_semana/7
    # zerando variaveis para soma, ja que é adicionado o valor de bytes a variavel e não substituido o valor
    chrome_segunda = 0
    chrome_terca = 0
    chrome_quarta = 0
    chrome_quinta = 0
    chrome_sexta = 0
    chrome_sabado = 0
    chrome_domingo = 0
    facebook_segunda = 0
    facebook_terca = 0
    facebook_quarta = 0
    facebook_quinta = 0
    facebook_sexta = 0
    facebook_sabado = 0
    facebook_domingo = 0
    instagram_segunda = 0
    instagram_terca = 0
    instagram_quarta = 0
    instagram_quinta = 0
    instagram_sexta = 0
    instagram_sabado = 0
    instagram_domingo = 0
    whatsapp_segunda = 0
    whatsapp_terca = 0
    whatsapp_quarta = 0
    whatsapp_quinta = 0
    whatsapp_sexta = 0
    whatsapp_sabado = 0
    whatsapp_domingo = 0
    outros_segunda = 0
    outros_terca = 0
    outros_quarta = 0
    outros_quinta = 0
    outros_sexta = 0
    outros_sabado = 0
    outros_domingo = 0
    #pedido, quer continuar sem relatorio? quer relatório e continuar? só o relatório ?

    x = 4
    while x < 0 or x > 2:
        x = int(input("digite 0 se deseja fazer um novo cadastramento sem relatório \ndigite 1 se deseja ver o relatório e fazer novo recadastramento\nu digite 2 se deseja apenas ver o relatório"))
    if x == 0:
        print('será feito um novo cadastro de dados')
    elif x == 1:
        #total de dados usados por cada aplicativo por dia:
        #chrome
        print ('o total de dados usados pelo chrome na segunda feira foi:', total_chrome_segunda,'bytes')
        print ('o total de dados usados pelo chrome na terça feira foi:', total_chrome_terca,'bytes')
        print ('o total de dados usados pelo chrome na quarta feira foi:', total_chrome_quarta,'bytes')
        print ('o total de dados usados pelo chrome na quinta feira foi:', total_chrome_quinta,'bytes')
        print ('o total de dados usados pelo chrome na sexta feira foi:', total_chrome_sexta,'bytes')
        print ('o total de dados usados pelo chrome na sabado feira foi:', total_chrome_sabado,'bytes')
        print ('o total de dados usados pelo chrome na domingo feira foi:', total_chrome_domingo,'bytes')
        #facebook
        print ('o total de dados usados pelo facebook na segunda feira foi:', total_facebook_segunda,'bytes')
        print ('o total de dados usados pelo facebook na terça feira foi:', total_facebook_terca,'bytes')
        print ('o total de dados usados pelo facebook na quarta feira foi:', total_facebook_quarta,'bytes')
        print ('o total de dados usados pelo facebook na quinta feira foi:', total_facebook_quinta,'bytes')
        print ('o total de dados usados pelo facebook na sexta feira foi:', total_facebook_sexta,'bytes')
        print ('o total de dados usados pelo facebook na sabado feira foi:', total_facebook_sabado,'bytes')
        print ('o total de dados usados pelo facebook na domingo feira foi:', total_facebook_domingo,'bytes')
        #instagram
        print ('o total de dados usados pelo instagram na segunda feira foi:', total_instagram_segunda,'bytes')
        print ('o total de dados usados pelo instagram na terça feira foi:', total_instagram_terca,'bytes')
        print ('o total de dados usados pelo instagram na quarta feira foi:', total_instagram_quarta,'bytes')
        print ('o total de dados usados pelo instagram na quinta feira foi:', total_instagram_quinta,'bytes')
        print ('o total de dados usados pelo instagram na sexta feira foi:', total_instagram_sexta,'bytes')
        print ('o total de dados usados pelo instagram na sabado feira foi:', total_instagram_sabado,'bytes')
        print ('o total de dados usados pelo instagram na domingo feira foi:', total_instagram_domingo,'bytes')
        #whatsapp
        print ('o total de dados usados pelo whatsapp na segunda feira foi:', total_whatsapp_segunda,'bytes')
        print ('o total de dados usados pelo whatsapp na terça feira foi:', total_whatsapp_terca,'bytes')
        print ('o total de dados usados pelo whatsapp na quarta feira foi:', total_whatsapp_quarta,'bytes')
        print ('o total de dados usados pelo whatsapp na quinta feira foi:', total_whatsapp_quinta,'bytes')
        print ('o total de dados usados pelo whatsapp na sexta feira foi:', total_whatsapp_sexta,'bytes')
        print ('o total de dados usados pelo whatsapp na sabado feira foi:', total_whatsapp_sabado,'bytes')
        print ('o total de dados usados pelo whatsapp na domingo feira foi:', total_whatsapp_domingo,'bytes')
        #outros
        print ('o total de dados usados pelo outros na segunda feira foi:', total_outros_segunda,'bytes')
        print ('o total de dados usados pelo outros na terça feira foi:', total_outros_terca,'bytes')
        print ('o total de dados usados pelo outros na quarta feira foi:', total_outros_quarta,'bytes')
        print ('o total de dados usados pelo outros na quinta feira foi:', total_outros_quinta,'bytes')
        print ('o total de dados usados pelo outros na sexta feira foi:', total_outros_sexta,'bytes')
        print ('o total de dados usados pelo outros na sabado feira foi:', total_outros_sabado,'bytes')
        print ('o total de dados usados pelo outros na domingo feira foi:', total_outros_domingo,'bytes')
        # total de dados usados por cada aplicativo na semana
        print ('o total de dados usados pelo chrome na semana foi:', chrome_semana,'bytes')
        print ('o total de dados usados pelo facebook na semana foi:', facebook_semana,'bytes')
        print ('o total de dados usados pelo instagram na semana foi:', instagram_semana,'bytes')
        print ('o total de dados usados pelo whatsapp na semana foi:', whatsapp_semana,'bytes')
        print ('o total de dados usados por outros na semana foi:', outros_semana,'bytes')
        # total de dados totais usados em cada dia
        print ('o total de dados usados na segunda feira foi', total_segunda,'bytes')
        print ('o total de dados usados na terça feira foi', total_terca,'bytes')
        print ('o total de dados usados na quarta feira foi', total_quarta,'bytes')
        print ('o total de dados usados na quinta feira foi', total_quinta,'bytes')
        print ('o total de dados usados na sexta feira foi', total_sexta,'bytes')
        print ('o total de dados usados no sabado foi', total_sabado,'bytes')
        print ('o total de dados usados no domingo feira foi', total_domingo,'bytes')
        # total de dados totais usados na semana
        print ("o total de dados usados foi:", total_todos_os_apps_semana,'bytes')
        # media diaria de consumo total de dados
        print ("a media diaria de dados usados ", media_diaria_semana_total,'bytes')
        # media diaria de consumo de dados de cada aplicativo
        print ('a media diaria de dados usados do chrome foi', media_diaria_semana_chrome,'bytes')
        print ('a media diaria de dados usados do facebook foi', media_diaria_semana_facebook,'bytes')
        print ('a media diaria de dados usados do instagram foi', media_diaria_semana_instagram,'bytes') 
        print ('a media diaria de dados usados do whatsapp foi', media_diaria_semana_whatsapp,'bytes') 
        print ('a media diaria de dados usados do outros foi', media_diaria_semana_outros,'bytes')
        print('será feito um novo cadastro de dados')
        x = 0
    elif x == 2:
        #total de dados usados por cada aplicativo por dia:
        #chrome
        print ('o total de dados usados pelo chrome na segunda feira foi:', total_chrome_segunda,'bytes')
        print ('o total de dados usados pelo chrome na terça feira foi:', total_chrome_terca,'bytes')
        print ('o total de dados usados pelo chrome na quarta feira foi:', total_chrome_quarta,'bytes')
        print ('o total de dados usados pelo chrome na quinta feira foi:', total_chrome_quinta,'bytes')
        print ('o total de dados usados pelo chrome na sexta feira foi:', total_chrome_sexta,'bytes')
        print ('o total de dados usados pelo chrome na sabado foi:', total_chrome_sabado,'bytes')
        print ('o total de dados usados pelo chrome na domingo foi:', total_chrome_domingo,'bytes')
        #facebook
        print ('o total de dados usados pelo facebook na segunda feira foi:', total_facebook_segunda,'bytes')
        print ('o total de dados usados pelo facebook na terça feira foi:', total_facebook_terca,'bytes')
        print ('o total de dados usados pelo facebook na quarta feira foi:', total_facebook_quarta,'bytes')
        print ('o total de dados usados pelo facebook na quinta feira foi:', total_facebook_quinta,'bytes')
        print ('o total de dados usados pelo facebook na sexta feira foi:', total_facebook_sexta,'bytes')
        print ('o total de dados usados pelo facebook na sabado foi:', total_facebook_sabado,'bytes')
        print ('o total de dados usados pelo facebook na domingo foi:', total_facebook_domingo,'bytes')
        #instagram
        print ('o total de dados usados pelo instagram na segunda feira foi:', total_instagram_segunda,'bytes')
        print ('o total de dados usados pelo instagram na terça feira foi:', total_instagram_terca,'bytes')
        print ('o total de dados usados pelo instagram na quarta feira foi:', total_instagram_quarta,'bytes')
        print ('o total de dados usados pelo instagram na quinta feira foi:', total_instagram_quinta,'bytes')
        print ('o total de dados usados pelo instagram na sexta feira foi:', total_instagram_sexta,'bytes')
        print ('o total de dados usados pelo instagram na sabado foi:', total_instagram_sabado,'bytes')
        print ('o total de dados usados pelo instagram na domingo foi:', total_instagram_domingo,'bytes')
        #whatsapp
        print ('o total de dados usados pelo whatsapp na segunda feira foi:', total_whatsapp_segunda,'bytes')
        print ('o total de dados usados pelo whatsapp na terça feira foi:', total_whatsapp_terca,'bytes')
        print ('o total de dados usados pelo whatsapp na quarta feira foi:', total_whatsapp_quarta,'bytes')
        print ('o total de dados usados pelo whatsapp na quinta feira foi:', total_whatsapp_quinta,'bytes')
        print ('o total de dados usados pelo whatsapp na sexta feira foi:', total_whatsapp_sexta,'bytes')
        print ('o total de dados usados pelo whatsapp na sabado foi:', total_whatsapp_sabado,'bytes')
        print ('o total de dados usados pelo whatsapp na domingo foi:', total_whatsapp_domingo,'bytes')
        #outros
        print ('o total de dados usados pelo outros na segunda feira foi:', total_outros_segunda,'bytes')
        print ('o total de dados usados pelo outros na terça feira foi:', total_outros_terca,'bytes')
        print ('o total de dados usados pelo outros na quarta feira foi:', total_outros_quarta,'bytes')
        print ('o total de dados usados pelo outros na quinta feira foi:', total_outros_quinta,'bytes')
        print ('o total de dados usados pelo outros na sexta feira foi:', total_outros_sexta,'bytes')
        print ('o total de dados usados pelo outros na sabado foi:', total_outros_sabado,'bytes')
        print ('o total de dados usados pelo outros na domingo foi:', total_outros_domingo,'bytes')
        # total de dados usados por cada aplicativo na semana
        print ('o total de dados usados pelo chrome na semana foi:', chrome_semana,'bytes')
        print ('o total de dados usados pelo facebook na semana foi:', facebook_semana,'bytes')
        print ('o total de dados usados pelo instagram na semana foi:', instagram_semana,'bytes')
        print ('o total de dados usados pelo whatsapp na semana foi:', whatsapp_semana,'bytes')
        print ('o total de dados usados por outros na semana foi:', outros_semana,'bytes')
        # total de dados totais usados em cada dia
        print ('o total de dados usados na segunda feira foi', total_segunda,'bytes')
        print ('o total de dados usados na terça feira foi', total_terca,'bytes')
        print ('o total de dados usados na quarta feira foi', total_quarta,'bytes')
        print ('o total de dados usados na quinta feira foi', total_quinta,'bytes')
        print ('o total de dados usados na sexta feira foi', total_sexta,'bytes')
        print ('o total de dados usados no sabado foi', total_sabado,'bytes')
        print ('o total de dados usados no domingo foi', total_domingo,'bytes')
        # total de dados totais usados na semana
        print ("o total de dados usados foi:", total_todos_os_apps_semana,'bytes')
        # media diaria de consumo total de dados
        print ("a media diaria de dados usados ", media_diaria_semana_total,'bytes')
        # media diaria de consumo de dados de cada aplicativo
        print ('a media diaria de dados usados do chrome foi', media_diaria_semana_chrome,'bytes')
        print ('a media diaria de dados usados do facebook foi', media_diaria_semana_facebook,'bytes')
        print ('a media diaria de dados usados do instagram foi', media_diaria_semana_instagram,'bytes') 
        print ('a media diaria de dados usados do whatsapp foi', media_diaria_semana_whatsapp,'bytes') 
        print ('a media diaria de dados usados do outros foi', media_diaria_semana_outros,'bytes') 



