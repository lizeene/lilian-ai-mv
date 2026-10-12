import gradio as gr

def create_video(song, image, prompt):
    return "Your CELEBRATION video is ready! Next we connect real AI."

app = gr.Interface(
    fn=create_video,
    inputs=[
        gr.Audio(label="Upload CELEBRATION song"),
        gr.Image(label="Upload your photo"),
        gr.Textbox(label="Video style", placeholder="joyful church celebration")
    ],
    outputs=gr.Textbox(label="Status"),
    title="Lilian AI MV",
    description="My own AI music video app"
)
app.launch()
