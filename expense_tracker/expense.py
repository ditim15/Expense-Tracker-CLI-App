from datetime import datetime

class Expense:
    def __init__(self, id, title, description, amount, date=datetime.now().month):
        self.id = id
        self.title = title
        self.description = description
        self.amount = amount
        self.date = date

    def __str__(self):
        return (f"[{self.id}] {self.title} - {'$' + f'{self.amount:.2f}':>10}\n"
                f"    {self.description} | Month: {self.date}\n"
                f"    {'-' * 36}")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "amount": self.amount,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            amount=data["amount"],
            date=data.get("date")
        )