import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
from pydub import AudioSegment
import os
from pyannote.audio import Pipeline
import torch
import torchaudio

class AudioToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("تبدیل مکالمه صوتی به متن (آفلاین)")
        self.root.geometry("600x400")

        # متغیرها
        self.audio_path = None

        # بارگذاری مدل‌های آفلاین
        self.whisper_model = whisper.load_model("base")  # مدل کوچک Whisper
        self.diarization_pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            use_auth_token="YOUR_HUGGINGFACE_TOKEN"  # جایگزین با توکن خود
        )

        # رابط گرافیکی
        self.label = tk.Label(root, text="لطفاً فایل صوتی را انتخاب کنید (فرمت WAV یا MP3)")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="انتخاب فایل", command=self.select_audio)
        self.select_button.pack(pady=5)

        self.process_button = tk.Button(root, text="پردازش فایل", command=self.process_audio, state="disabled")
        self.process_button.pack(pady=5)

        self.text_area = tk.Text(root, height=15, width=60)
        self.text_area.pack(pady=10)

    def select_audio(self):
        self.audio_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if self.audio_path:
            self.label.config(text=f"فایل انتخاب شده: {os.path.basename(self.audio_path)}")
            self.process_button.config(state="normal")

    def process_audio(self):
        if not self.audio_path:
            messagebox.showerror("خطا", "لطفاً ابتدا یک فایل صوتی انتخاب کنید!")
            return

        try:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, "در حال پردازش...\n")

            # تبدیل فایل به WAV
            audio = AudioSegment.from_file(self.audio_path)
            wav_path = "temp.wav"
            audio.export(wav_path, format="wav")

            # تشخیص گوینده
            diarization = self.diarization_pipeline(wav_path)
            segments = []
            for turn, _, speaker in diarization.itertracks(yield_label=True):
                segments.append((turn.start, turn.end, speaker))

            # تبدیل گفتار به متن
            for start, end, speaker in segments:
                audio_segment = audio[start * 1000:end * 1000]
                segment_wav = "temp_segment.wav"
                audio_segment.export(segment_wav, format="wav")

                result = self.whisper_model.transcribe(segment_wav, language="fa")
                text = result["text"]
                self.text_area.insert(tk.END, f"گوینده {speaker}: {text}\n")

            # پاکسازی فایل‌های موقت
            if os.path.exists(wav_path):
                os.remove(wav_path)
            if os.path.exists(segment_wav):
                os.remove(segment_wav)

            messagebox.showinfo("موفقیت", "پردازش با موفقیت انجام شد!")
        except Exception as e:
            messagebox.showerror("خطا", f"خطایی رخ داد: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioToTextApp(root)
    root.mainloop()