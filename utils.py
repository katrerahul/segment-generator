from google import genai
from google.genai import types
import base64
import os
from constants import SEGMENT_GENERATE_PROMPT

def generate(segment_prompt):
  client = genai.Client(
      vertexai=True,
      api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"),
  )

#   si_text1 = """You will assist to create a sql string for creating a segment.
#
# platform can be the following inputs : whatsapp, googlercs, sms
# marketing_opt_in_state is an integer and can be 0,1,-1 and NULL.
# 0: No Status
#  1: Subscribed (Opt-in)
# NULL: no status
# -1: Unsubscribed/ opted out
#
#
# tags is a string input
# Double quotes needs to be escaped with a backslash
#
# Here are some outputs
# platform=\\"whatsapp\\" && marketing_opt_in_state IN (1)
# platform=\\"whatsapp\\" && (marketing_opt_in_state IN (1, 0) OR marketing_opt_in_state IS NULL) && \\"valid\\" in unnest(tags)"""

  model = "gemini-3-pro-preview"
  contents = [
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text=segment_prompt)
      ]
    ),
  ]
  tools = [
    types.Tool(google_search=types.GoogleSearch()),
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    tools = tools,
    system_instruction=[types.Part.from_text(text=SEGMENT_GENERATE_PROMPT)],
    thinking_config=types.ThinkingConfig(
      thinking_level="HIGH",
    ),
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    if not chunk.candidates or not chunk.candidates[0].content or not chunk.candidates[0].content.parts:
        continue
    print(chunk.text, end="")
    return chunk.text

if __name__ == "__main__":
  generate("target a segment for google rcs and opted in")