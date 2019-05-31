#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding: UTF-8
import os,subprocess
import io


class juliusSpeechToText:
    def __init__(self):
        self.startListening()
    def __del__(self):
        self.stopListening()

    def startListening(self):
        # cmd = 'bash ./lib/dictation-kit/run-linux-dnn-minimal.sh'
        cmd = 'cd ~/lib/julius_libs/dictation-kit/;bash run-linux-dnn.sh'
        self.julius_process = subprocess.Popen(cmd,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
        # print('debug_1\n')

    def stopListening(self):
        # print('debug_3\n')
        self.julius_process.kill()

    def textStreaming(self):
        # print('debug_2\n')
        # 文字列の逐次表示（参考：https://qiita.com/FGtatsuro/items/0f68ab9c1bcad9c4b320）
        with io.open(self.julius_process.stdout.fileno(), closefd=False) as stream:
            for line in stream:
                out_string = line.rstrip('\n')
                # print(out_string)
                find_text_flag = out_string.find('sentence1:  ')
                if find_text_flag != -1:
                    text_string = out_string.lstrip('sentence1:  ')
                    if text_string != '。':
                        # None
                        print('text:'+ text_string)


def main():
    julius = juliusSpeechToText()
    print("Juliusによる音声認識を開始")
    julius.textStreaming()


if __name__ == '__main__':
    main()
