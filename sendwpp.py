from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
       self.mensagem = "Deu certooooooo" 
       self.grupos = ["GrupoA","Grupo2","Grupo3","Grupo4","Grupo5","Grupo6","Grupo7","Grupo8","Grupo9","Grupo10"]
       options = webdriver.ChromeOptions()
       options.add_argument('lang=pt-br')
       self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="Grupo da galera" class="_3ko75 _5h6Y_ _3Whw5">Grupo da galera</span>
        #<div tabindex="-1" class="_3uMse">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
       
bot = WhatsappBot()
bot.EnviarMensagens()


#<span dir="auto" title="Grupo da galera" class="_3ko75 _5h6Y_ _3Whw5"><span class="matched-text _3Whw5">Grupo</span> da galera</span>

#<div tabindex="-1" class="_3uMse">

#<span data-testid="send" data-icon="send" class="">