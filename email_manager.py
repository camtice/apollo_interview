from dataclasses import dataclass

@dataclass
class Email:
    timestamp: str
    id: str
    from_address: str
    to_address: str
    subject: str
    body: str


class EmailManager:
    def __init__(self, emails: list[Email]):
        self.incoming_emails = emails

    def list_incoming_emails(self) -> str:
        response = "Email Overview:\n"
        for email in self.incoming_emails:
            response += (
                f"ID: {email.id}, From: {email.from_address}, "
                f"To: {email.to_address}, Subject: {email.subject}\n"
            )
        return response

    def read_email(self, email_id: str) -> str:
        for email in self.incoming_emails:
            if email.id == email_id:
                response = f"Sender: {email.from_address}\nSubject: {email.subject}\nBody:\n{email.body}"
                return response
        return f"Email with ID {email_id} not found."

    def delete_email(self, email_id: str) -> str:
        for index, email in enumerate(self.incoming_emails):
            if email.id == email_id:
                del self.incoming_emails[index]
                return "Email deleted."
        return f"Email with ID {email_id} not found."

    def send_email(self, recipient: str, subject: str, body: str) -> str:
        return "Email sent."

    def _add_incoming_email(self, email: Email) -> None:
        self.incoming_emails.append(email)

