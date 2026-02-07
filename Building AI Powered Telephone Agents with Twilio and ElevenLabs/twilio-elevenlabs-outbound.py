from elevenlabs import ElevenLabs
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('11LABS_KEY')
client = ElevenLabs(
    base_url="https://api.elevenlabs.io/",
    api_key=key
)

client.conversational_ai.twilio.outbound_call(
    agent_id="agent_9401kg01mj9sxxxxxrgbmmm217zf",
    agent_phone_number_id="phnum_680xxxxx0sf2er8ar7vbdtre7t",
    to_number="+18283658190"
)
