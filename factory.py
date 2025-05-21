"""
This is an example of the factory creational pattern implemented in Python.

Scenario:
We're building a notification system that can send messages via different
channels.  We want to create a simple interface for sending notifications
without having to worry about the specifics of each channel.
"""


class NotificationSender:
    def send(self, *args, **kwargs):
        raise NotImplementedError


class EmailNotificationSender(NotificationSender):
    def send(self, *args, **kwargs):
        if not kwargs.get("email"):
            raise ValueError("email is required")

        if not kwargs.get("subject"):
            raise ValueError("subject is required")

        if not kwargs.get("message"):
            raise ValueError("message is required")

        print("Sending email...")
        print(f"Email: {kwargs['email']}")
        print(f"Subject: {kwargs['subject']}")
        print(f"Message: {kwargs['message']}")


class SMSNotificationSender(NotificationSender):
    def send(self, *args, **kwargs):
        if not kwargs.get("phone"):
            raise ValueError("phone is required")

        if not kwargs.get("message"):
            raise ValueError("message is required")

        print("Sending SMS...")
        print(f"To: {kwargs['phone']}")
        print(f"Message: {kwargs['message']}")


class PushNotificationSender(NotificationSender):
    def send(self, *args, **kwargs):
        if not kwargs.get("device_token"):
            raise ValueError("device_token is required")

        if not kwargs.get("message"):
            raise ValueError("message is required")

        print("Sending push notification...")
        print(f"Device Token: {kwargs['device_token']}")
        print(f"Message: {kwargs['message']}")


class Notifier:
    @staticmethod
    def get_sender(notification_type: str) -> NotificationSender:
        """
        Returns the appropriate NotificationSender subclass for the given
        notification_type.
        """

        if notification_type == "email":
            return EmailNotificationSender()
        elif notification_type == "sms":
            return SMSNotificationSender()
        elif notification_type == "push":
            return PushNotificationSender()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

    @staticmethod
    def send(notification_type: str, **kwargs):
        sender = Notifier.get_sender(notification_type)
        sender.send(**kwargs)


Notifier.send(
    "email",
    email="user@example.com",
    subject="You have received a notification",
    message="This is a test email.",
)

Notifier.send(
    "sms",
    phone="+1234567890",
    message="This is a test SMS.",
)

Notifier.send(
    "push",
    device_token="abcdef123456",
    message="This is a test push notification.",
)
