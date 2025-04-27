import torch
from fastapi import APIRouter, Request
import io
import ffmpeg
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import soundfile as sf
# from datasets import load_dataset

router = APIRouter()

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)

@router.post("/transcribe")
async def transcribe_audio(request: Request):
    webm_bytes = await request.body()

    in_buffer = io.BytesIO(webm_bytes)

    process = (
        ffmpeg
        .input('pipe:0')
        .output('pipe:1', format='wav', acodec='pcm_s16le', ac=1, ar='16k')
        .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True)
    )

    out, err = process.communicate(input=in_buffer.read())

    wav_buffer = io.BytesIO(out)

    # Step: Read into numpy
    wav_buffer.seek(0)
    # This returns a tuple of (data, samplerate)
    audio_data = sf.read(wav_buffer)
    
    # Extract the audio data (numpy array) from the tuple
    audio = audio_data[0]
    samplerate = audio_data[1]

    # Transcribe - pass just the audio data (numpy array)
    result = pipe(audio, return_timestamps=True)
    return {"text": result["text"]}
