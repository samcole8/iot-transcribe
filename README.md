# iot-audio-stream
Realtime audio streaming application, originally for the purpose of speech transcription from a Raspberry Pi Zero.

## Setup

1. Follow the setup guide for the AWS SDK: https://github.com/awslabs/amazon-transcribe-streaming-sdk/tree/develop
2. Install Docker and Docker Compose (optional but required for HTTP display server demo)
3. Ensure PortAudio is installed (`libportaudio2` on Debian-based systems)
4. Install pip requirements

### Run text demo

```
cd client
python3 transcribe.py
```

### Run HTTP display server demo

```
cd display
docker compose up -d
cd ../client
python3 transcribe_http.py
```