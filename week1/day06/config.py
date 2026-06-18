from dataclasses import dataclass, field
from enum import Enum
from typing import List


# ----------------------------------
# ENUM
# ----------------------------------

class Environment(Enum):
    DEV = "development"
    STAGING = "staging"
    PROD = "production"


# ----------------------------------
# DATACLASS
# ----------------------------------

@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str


# ----------------------------------
# APP CONFIG
# ----------------------------------

@dataclass
class AppConfig:
    app_name: str
    version: str
    environment: Environment
    database: DatabaseConfig
    features: List[str] = field(default_factory=list)


# ----------------------------------
# CREATE CONFIG
# ----------------------------------

db_config = DatabaseConfig(
    host="localhost",
    port=5432,
    username="admin",
    password="secret"
)

app_config = AppConfig(
    app_name="AI Engineering Roadmap",
    version="1.0",
    environment=Environment.DEV,
    database=db_config,
    features=["logging", "monitoring", "analytics"]
)

print(app_config)

print("\nEnvironment:")
print(app_config.environment.value)

print("\nFeatures:")
for feature in app_config.features:
    print("-", feature)