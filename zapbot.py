from selenium import webdriver
import time

class whatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia pessoal veja pessoal. Deus abençoe grandemente mais um dia a todos voces: Veja a mensagem de hoje: "
        self.Usuarios = ["Mor","Ricardo"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        
    def EnviarMensagens(self):       
             self.driver.get('https://web.whatsapp.com')
             time.sleep(30)
             for users in self.Usuarios:
                 users = self.driver.find_element_by_xpath(f"//span[@title='{users}']")
                 time.sleep(3)
                 users.click()
                 chat_box = self.driver.find_element_by_class_name('p3_M1')
                 time.sleep(3)
                 chat_box.click()
                 chat_box.send_keys(self.mensagem)
                 botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                 time.sleep(3)
                 botao_enviar.click()
                 time.sleep(3)
bot =  whatsappBot()
bot.EnviarMensagens()

# https://www.youtube.com/watch?v=ISYHWfWvp3E