# telegram-hello-ep17-bot
This is a small how to build a telegram bot for EuroPython 2017

# Build venv
Requires python 3
```shell
./build_venv.sh
```

# Run
```shell
. .venv/bin/activate
export TG_BOT_TOKEN="Bot Token goes here"
export TG_BOT_NAME="Bot Name goes here"
python src/app.py
```

# Docker
```shell
docker build -t ep17bot . && \
docker run -e TG_BOT_TOKEN="token" ep17bot
```

*OR*

```shell
docker run -e TG_BOT_TOKEN="token" vit1/telegram-hello-ep17-bot
```
