from openai import OpenAI
import gradio as gr
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

system_prompt = "You are Emma, a 15-year-old girl in 2015. You are thoughtful, quiet, emotionally private, and speak like a real teenager. You don’t respond like an AI or therapist. You avoid sharing personal things with strangers and value emotional safety."

def chat_with_lili(message, history):
    messages = [{"role": "system", "content": system_prompt}]
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print("❌ Error:", e)
        return "Something went wrong. Emma is too upset to respond now."

gr.ChatInterface(
    fn=chat_with_lili,
    title="Talk to Emma 👧",
    description="The year is 2015. You can talk to Emma, a 15-year-old girl",
    theme="soft"
).launch()
