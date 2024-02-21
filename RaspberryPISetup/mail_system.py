
import datetime
import time
import threading
from email.message import EmailMessage
import ssl
import smtplib
from supabase import create_client


url = "https://ctbocdqgvhimayeqvqov.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN0Ym9jZHFndmhpbWF5ZXF2cW92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDYzNjQ1MzEsImV4cCI6MjAyMTk0MDUzMX0.HHOqs4_KujahCS_V60CsKWjb0ky4UTO2qQNzdyV0sdU"
supabase = create_client(url, key)

def sendMail(email_receiver, body):
    email_sender = "bharambepratik2002@gmail.com"
    email_password = "yhexjdsegqiforwq"
    now = datetime.datetime.now()
    if (now.hour == 11):
        subject = "Practical scheduled REMAINDER"
    else:
        subject = "Lecture scheduled REMAINDER"
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


def generate_Message_And_send_Mail_for_faculty(subjects):
    now = datetime.datetime.now()
    minute = now.minute + 10
    for subject in subjects:
        response = supabase.table("faculty_data").select("name", "mail").eq("subject", subject).execute()
        for data in response.data:
            name = data["name"]
            mail = data["mail"]
            if (now.hour == 11):
                message = "Hello " + name + ", \nYou have pratical scheduled at time " + str(now.hour) + " : " + str(minute) + " on BE E&TC Class for " + subject + " subject.\nSo it's a humble request to report on time on the respetive lab."
                sendMail(mail, message)
            else:
                message = "Hello " + name + ", \nYou have lecture scheduled at time " + str(now.hour) + " : " + str(minute) + " on BE E&TC Class for " + subject + " subject.\nSo it's a humble request to report on time on the respetive classroom."
                sendMail(mail, message)


def send_mail_to_rescheduled_faculty():
    print("send_mail_to_rescheduled_faculty")
    rescheduling_response = supabase.table("reschedule_data").select("rescheduled").execute()
    mail_sendding_subject = ""
    for item in rescheduling_response.data:
        mail_sendding_subject = item["rescheduled"]
    subject = [mail_sendding_subject]
    return subject


def set_default_values_in_rescheduling_system():
    response = supabase.table('be_tt').select("id").eq("is_rescheduled", True).execute()
    for items in response.data:
        supabase.table("be_tt").update({"is_rescheduled": False}).eq("id", items["id"]).execute()


def if_true_send_mail_to_rescheduled_faculty(id):
    is_rescheduled_response = supabase.table("be_tt").select("is_rescheduled").eq("id", id).execute()
    is_rescheduled = ""
    for item in is_rescheduled_response.data:
        is_rescheduled = item["is_rescheduled"]
    return is_rescheduled


def send_mail_rescheduled():
    list_of_subject = send_mail_to_rescheduled_faculty()
    generate_Message_And_send_Mail_for_faculty(list_of_subject)


