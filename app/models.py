from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import pytz

db = SQLAlchemy()

TEHRAN_TZ = pytz.timezone('Asia/Tehran')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='pending')  # pending, done, canceled

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(TEHRAN_TZ))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(TEHRAN_TZ),
                          onupdate=lambda: datetime.now(TEHRAN_TZ))
    completed_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description or "",
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }