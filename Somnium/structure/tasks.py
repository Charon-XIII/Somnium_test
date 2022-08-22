from Somnium.celery import app
from django.core.mail import EmailMessage
from .models import Person

@app.task(bind=True)
def send_notice(self, task_info):
    person = Person.objects.get(id=task_info['person'])
    email = EmailMessage(
            f"Задача №{task_info['id']}", 
            """
            <html>
              <head></head>
              <body>
                <h1 style="margin: 0;">Уважаемый(-ая), {0}</h1>
                <h2 style="margin: 0;">Вам необходимо выполнить следующее:</h2>
                <p style="margin: 0;">{1}</p>
                <br>
                <br>
                <p style="margin: 0;">Дата и время начала задачи: {2}</p>
                <p style="margin: 0;">Дата и время окончания задачи: {3}</p>
              </body>
            </html>
            """.format(person.fullname, task_info['description'], str(task_info['date_start']), str(task_info['date_finish'])), 'testuzver01@yandex.kz', [person.email])
    email.content_subtype = "html"
    email.send()

