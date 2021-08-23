# import pywhatkit
from selenium import webdriver
from goto import with_goto
import time
import datetime
# pywhatkit.sendwhatmsg_instantly('+917979815545','Hello saurav nice to meet you')

whatsapp = webdriver.Chrome()
whatsapp.get("https://web.whatsapp.com")


def new_msg():
    print("checking new message")
    try:
        print("please wait ...")
        time.sleep(2)
        msg_notif = whatsapp.find_element_by_css_selector("span[class='_23LrM']")

        if msg_notif.text:
            print("Message found")
            msg_notif.click()
            search_msg = whatsapp.find_elements_by_css_selector("._1Gy50")
            print(search_msg)
            for msg in search_msg:
                last_msg = msg.text
                print(last_msg)
            return last_msg
    except Exception as error:
        print(error)
        print("there is No message yet")
        time.sleep(2)
        return False


def bot_reply(user_msg): 
    respond = {
    "hi":"Hello! ",
    "fine":"good",
    "good morning":"Good Morning you too",
    "where are you":"I am in jamshedpur",
    "hnji":"ok",
    "hi saurav":"hi Buddy",
    "how are you":"I am fine. And you",
    "good evening":"Good evening you too",
    "good night":"Good night. And Sweet dream",
    "by":"By By..... We will meet soon.",
    "are you there":"Ya I am still live",
    "nice":"Thank you",
    }
    enter_msg_xpath = "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]"
    type_msg = whatsapp.find_element_by_xpath(enter_msg_xpath)
    print(user_msg,respond.keys())
    if user_msg.lower() in respond.keys():
        print("keys found")
        type_msg.send_keys(respond[user_msg.lower()])
        print("sending message ......")
        button_xpath = "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]/button"
        button_send = whatsapp.find_element_by_xpath(button_xpath)
        button_send.click()
        other_user = whatsapp.find_elements_by_css_selector(".zoWT4")
        other_user[0].click()
    else:
        print("keys not found")
        type_msg.send_keys("Admin will contact you soon for this question")
        print("sending message ......")
        button_xpath = "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]/button"
        button_send = whatsapp.find_element_by_xpath(button_xpath)
        button_send.click()
        with open("whatsappLog.txt","a+") as file:
            file.write(f"\n-------------\n Date :- {datetime.datetime.today()}\n Question was :- {user_msg} ")
            file.close()


if __name__=='__main__':
    input("Scan the QR code and hit any key to continue ")
    count = 1
    while(count == 1):
        user_msg = new_msg()
        if user_msg != False:
            print("bot is sending message")
            bot_reply(user_msg)

        time.sleep(2)
  
    

