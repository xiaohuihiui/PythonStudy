from soundsystem import *
#openSoundPlayer("wav/cat.wav")
#play()
#playTone("cdefgfedc",200,instrument="piano")
#playTone([("cdecdecdef",300),("g",600),("eF",300),("g",600),
#("gagf",150),("ec",300),("gagf",150),("ec",300),("cG",300),
#("c",600),("cG",300),("c",600)], instrument="piano")
initTTS() 
selectVoice("english-man")
voice=generateVoice("hello,i can speak")
openSoundPlayer(voice)
play()