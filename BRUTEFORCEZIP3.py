import time
import threading
import os
import pyzipper

global attempt, caracteres, stop, time1, password, password2, password3, password4, thread, caminho_zip, pasta_destino, senhas
senhas = None
stop = True
attempt = 0
caracteres = ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop_password = threading.Event()
lock = threading.Lock()

def arquivo_quebrado(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        with lock:    
          if not stop_password.is_set():  
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
        with lock:    
          if not stop_password.is_set():  
            print("Arquivo descompactado com sucesso!")
            senhas = 2
            stop = False
            stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True   
        
def arquivo_quebrado3(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        with lock:
          if not stop_password.is_set():      
            print("Arquivo descompactado com sucesso!")
            senhas = 3
            stop = False
            stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True           
        
def arquivo_quebrado4(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        with lock:
          if not stop_password.is_set():      
            print("Arquivo descompactado com sucesso!")
            senhas = 4
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
    e = 0
    while not stop_password.is_set():
        password = caracteres[a] + caracteres[b] + caracteres[c] + caracteres[d] + caracteres[e]
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
            e += 1
        if e == 16:
            print("senha não encontrada")
            stop = False
            yes = False
            break

def sep1_5():
    global attempt, caracteres, stop, password3, caminho_zip
    k = 17
    l = 36
    m = 36
    n = 36
    o = 36
    while not stop_password.is_set():
        password3 = caracteres[k] + caracteres[l] + caracteres[m] + caracteres[n] + caracteres[o]
        arquivo_quebrado3(password3)  
        attempt += 1
        o = o - 1
        if o == -1:
             n = n - 1
             o = 36
        if n == -1:
             m = m - 1
             n = 36
        if m == -1:
             l = l - 1
             m = 36
        if l == -1:
             l = 36
             k = k - 1
        if k == -1:    
             print("senha não encontrada")
             break 
             
def sep5_2():
    global attempt, caracteres, stop, password4, caminho_zip, pasta_destino
    a = 18
    b = 1
    c = 1
    d = 1
    e = 1
    while not stop_password.is_set():
        password4 = caracteres[a] + caracteres[b] + caracteres[c] + caracteres[d] + caracteres[e]
        arquivo_quebrado4(password4)
        attempt += 1
        a += 1
        if a == 36:
            b += 1
            a = 1
        if b == 36:
            c += 1
            b = 1
        if c == 36:
            c = 1
            d += 1   
        if d == 36:
            d = 1
            e += 1
        if e == 16:
            print("senha não encontrada")
            stop = False
            yes = False
            break

def sep2():
    global attempt, caracteres, stop, password2, caminho_zip
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
print("Versão: 3.0")            
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
thread3 = threading.Thread(target=sep1_5)
thread4 = threading.Thread(target=sep5_2)

print("128000 combinações estão sendo testadas por minuto.")
time.sleep(0.3)
print("OBS: O tempo para testar todas as combinações possíveis")
print("é de aproximadamente 2 horas (no máximo) dependendo da senha")
time.sleep(0.3)
print("Ferramenta iniciada com sucesso :D")
time.sleep(0.3)
print("Por favor aguarde...")

thread1.start()           
thread2.start() 
thread3.start()           
thread4.start() 

time1 = time.time()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time2 = time.time() 
time3 = time2 - time1

time.sleep(2)
os.system('clear') or None
print(f"Thread que achou a senha: {senhas} (Caso não saiba \n o que")
print("isso significa, apenas ignore)")
if senhas == 1:
    print(f"A senha do arquivo é: {password}")
elif senhas == 2:
    print(f"A senha do arquivo é: {password2}")#funciona
elif senhas == 3:
    print(f"A senha do arquivo é: {password3}")
elif senhas == 4:
    print(f"A senha do arquivo é: {password4}")#funciona         
else:
    print("Não foi possível encontrar a senha :(")
    
if time3 < 1.5:
    print("Tempo de execução: instantâneo")
else:
    print(f"Tempo de execução: {time3:.3f} segundos")
    
print(f"Quantidade de tentativas: {attempt}")
print("A senha do arquivo foi quebrada com sucesso!!!")


#ass: JVLEGEND