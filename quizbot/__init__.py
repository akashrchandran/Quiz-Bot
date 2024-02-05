import logging
import os
from dotenv import load_dotenv
from quizbot.modules.downloader import FilesDownloder

load_dotenv()
FilesDownloder()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ERROR_CHANNEl_ID = os.getenv("ERROR_CHANNEl_ID")
ENVIRONMENT = os.getenv("ENVIRONMENT")
PORT = int(os.environ.get("PORT", "8080"))



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

__VERSION__ = "0.0.0"