import time
import threading
import os
import pyzipper

global attempt, caracteres, stop, time1, password, password2, thread, caminho_zip, pasta_destino, senhas
senha = 0
stop = True
attempt = 0
caracteres = ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop_password = threading.Event()

def arquivo_quebrado(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        print("Arquivo descompactado com sucesso!")
        senhas = 1
        stop = False
        stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True   
              
def arquivo_quebrado2(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        print("Arquivo descompactado com sucesso!")
        senhas = 2
        stop = False
        stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True   
        
def sep1():
    global attempt, caracteres, stop, password, caminho_zip, pasta_destino
    a = 0
    b = 0
    c = 0
    d = 0
    z = 0
    while not stop_password.is_set():
        password = caracteres[a] + caracteres[b] + caracteres[c] + caracteres[d] + caracteres[z]
        arquivo_quebrado(password)
        attempt += 1
        a += 1
        if a == 36:
            b += 1
            a = 0
        if b == 36:
            c += 1
            b = 0
        if c == 36:
            c = 0
            d += 1   
        if d == 36:
            d = 0
            z += 1
        if z == 16:
            print("senha não encontrada")
            stop = False
            yes = False
            break

def sep2():
    global attempt, caracteres, stop, password2, caminho_zip, pasta_destino2
    f = 36
    g = 36
    h = 36
    i = 36
    j = 36
    while not stop_password.is_set():
        password2 = caracteres[f] + caracteres[g] + caracteres[h] + caracteres[i] + caracteres[j]
        arquivo_quebrado2(password2)  
        attempt += 1
        j = j - 1
        if j == -1:
             i = i- 1
             j = 36
        if i == -1:
             h = h - 1
             i = 36
        if h == -1:
             g = g - 1
             h = 36
        if g == -1:
             g = 36
             f = f - 1
        if f == -1:    
             print("senha não encontrada")
             break 
             
print("")            
print("BEM VINDO AO QUEBRADOR DE SENHA DE ARQUIVOS ZIP")          
print("Versão: 1.0")            
print("Em próximas versões, o maiores otimizações serão feitas")
print("O uso desse script é destinado apenas para fins educacionais,")
print("ou caso tenha esquecido a senha de SEU arquivo.")
caminho_zip = input('Insira o nome do arquivo (com a extensão dele) >>> ')
if " " in caminho_zip:
    print("O nome do arquivo não pode conter espaços, remova-os")
    exit("Algum erro ocorreu. Encerrado o programa...")
if not (".zip" in caminho_zip or ".7z" in caminho_zip):
    print("Isso não é um arquivo .zip ou .7z")
    exit("Algum erro ocorreu. Encerrado o programa...")
print("Insira o nome da pasta para onde irão os arquivos descompactados")
pasta_destino = input('caso a pasta não for encontrada, o sistema criará uma pasta \ncom o nome específicado >>>  ')

thread1 = threading.Thread(target=sep1)
thread2 = threading.Thread(target=sep2)

print("64364 de combinações estão sendo testadas por minuto.")
time.sleep(0.3)
print("OBS: O tempo para testar todas as combinações possíveis")
print("é de aproximadamente 4 horas (no máximo) dependendo da senha")
time.sleep(0.3)
print("Ferramenta iniciada com sucesso :D")
time.sleep(0.3)
print("Por favor aguarde...")

thread1.start()           
thread2.start() 

time1 = time.time()

thread1.join()
thread2.join()

time2 = time.time() 
time3 = time2 - time1

time.sleep(2)
os.system('clear') or None
if senhas == 1:
    print(f"A senha do arquivo é: {password}")
elif senhas == 2:
    print(f"A senha do arquivo é: {password2}")    
else:
    print("Não foi possível encontrar a senha :(")
    
if time3 < 1.5:
    print("Tempo de execução: instantâneo")
else:
    print(f"Tempo de execução: {time3:.3f} segundos")
    
print(f"Quantidade de tentativas: {attempt}")
print("A senha do arquivo foi quebrada com sucesso!!!")



#ass: JVLEGEND