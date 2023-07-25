import openai
import gradio as gr

openai.api_key = "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"

def chatbot(system_msg, message):
    messages = [{"role": "system", "content": system_msg}]
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

iface = gr.Interface(
    fn=chatbot,
    inputs=["text", "text"],
    outputs="text",
    inputs_layout="horizontal",
    outputs_layout="vertical",
    examples=[["Tell me a joke", "Why did the chicken cross the road?"],
              ["Translate this English text to French", "Hello, how are you?"],
              ["can you give reply like my mom she is angry and sweet ","who is president of india"]],
    title="NAMA ChatBot",
    description="Type your system message and chat with the chatbot!"
)

if __name__ == '__main__':
    iface.launch(share=True)
