from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
    DateTime,
    CheckConstraint,
    text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""All models and schemas for SQLAchemy that are used to create MySQL database tables."""


class City(Base):
    __tablename__ = "cities"

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(40), unique=True, nullable=False)

    # Relationship to WeatherData
    weather_data = relationship("WeatherData", back_populates="city")


class WeatherData(Base):
    __tablename__ = "weather_data"

    weather_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(40), ForeignKey("cities.city_name"), nullable=False)
    temperature = Column(Float)
    # unit = Column(String(20), default="Celsius")
    # Using server_default=text("'Celsius'") ensures that the default value is set at the database level, so even if you insert data without specifying a value for the "unit" column, "Celsius" will be used as the default.
    unit = Column(String(20), server_default=text("'Celsius'"))
    condition = Column(String(50))
    conditions_description = Column(String(255))
    timestamp = Column(DateTime)

    # Corrected Relationship to City
    city = relationship("City", back_populates="weather_data")

    # CheckConstraints for condition and temperature
    __table_args__ = (
        CheckConstraint(unit.in_(["Fahrenheit", "Celsius", "Kelvin"])),
        CheckConstraint(temperature.between(-100, 100)),
    )


# class WeatherData(Base):
#     __tablename__ = "weather_data"

#     weather_id = Column(Integer, primary_key=True, autoincrement=True)
#     # city_id = Column(Integer, ForeignKey("cities.city_id"), nullable=False)
#     city_name = Column(String(40), ForeignKey("cities.city_name"), nullable=False)
#     temperature = Column(Float)
#     # Add Tempt_measurement, i.e. Celsius or Fahrenheit, and enforce this in Database level with a check
#     condition = Column(String(50))
#     conditions_description = Column(String(255))
#     timestamp = Column(DateTime)

#     # Relationship to City
#     city = relationship("City", back_populates="weather_data")

#     # def __repr__(self):
#     #     return f"<WeatherData(weather_id='{self.weather_id}', city_id='{self.city_id}', temperature='{self.temperature}', condition='{self.condition}', conditions_description='{self.conditions_description}', timestamp='{self.timestamp}')>"