# function to follow monday schedule ....................
def mondaySchedule():
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(1):
                send_mail_rescheduled()
            else:
                m1 = supabase.table("be_tt").select("monday").eq("id", 1).execute()
                m1_sub_list = []
                for subject in m1.data:
                    m1_sub_list.append(subject["monday"])
                generate_Message_And_send_Mail_for_faculty(m1_sub_list)
                time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(2):
                send_mail_rescheduled()
            else:
                m2 = supabase.table("be_tt").select("monday").eq("id", 2).execute()
                m2_sub_list = []
                for subject in m2.data:
                    m2_sub_list.append(subject["monday"])
                generate_Message_And_send_Mail_for_faculty(m2_sub_list)
                time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if if_true_send_mail_to_rescheduled_faculty(4) or if_true_send_mail_to_rescheduled_faculty(5) or if_true_send_mail_to_rescheduled_faculty(6):
                send_mail_rescheduled()
            else:
                m41 = supabase.table("be_tt").select("monday").eq("id", 4).execute()
                m42 = supabase.table("be_tt").select("monday").eq("id", 5).execute()
                m43 = supabase.table("be_tt").select("monday").eq("id", 6).execute()
                m4_sub_list = []
                for subject in m41.data:
                    m4_sub_list.append(subject["monday"])
                for subject in m42.data:
                    m4_sub_list.append(subject["monday"])
                for subject in m43.data:
                    m4_sub_list.append(subject["monday"])
                generate_Message_And_send_Mail_for_faculty(m4_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(8):
                send_mail_rescheduled()
            else:
                m6 = supabase.table("be_tt").select("monday").eq("id", 8).execute()
                m6_sub_list = []
                for subject in m6.data:
                    m6_sub_list.append(subject["monday"])
                generate_Message_And_send_Mail_for_faculty(m6_sub_list)
                time.sleep(60)

        elif now.hour == 15 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(9):
                send_mail_rescheduled()
            else:
                m7 = supabase.table("be_tt").select("monday").eq("id", 9).execute()
                m7_sub_list = []
                for subject in m7.data:
                    m7_sub_list.append(subject["monday"])
                generate_Message_And_send_Mail_for_faculty(m7_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 0:
            set_default_values_in_rescheduling_system()
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to follow tuesday schedule ...................
def tuesdaySchedule():
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(1):
                send_mail_rescheduled()
            else:
                tu1 = supabase.table("be_tt").select("tuesday").eq("id", 1).execute()
                tu1_sub_list = []
                for subject in tu1.data:
                    tu1_sub_list.append(subject["tuesday"])
                generate_Message_And_send_Mail_for_faculty(tu1_sub_list)
                time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(2):
                send_mail_rescheduled()
            else:
                tu2 = supabase.table("be_tt").select("tuesday").eq("id", 2).execute()
                tu2_sub_list = []
                for subject in tu2.data:
                    tu2_sub_list.append(subject["tuesday"])
                generate_Message_And_send_Mail_for_faculty(tu2_sub_list)
                time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if if_true_send_mail_to_rescheduled_faculty(4) or if_true_send_mail_to_rescheduled_faculty(5) or if_true_send_mail_to_rescheduled_faculty(6):
                send_mail_rescheduled()
            else:
                tu41 = supabase.table("be_tt").select("tuesday").eq("id", 4).execute()
                tu42 = supabase.table("be_tt").select("tuesday").eq("id", 5).execute()
                tu43 = supabase.table("be_tt").select("tuesday").eq("id", 6).execute()
                tu4_sub_list = []
                for subject in tu41.data:
                    tu4_sub_list.append(subject["tuesday"])
                for subject in tu42.data:
                    tu4_sub_list.append(subject["tuesday"])
                for subject in tu43.data:
                    tu4_sub_list.append(subject["tuesday"])
                generate_Message_And_send_Mail_for_faculty(tu4_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(8):
                send_mail_rescheduled()
            else:
                tu6 = supabase.table("be_tt").select("tuesday").eq("id", 8).execute()
                tu6_sub_list = []
                for subject in tu6.data:
                    tu6_sub_list.append(subject["tuesday"])
                generate_Message_And_send_Mail_for_faculty(tu6_sub_list)
                time.sleep(60)

        elif now.hour == 15 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(9):
                send_mail_rescheduled()
            else:
                tu7 = supabase.table("be_tt").select("tuesday").eq("id", 9).execute()
                tu7_sub_list = []
                for subject in tu7.data:
                    tu7_sub_list.append(subject["tuesday"])
                generate_Message_And_send_Mail_for_faculty(tu7_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 0:
            set_default_values_in_rescheduling_system()
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to follow wednesday schedule .................
def wednesdaySchedule():
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(1):
                send_mail_rescheduled()
            else:
                w1 = supabase.table("be_tt").select("wednesday").eq("id", 1).execute()
                w1_sub_list = []
                for subject in w1.data:
                    w1_sub_list.append(subject["wednesday"])
                generate_Message_And_send_Mail_for_faculty(w1_sub_list)
                time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(2):
                send_mail_rescheduled()
            else:
                w2 = supabase.table("be_tt").select("wednesday").eq("id", 2).execute()
                w2_sub_list = []
                for subject in w2.data:
                    w2_sub_list.append(subject["wednesday"])
                generate_Message_And_send_Mail_for_faculty(w2_sub_list)
                time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if if_true_send_mail_to_rescheduled_faculty(4) or if_true_send_mail_to_rescheduled_faculty(5) or if_true_send_mail_to_rescheduled_faculty(6):
                send_mail_rescheduled()
            else:
                w41 = supabase.table("be_tt").select("wednesday").eq("id", 4).execute()
                w42 = supabase.table("be_tt").select("wednesday").eq("id", 5).execute()
                w43 = supabase.table("be_tt").select("wednesday").eq("id", 6).execute()
                w4_sub_list = []
                for subject in w41.data:
                    w4_sub_list.append(subject["wednesday"])
                for subject in w42.data:
                    w4_sub_list.append(subject["wednesday"])
                for subject in w43.data:
                    w4_sub_list.append(subject["wednesday"])
                generate_Message_And_send_Mail_for_faculty(w4_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(8):
                send_mail_rescheduled()
            else:
                w6 = supabase.table("be_tt").select("wednesday").eq("id", 8).execute()
                w6_sub_list = []
                for subject in w6.data:
                    w6_sub_list.append(subject["wednesday"])
                generate_Message_And_send_Mail_for_faculty(w6_sub_list)
                time.sleep(60)

        elif now.hour == 15 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(9):
                send_mail_rescheduled()
            else:
                w7 = supabase.table("be_tt").select("wednesday").eq("id", 9).execute()
                w7_sub_list = []
                for subject in w7.data:
                    w7_sub_list.append(subject["wednesday"])
                generate_Message_And_send_Mail_for_faculty(w7_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 0:
            set_default_values_in_rescheduling_system()
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to follow thursday schedule .................
def thursdaySchedule():
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(1):
                send_mail_rescheduled()
            else:
                th1 = supabase.table("be_tt").select("thursday").eq("id", 1).execute()
                th1_sub_list = []
                for subject in th1.data:
                    th1_sub_list.append(subject["thursday"])
                generate_Message_And_send_Mail_for_faculty(th1_sub_list)
                time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(2):
                send_mail_rescheduled()
            else:
                th2 = supabase.table("be_tt").select("thursday").eq("id", 2).execute()
                th2_sub_list = []
                for subject in th2.data:
                    th2_sub_list.append(subject["wednesday"])
                generate_Message_And_send_Mail_for_faculty(th2_sub_list)
                time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if if_true_send_mail_to_rescheduled_faculty(4) or if_true_send_mail_to_rescheduled_faculty(5) or if_true_send_mail_to_rescheduled_faculty(6):
                send_mail_rescheduled()
            else:
                th41 = supabase.table("be_tt").select("thursday").eq("id", 4).execute()
                th42 = supabase.table("be_tt").select("thursday").eq("id", 5).execute()
                th43 = supabase.table("be_tt").select("thursday").eq("id", 6).execute()
                th4_sub_list = []
                for subject in th41.data:
                    th4_sub_list.append(subject["thursday"])
                for subject in th42.data:
                    th4_sub_list.append(subject["thursday"])
                for subject in th43.data:
                    th4_sub_list.append(subject["thursday"])
                generate_Message_And_send_Mail_for_faculty(th4_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(8):
                send_mail_rescheduled()
            else:
                th6 = supabase.table("be_tt").select("thursday").eq("id", 8).execute()
                th6_sub_list = []
                for subject in th6.data:
                    th6_sub_list.append(subject["thursday"])
                generate_Message_And_send_Mail_for_faculty(th6_sub_list)
                time.sleep(60)

        elif now.hour == 15 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(9):
                send_mail_rescheduled()
            else:
                th7 = supabase.table("be_tt").select("thursday").eq("id", 9).execute()
                th7_sub_list = []
                for subject in th7.data:
                    th7_sub_list.append(subject["thursday"])
                generate_Message_And_send_Mail_for_faculty(th7_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 0:
            set_default_values_in_rescheduling_system()
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to follow friday schedule..................
def fridaySchedule():
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(1):
                send_mail_rescheduled()
            else:
                f1 = supabase.table("be_tt").select("friday").eq("id", 1).execute()
                f1_sub_list = []
                for subject in f1.data:
                    f1_sub_list.append(subject["friday"])
                generate_Message_And_send_Mail_for_faculty(f1_sub_list)
                time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(2):
                send_mail_rescheduled()
            else:
                f2 = supabase.table("be_tt").select("friday").eq("id", 2).execute()
                f2_sub_list = []
                for subject in f2.data:
                    f2_sub_list.append(subject["friday"])
                generate_Message_And_send_Mail_for_faculty(f2_sub_list)
                time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if if_true_send_mail_to_rescheduled_faculty(4) or if_true_send_mail_to_rescheduled_faculty(5) or if_true_send_mail_to_rescheduled_faculty(6):
                send_mail_rescheduled()
            else:
                f41 = supabase.table("be_tt").select("friday").eq("id", 4).execute()
                f42 = supabase.table("be_tt").select("friday").eq("id", 5).execute()
                f43 = supabase.table("be_tt").select("friday").eq("id", 6).execute()
                f4_sub_list = []
                for subject in f41.data:
                    f4_sub_list.append(subject["friday"])
                for subject in f42.data:
                    f4_sub_list.append(subject["friday"])
                for subject in f43.data:
                    f4_sub_list.append(subject["friday"])
                generate_Message_And_send_Mail_for_faculty(f4_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(8):
                send_mail_rescheduled()
            else:
                f6 = supabase.table("be_tt").select("friday").eq("id", 8).execute()
                f6_sub_list = []
                for subject in f6.data:
                    f6_sub_list.append(subject["friday"])
                generate_Message_And_send_Mail_for_faculty(f6_sub_list)
                time.sleep(60)

        elif now.hour == 15 and now.minute == 5:
            if if_true_send_mail_to_rescheduled_faculty(9):
                send_mail_rescheduled()
            else:
                f7 = supabase.table("be_tt").select("friday").eq("id", 9).execute()
                f7_sub_list = []
                for subject in f7.data:
                    f7_sub_list.append(subject["friday"])
                generate_Message_And_send_Mail_for_faculty(f7_sub_list)
                time.sleep(60)

        elif now.hour == 14 and now.minute == 0:
            set_default_values_in_rescheduling_system()
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to activate current day thread ..................
def activeCurrentDaySchedule():
    current_date = datetime.date.today()
    current_day = current_date.strftime("%A")

    # conditions to call the schedule methods according to current day
    if (current_day == "Monday"):
        print("Current day is : ", current_day)
        mondayThread = threading.Thread(target=mondaySchedule)
        mondayThread.start()
        print(current_day, "Thread is started .................")

    elif (current_day == "Tuesday"):
        print("Current day is : ", current_day)
        tuesdayThread = threading.Thread(target=tuesdaySchedule)
        tuesdayThread.start()
        print(current_day, "Thread is started .................")

    elif (current_day == "Wednesday"):
        print("Current day is : ", current_day)
        wednesdayThread = threading.Thread(target=wednesdaySchedule)
        wednesdayThread.start()
        print(current_day, "Thread is started .................")

    elif (current_day == "Thursday"):
        print("Current day is : ", current_day)
        thursdayThread = threading.Thread(target=thursdaySchedule)
        thursdayThread.start()
        print(current_day, "Thread is started .................")

    elif (current_day == "Friday"):
        print("Current day is : ", current_day)
        fridayThread = threading.Thread(target=fridaySchedule)
        fridayThread.start()
        print(current_day, "Thread is started .................")

    else:
        print("Today is ", current_day,
              "\nToday is Holiday so, Enjoy your day .............")
        return




