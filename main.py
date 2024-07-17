
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def create_email(subject, body, to_email, from_email, attachment_paths, template_image_path=None):
    # Create the MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # # Attach files
    # for file_path in attachment_paths:
    #     attachment = open(file_path, "rb")
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload((attachment).read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file_path)}")
    #     msg.attach(part)
    #
    # # Attach template image if provided
    # if template_image_path:
    #     image_attachment = open(template_image_path, "rb")
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload((image_attachment).read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(template_image_path)}")
    #     msg.attach(part)

    return msg

def save_draft(msg, smtp_server, smtp_port, login, password):
    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to the email account
        server.login(login, password)

        # Save the email as a draft
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        # Disconnect from the server
        server.quit()

        print("Draft email saved successfully!")
    except Exception as e:
        print(f"Failed to save draft email: {str(e)}")


# Main Function to runn things here
if __name__ == '__main__':

    # Usage
    subject = "Your Subject"
    body = "This is a draft email."
    to_email = "jyothiranuragvasuch@gmail.com"
    from_email = "jyothiranurag@gmail.com"
    attachment_paths = ["path/to/file1.txt", "path/to/file2.pdf"]
    template_image_path = "path/to/template_image.png"

    msg = create_email(subject, body, to_email, from_email, attachment_paths, template_image_path)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    login = from_email
    password = "anudee1321"

    save_draft(msg, smtp_server, smtp_port, login, password)
