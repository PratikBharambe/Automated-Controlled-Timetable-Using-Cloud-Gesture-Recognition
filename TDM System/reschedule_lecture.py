from supabase import create_client
import random
import datetime
from email.message import EmailMessage
import ssl
import smtplib

url = "https://ctbocdqgvhimayeqvqov.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN0Ym9jZHFndmhpbWF5ZXF2cW92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDYzNjQ1MzEsImV4cCI6MjAyMTk0MDUzMX0.HHOqs4_KujahCS_V60CsKWjb0ky4UTO2qQNzdyV0sdU"
supabase = create_client(url, key)


def send_mail(email_receiver, body):
    email_sender = "bharambepratik2002@gmail.com"
    email_password = "yhexjdsegqiforwq"
    now = datetime.datetime.now()
    if now.hour == 11:
        subject = "Practical Reschedule Information"
    else:
        subject = "Lecture Reschedule Information"
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        msg = em.as_string()
        smtp.sendmail(email_sender, email_receiver, msg)
        print("Mail sent to : ", email_receiver)


def generate_message_and_send_mail_for_faculty(subject):
    now = datetime.datetime.now()
    minute = now.minute + 10
    response = supabase.table("faculty_data").select("name", "mail").eq("subject", subject).execute()
    for data in response.data:
        name = data["name"]
        mail = data["mail"]
        if now.hour == 11:
            message = "Hello " + name + ", \nYou have practical scheduled at time " + str(now.hour) + " : " + str(
                minute) + " on BE E&TC Class for " + subject + (" subject.\nSo it's a humble request to report on time "
                                                                "on the respective lab.")
            send_mail(mail, message)
        else:
            message = "Hello " + name + ", \nYou have lecture scheduled at time " + str(now.hour) + " : " + str(
                minute) + " on BE E&TC Class for " + subject + (" subject.\nSo it's a humble request to report on time "
                                                                "on the respective classroom.")
            send_mail(mail, message)


def get_subject_name(name):
    response = supabase.table('faculty_data').select('subject').eq('name', name).execute()
    subject = ""
    for item in response.data:
        subject = item['subject']
    return subject


def get_subject_name_list():
    response = supabase.table('faculty_data').select("subject").execute()
    subject_list = []
    for subject in response.data:
        subject_list.append(subject['subject'])
    return subject_list


def update_is_rescheduled_status():
    current_date = datetime.date.today()
    current_day = current_date.strftime("%A")
    response = supabase.table('be_tt').select(current_day, "id", "is_rescheduled").execute()
    reschedule_response = supabase.table("reschedule_data").select("rescheduling", "rescheduled").execute()
    rescheduling_subject = ""
    for sub in reschedule_response.data:
        rescheduling_subject = sub["rescheduling"]

    for items in response.data:
        if items[current_day] == rescheduling_subject:
            supabase.table("be_tt").update({"is_rescheduled": True}).eq("id", items["id"]).execute()


def initialize_reshedule_algorithm(faculty_name):
    subject = get_subject_name(faculty_name)
    subject_list = get_subject_name_list()
    subject_list.remove(subject)
    resheduled_lecture_name = random.choice(subject_list)

    supabase.table("reschedule_data").update({"rescheduling": subject, "rescheduled": resheduled_lecture_name}).eq("id", 1).execute()
    update_is_rescheduled_status()
    generate_message_and_send_mail_for_faculty(resheduled_lecture_name)

