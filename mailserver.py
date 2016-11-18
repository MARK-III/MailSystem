
import smtpd
import dns.resolver
import asyncore
import smtplib
import email.utils
from email.mime.text import MIMEText

class CustomSMTPClient():

    @staticmethod
    def send_to_gmail(mailfrom, rcpttos, data):

        username = ''
        password = ''
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        #server.set_debuglevel(True) # show communication with the server
        try:
            server.sendmail(mailfrom, ['xjq314@gmail.com'] , data)
        finally:
            server.quit()

    @staticmethod
    def send_to_qq(mailfrom, rcpttos, data):

        domain = 'qq.com'
        mail_via = 'xjq_314@qq.com'
        mx_group =  dns.resolver.query(domain, 'MX')
        mx_major = mx_group[0].to_text()
        mx = mx_major[mx_major.index(' ') + 1 :]
        server = smtplib.SMTP(mx, 25)
        #server.set_debuglevel(True) # show communication with the server
        try:
            server.sendmail('forward@xjq314.com', [mail_via], data)
        finally:
            server.quit()


class CustomSMTPServer(smtpd.SMTPServer):


    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))
        #print('Message content :')
        #print(data)

        receiver_0 = rcpttos[0]
        receiver_0_domain = receiver_0[receiver_0.find('@')+1:]

        if receiver_0_domain == 'xjq314.com':
            CustomSMTPClient.send_to_qq(mailfrom, rcpttos, data)

        else:
            print('ignore mail')

        return

server = CustomSMTPServer(('0.0.0.0', 25), None)

asyncore.loop()

