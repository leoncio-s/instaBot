#! /bin/python3 
__name__   = 'insta-Boot'
__version__= "2.0.0"
__author__ = "Leôncio Souza"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


#  Inicia o webdriver do firefox
driver = webdriver.Firefox()

class Boot():
    def __init__(self, url, user, passwd ):
        self.url = url          # Url da página que vai comentar
        self.username = user    # Username, telefone ou email de acesso ao instagram
        self.password = passwd  # Senha

        # WebDriver abre a URL da página do instagram
        sleep(1)
        driver.get("https://www.instagram.com")

    def login(self):
        try:
            error = bool(driver.find_element_by_xpath("//div[@class='eiCW']"))
            if error == True:
                driver.close()
                print("\033[1;31m", "Erro no Login", "\033[m")
        except Exception:
            # Procura o elemento de para inserir o nome de usuário e a senha
            driver.find_element_by_css_selector("input[name='username']").send_keys(self.username)
            driver.find_element_by_css_selector("input[name='password']").send_keys(self.password)
            
            # Procura o botão de envio dos dados de login
            self.button   = driver.find_element_by_xpath("//button[@type='submit']")

            #Espera 1 segundo e clica no botão para logar no site
            sleep(1)
            self.button.click()
            
            #Espera 5 segundos porque aparece um pop-up pedindo para salvar os dados de login
            sleep(5)
            return print("\033[1;32m", "Login OK", "\033[1;m")

    def iniBoot(self):
        
        sleep(1)
        try:
            self.login()
            #Volta para uma página anterir para se livrar do pop-up
            driver.get(self.url)

            sleep(5)
            
            return print("\033[1;32m", 'OK', "\033[1;m")
            
        #Se não conseguir fazer o login gera uma excessão e fecha o navegador
        except Exception:
            driver.close()
            return print("\033[1;31m", 'FAIL', "\033[1;m")



    def comments(self, comment):
        sleep(4)
        try:
            # Se encontrar o bloqueador de comentário aguarda por 60 segundos e recarrega a página
            if (driver.find_element_by_xpath("//p[@class='gxNyb']")):
                sleep(60)
                driver.navigate().refresh()
                return print("\033[1;41m", 'Sleeping', "\033[1;m")

        except:    
            sleep(1)
            
            try:
                # Procura o campo de comentário e dá um click nele
                driver.find_element_by_xpath("//form/textarea[@class='Ypffh']").click()
                sleep(1)

                # Procura o campo de comentário já clicado e armazena em uma variavel
                self.textarea = driver.find_element_by_xpath("//form/textarea[@class='Ypffh focus-visible']")

                # Script js para inserir um valor em branco no campo de comentário
                self.js = "arguments[0].value = '';"

                # O navegador executa o script js no campo de comentário
                driver.execute_script(self.js, self.textarea)

                # Insere o valor texto escolhido dentro do campo de comentário e faz o envio
                self.textarea.send_keys(comment, Keys.ENTER)
                
                return print("\033[1;32m", 'OK', "\033[1;m")
            except Exception:
                return print("\033[1;31m", 'Falha no comentário', "\033[1;m")

    def close(self):
        driver.close()
        return print("\033[1;42m", 'Fecha Navegador', "\033[1;m")