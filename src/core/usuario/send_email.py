from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send(worker, link):
    link = f'http://localhost:8000/worker/{link}/'
    subject = 'Verifique se esse usuario é um Funcionário'


    html_render = render_to_string('worker_email.html', {
        "worker": worker,
        'link': link
    })

    email_multi_alternative = EmailMultiAlternatives(
        subject,
        from_email=settings.EMAIL_HOST_USER,
        to=[worker.user.email]
    )

    email_multi_alternative.attach_alternative(html_render, 'text/html')
    email_multi_alternative.send()

    print(f'email enviado para {worker.user.email}')




    