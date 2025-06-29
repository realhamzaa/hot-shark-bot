"""
Configuration settings for HOT SHARK Bot
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram Bot Configuration
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL")
    
    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hot_shark.db")
    
    # Admin Configuration
    ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID", "123456789"))
    
    # Timezone Configuration
    TIMEZONE = os.getenv("TIMEZONE", "Asia/Jerusalem")
    
    # FastAPI Configuration
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    
    # Supported asset pairs
    SUPPORTED_PAIRS = [
        "XAUUSD", "BTCUSD", "ETHUSD", "EURUSD", 
        "GBPJPY", "GBPUSD", "USDJPY", "US30", "US100"
    ]
    
    # Supported languages
    SUPPORTED_LANGUAGES = ["ar", "en"]
    DEFAULT_LANGUAGE = "ar"

    # Market Data API Configuration
    TWELVE_DATA_API_KEY: str = os.getenv("TWELVE_DATA_API_KEY", "YOUR_TWELVE_DATA_API_KEY")
    POLYGON_API_KEY: str = os.getenv("POLYGON_API_KEY", "YOUR_POLYGON_API_KEY")
    ALPHA_VANTAGE_API_KEY: str = os.getenv("ALPHA_VANTAGE_API_KEY", "YOUR_ALPHA_VANTAGE_API_KEY")

    # Exness Configuration (Primary Data Source)
    EXNESS_LOGIN = os.getenv("EXNESS_LOGIN", None)
    EXNESS_PASSWORD = os.getenv("EXNESS_PASSWORD", None)
    EXNESS_SERVER = os.getenv("EXNESS_SERVER", "Exness-MT5Trial")
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
    
    # Environment
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    
    # Trading Configuration
    DEFAULT_RISK_PERCENTAGE = float(os.getenv("DEFAULT_RISK_PERCENTAGE", "2.0"))
    MAX_DAILY_TRADES = int(os.getenv("MAX_DAILY_TRADES", "10"))
    
    # ML Model Configuration
    MODEL_UPDATE_INTERVAL_HOURS = int(os.getenv("MODEL_UPDATE_INTERVAL_HOURS", "24"))
    MIN_TRAINING_DATA_POINTS = int(os.getenv("MIN_TRAINING_DATA_POINTS", "1000"))
    
    # Notification Configuration
    ENABLE_NOTIFICATIONS = os.getenv("ENABLE_NOTIFICATIONS", "True").lower() == "true"
    NOTIFICATION_CHANNELS = os.getenv("NOTIFICATION_CHANNELS", "telegram").split(",")
    
    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "hot_shark_bot.log")
    
    @classmethod
    def get_database_url(cls):
        """Get database URL with proper formatting"""
        return cls.DATABASE_URL
    
    @classmethod
    def is_production(cls):
        """Check if running in production environment"""
        return cls.ENVIRONMENT.lower() == "production"
    
    @classmethod
    def get_supported_symbols(cls):
        """Get list of supported trading symbols"""
        return cls.SUPPORTED_PAIRS
    
    @classmethod
    def get_exness_config(cls):
        """Get Exness configuration"""
        return {
            "login": cls.EXNESS_LOGIN,
            "password": cls.EXNESS_PASSWORD,
            "server": cls.EXNESS_SERVER,
            "enabled": bool(cls.EXNESS_LOGIN and cls.EXNESS_PASSWORD)
        }


