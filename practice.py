from dataclasses import dataclass


@dataclass
class Email:
    id: str
    to: str
    sender: str
    heading: str
    body: str
    

class EmailManager: 
    def __init__(self, emails:list[Email]):
        self.inbox = emails

    def list_inbox(self) -> str:
        output = "Current Inbox \n"
        
        for email in self.inbox:
            output += f"ID: {email.id}\n"
            
        return output

emails = [
    Email(id='1', to='you', sender='me', heading='what you doing', body='for real, wyd'), 
    Email(id='2', to='me', sender='you', heading='nothing', body='for real, nothing')]


inbox = EmailManager(emails=emails)

print(inbox.list_inbox())