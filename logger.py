import config

def info(text):
    if config.logging:
        print(text)
