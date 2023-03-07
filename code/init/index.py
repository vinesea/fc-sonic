# coding=utf-8
import os


def handler(event, context):
    if not os.path.exists("/mnt/auto/sonic"):
        os.system(
            "wget https://github.com/go-sonic/sonic/releases/download/v1.0.8/sonic-linux-amd64.zip -O /mnt/auto/sonic.zip")
        os.system(
            "cd /mnt/auto && unzip -d sonic sonic.zip && rm sonic.zip && cd -")
    return "nas init"
