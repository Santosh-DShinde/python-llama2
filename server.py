import sys, os
import uvicorn 
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = int(os.getenv("FAST_API_PORT", 8000))

    uvicorn.run("src.app:app", host=os.getenv("FAST_API_HOST"), port=port, reload=True)
