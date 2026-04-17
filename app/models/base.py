from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, func
from sqlmodel import Field, SQLModel


class IDMixin(SQLModel):
	id: Optional[int] = Field(default=None, primary_key=True)


class TimestampMixin(SQLModel):
	created_at: datetime = Field(
		default_factory=datetime.utcnow,
		nullable=False,
		sa_type=DateTime(timezone=True),
		sa_column_kwargs={"server_default": func.now()},
	)
	updated_at: datetime = Field(
		default_factory=datetime.utcnow,
		nullable=False,
		sa_type=DateTime(timezone=True),
		sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()},
	)
