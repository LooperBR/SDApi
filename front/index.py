import requests
while(1==1):
    entrada = int(input("1-asdf\n2-fjgjdfsfdhjsd\n3-sair\n"))

    if(entrada==3):
        break
    elif(entrada==1):
        valor = 'asdf'
        teste = requests.get('http://127.0.0.1:5000')
        print(teste)
        print(valor)
    elif(entrada==2):
        valor='fjgjdfsfdhjsd'
        print(valor)


