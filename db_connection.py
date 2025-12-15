import pymongo
import os
from datetime import datetime
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

# =====================================================
# MONGO CONFIG
# =====================================================
MONGO_URL = getattr(
    settings,
    "MONGO_URL",
    os.getenv("MONGO_URL", "mongodb://localhost:27017")
)

MONGO_DB_NAME = getattr(
    settings,
    "MONGO_DB_NAME",
    os.getenv("MONGO_DB_NAME", "shop_db")
)

_client = pymongo.MongoClient(
    MONGO_URL,
    serverSelectionTimeoutMS=5000
)

_db = _client[MONGO_DB_NAME]


# =====================================================
# HELPERS
# =====================================================
def get_db():
    return _db


def get_collection(name: str):
    return _db[name]


# =====================================================
# CUSTOM ORDER SAVE (USED BY CUSTOMIZE)
# =====================================================
def save_custom_order(data: dict):
    """
    Save customized product order to MongoDB
    """
    doc = {
        "user_id": data.get("user_id"),
        "product": data.get("product"),
        "custom_text": data.get("custom_text"),
        "text_color": data.get("text_color"),
        "text_font": data.get("text_font"),
        "packaging": data.get("packaging"),
        "gift_wrap": data.get("gift_wrap", False),
        "pricing": data.get("pricing", {}),
        "status": "created",
        "created_at": datetime.utcnow(),
    }

    return get_collection("custom_orders").insert_one(doc)


# =====================================================
# OPTIONAL: CREATE INDEXES (RUN ONCE)
# =====================================================
def ensure_indexes():
    get_collection("carts").create_index(
        [("owner_type", pymongo.ASCENDING), ("owner", pymongo.ASCENDING)],
        unique=True
    )

    get_collection("custom_orders").create_index(
        [("user_id", pymongo.ASCENDING), ("created_at", pymongo.DESCENDING)]
    )

    get_collection("catalog").create_index(
        [("product_id", pymongo.ASCENDING)], unique=True
    )

    get_collection("catalog").create_index(
        [("name", pymongo.TEXT)]
    )
