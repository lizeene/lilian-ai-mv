import gradio as gr

def make_mv(song_title, audio, image, style, mood):
    if audio is None:
        return None, f"Please upload audio for '{song_title}' first!"
    if image is None:
        return None, "Please upload your photo / cover art!"
    
    # This is the base - we will connect real AI video next step
    message = f"""
    ✅ Ready to create!
    Song Title: {song_title}
    Style: {style}
    Mood: {mood}
    Audio: Uploaded
    Photo: Uploaded
    
    Next: Add Replicate token to generate REAL video for ANY song.
    """
    return image, message

with gr.Blocks(title="Lilian Gospel MV Maker") as app:
    gr.Markdown("# 🎤 Lilian Gospel MV Maker\n### Create music videos for ANY of your songs")
    
    song_title = gr.Textbox(label="Song Title", placeholder="e.g., Celebration, Grateful Heart, Holy Spirit...")
    with gr.Row():
        audio_input = gr.Audio(label="Upload ANY Gospel Song (MP3/WAV)", type="filepath")
        image_input = gr.Image(label="Upload Photo / Cover Art", type="filepath")
    
    with gr.Row():
        style = gr.Textbox(label="Video Style", value="joyful gospel celebration, golden lights, church crowd dancing", placeholder="Describe your video...")
        mood = gr.Dropdown(choices=["Joyful Celebration", "Deep Worship", "Thanksgiving", "Praise Dance", "Soulful"], label="Mood", value="Joyful Celebration")
    
    btn = gr.Button("CREATE MUSIC VIDEO FOR THIS SONG ✨")
    
    video_output = gr.Image(label="Preview / Result")
    status = gr.Textbox(label="Status", lines=8)

    btn.click(fn=make_mv, inputs=[song_title, audio_input, image_input, style, mood], outputs=[video_output, status])

app.launch()
