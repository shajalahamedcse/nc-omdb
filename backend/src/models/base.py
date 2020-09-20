from datetime import datetime
from src.core import db
from sqlalchemy import inspect

class BaseModel:
    _created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    _updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.now)
    to_json_filter = ()
    @property
    def json(self):
        return {
            column: value
            if not isinstance(value, datetime) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
            if column not in self.to_json_filter and not column.startswith("_") and not column.startswith("rel_")
        }
        
    def _to_dict(self):
            
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self.__class__).attrs
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()