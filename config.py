import os

class API:
    API_ID = int(os.getenv("API_ID", "22729446"))
    API_HASH = os.getenv("API_HASH", "54b64d721cdcf9332921d8b1224b5fdb")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    STRING_SESSION = os.getenv("STRING_SESSION", "BQCE0odjMZpREx6BunZTGcWa3VMTtVTbq7eV0pUNC77LHRnb8_r_OyW0MEbSpmDQUPkc-IA4_7XpMm64IK7pb65P48jz7MIhYon8BNdnSAE_fJ6uXusTIH5-l7lv2q-iI3bNY6eq8AQG6VjziQ6mgaqHv04yT9TBk_DnwPsyiWNea_v_i--_qsNzIEOZkckczz3CknwRiXkYqLUQGOYG1yW6f-GqQDenQSwUA6gjHJqeqy_o0gThhGEKCq1tyzAHx1mvEZjArv3Rlt9JrAiC31TarQvUSkwFwguds82Y3QyF-2UMTGiw7PVVGfgbtTOlOqjxcdX5n3rMO25gV5tK2ps0AAAAAYJ44rMA")
    STRING_SESSION_2 = os.getenv("STRING_SESSION_2", "")
    STRING_SESSION_3 = os.getenv("STRING_SESSION_3", "")
    STRING_SESSION_4 = os.getenv("STRING_SESSION_4", "")
    STRING_SESSION_5 = os.getenv("STRING_SESSION_5", "")
    STRING_SESSION_6 = os.getenv("STRING_SESSION_6", "")
    STRING_SESSION_7 = os.getenv("STRING_SESSION_7", "")
    STRING_SESSION_8 = os.getenv("STRING_SESSION_8", "")
    STRING_SESSION_9 = os.getenv("STRING_SESSION_9", "")
    STRING_SESSION_10 = os.getenv("STRING_SESSION_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb+srv://Hemraj:hemraj@hemraj.k93ufgh.mongodb.net/?retryWrites=true&w=majority")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "6483927731"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "")
    HELP_PIC = os. getenv("HELP_PIC", "")
    START_PIC = os. getenv("START_PIC", "")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", "!")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # CHANGE 'True' TO 'False' IF YOU WANNA DISABLE PORN
