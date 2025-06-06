import whisper
import os

def transcribe_audio(input_path, output_dir, model_name="small"):
    model = whisper.load_model(model_name)
    result = model.transcribe(input_path, verbose=True)
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    srt_path = os.path.join(output_dir, f"{base_name}.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result['segments'], 1):
            start = segment['start']
            end = segment['end']
            text = segment['text']
            def format_time(s):
                h = int(s // 3600)
                m = int((s % 3600) // 60)
                s = s % 60
                return f"{h:02}:{m:02}:{int(s):02},{int((s - int(s)) * 1000):03}"
            f.write(f"{i}\n{format_time(start)} --> {format_time(end)}\n{text.strip()}\n\n")
    print(f"SRT сохранён: {srt_path}")
    return srt_path

if __name__ == "__main__":
    input_audio = "../audio_input/testfile.mp3"  # Замени на нужный файл
    output_dir = "../srt_output"
    transcribe_audio(input_audio, output_dir)
