# add button to pin 2 and pin 10
# add buzzer to pin 11 and ground

from picamera2 import Picamera2
from gpiozero import Button, LED, Buzzer
from signal import pause
from time import sleep
import smtplib
from email.message import EmailMessage
import imghdr


button = Button(17)
buzzer = Buzzer(21)
pic_counter = 0


def take_photo(file_path):
    with Picamera2() as camera:
        # camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
        # camera.configure(camera_config)
        camera_config = camera.create_still_configuration()
        camera.configure(camera_config)
        camera.start()
        sleep(2)
        camera.capture_file(file_path)
        # image = camera.capture_mage("main") # capture PIL images
        camera.close()


def send_email(file_name):
    # Email configuration
    sender_email = "azektser@gmail.com"  # Replace with your email
    receiver_email = "alex3181@yahoo.com"  # Replace with recipient's email
    password = "jesb mipc zufy rmvz"  # Replace with your email password
    # Create a message object
    msg = EmailMessage()
    msg["Subject"] = "Sending a picture attachment"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Check out " + file_name)

    # Load the image file
    with open(file_name, "rb") as f:  # Replace 'image.jpg' with your image file
        file_data = f.read()
        file_type = imghdr.what(None, file_data)

    # Add the image as an attachment
    msg.add_attachment(
        file_data, maintype="image", subtype=file_type, filename=file_name
    )

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)

    print("Email sent successfully!")


def pressed_button():
    global pic_counter
    buzzer.on()
    sleep(0.15)
    buzzer.off()
    file_name = "pic" + str(pic_counter) + ".jpg"
    take_photo(file_name)
    print("File " + file_name + " created")
    pic_counter = pic_counter + 1
    send_email(file_name)	

if __name__ == "__main__":
    button.when_pressed = pressed_button
    pause()
