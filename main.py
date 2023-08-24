from instabot import Bot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import imaplib
import email
import smtplib
import time
import openai
import re

#-------------------------------------------------------------------------THIS IS FOR INSTAGRAM BOT---------------------------------------------------------------------------------------------------------------------
bot = Bot()
bot.login(username="aiautomationtest", password="thisiscoolautomationxd")

users = bot.search_users("fitness coach")
print(len(users))

for id in users:
    user_info = bot.get_user_info(id)
    username = user_info['username']
    website = user_info.get('external_url', 'No website available')  # Use a default value if website is not provided

    print(f"Username: {username}")
    print(f"Website: {website}")

#------------------------------------------THIS IS FOR SUBSCRIBING TO NEWS LETTER---------------------------------------------------------------------------
driver = webdriver.Chrome()

# ***********WRITE THE WEBSITE YOU WANT TO AUTOMATICALLY SUBSCRIBE EMAIL TO
driver.get("https://fionasimpsonscoaching.co.uk/")

email_input = driver.execute_script("""
    var inputs = document.querySelectorAll("input");

    for (var i = 0; i < inputs.length; i++) {
        var inputType = inputs[i].getAttribute("type");
        var inputName = inputs[i].getAttribute("name");
        var inputPlaceholder = inputs[i].getAttribute("placeholder");
        var inputAutocomplete = inputs[i].getAttribute("autocomplete");

        if ((inputType && inputType.toLowerCase() === "email") ||
            (inputName && inputName.toLowerCase().includes("email")) ||
            (inputPlaceholder && inputPlaceholder.toLowerCase().includes("email")) ||
            (inputAutocomplete && inputAutocomplete === "email")) {
            return inputs[i];
        }
    }

    return null;

""")


if email_input:
    email_input.send_keys("redmagic8propljustransformers@gmail.com")
    parent_form = email_input.find_element(By.XPATH, "./ancestor::form")
    parent_form.submit()
    time.sleep(10)
else:
    print("EMAIL LIST NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT AVVVVVVVVVVVVVVVVVVVVVVVVAAAIIIIIIIIIIIIIIIIIIIIIIIILLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBLE")

driver.quit()
# ----------------------------------------------------------THIS FOR EMAIL AUTOMATION--------------------------------------------------------------------------------------

openai.api_key=""

imap_server = ""
username = ""
password = ""


# SMTP settings
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = ""
smtp_password = ""

def get_text_content(part):
    if part.is_multipart():
        text_content = ""
        for subpart in part.get_payload():
            text_content += get_text_content(subpart)
        return text_content
    else:
        return part.get_payload()

def extract_text_before_html(content):
    index = content.find("<html>")
    if index != -1:
        return content[:index]
    return content

while True:
    try:
        print("test")
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        mail.select("inbox")

        status, email_ids = mail.search(None, "UNSEEN")

        for email_id in email_ids[0].split():
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            email_content = get_text_content(msg)

            html_tag_pattern = r"<.*?>"

            match = re.search(html_tag_pattern, email_content)
            if match:
                index = match.start()
                email_content = email_content[:index]
            else:
                email_content = email_content

            prompt = f"Given the following newsletter content:\n\n{email_content}\n\nPlease provide suggestions on how to improve it."
            prompt2 = f"Generate a personalized compliment using {email_content}. Make it short"

            response = openai.Completion.create(
                engine="davinci",  # Choose the appropriate engine
                prompt=prompt,
                max_tokens=50  # Adjust as needed
            )

            response2 = openai.Completion.create(
                engine="davinci",  # Choose the appropriate engine
                prompt=prompt2,
                max_tokens=10  # Adjust as needed
            )

            improvement_suggestions = response.choices[0].text.strip()
            compliment = response2.choices[0].text.strip()

            print("Improvement Suggestions:")
            print(improvement_suggestions)

            print("Compliment:")
            print(compliment)

            print(f"Content: {email_content}")

            response_subject = "Re: Newsletter"
            response_msg = f"Hi \n\n, {compliment} but I saw that there were some mistakes and things that could be improved for example {improvement_suggestions} so I would like to offer you an opportunity to partner with me I will increase your sales, help make your newsletter better, if that's something you would be intrested in please message me on whatsapp 07405187555 or Reply to this email"

            # response_msg = f"Subject: COOL AUTOMATION\n\n{email_content} \n IMPROVED VERSION: \n ****NEED CHATGPT API KEY FOR THIS"

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, msg["From"], response_msg)

            mail.store(email_id, '+FLAGS', '\Seen')

        mail.logout()

    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(10)

# can get textbox input type - email or
#1) I want to find a fitness coach with a newletter in his website. 2) Then I want to find way to go in the newsletter and get his latest and copy the text 3) Then use gpt3 to make it better according to what he said
# can find email list by ctrl f "email list" "mail" "newsletter"
# EDGE CASE: Wants to click then automatically do but might do same person twice. Can add the id somewhere when he clicks it(maybe another file or same)then when clicks it again has to check if id is already in file if it is then do again
