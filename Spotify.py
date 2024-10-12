import tkinter as tk
import pygame
from tkinter import *
from mutagen.mp3 import MP3


root = tk.Tk()
root.title("Spotify")
root.state('zoomed') 
root.config(bg="#060E08")


pygame.mixer.init()

global count 
count = -60

global liked_song 
liked_song = [0,0,0,0,0]

global active_library
active_library = 1

global active_song
active_song = 1

global like_button1_clicked
global like_button2_clicked
global like_button3_clicked
global like_button4_clicked
global like_button5_clicked

like_button1_clicked = True
like_button2_clicked = True
like_button3_clicked = True
like_button4_clicked = True
like_button5_clicked = True


global music_path
global music_path_2
global music_path_3
global music_path_4
global music_path_5

music_path = r"D:\Repo\Python\Song\song1.mp3"
pygame.mixer.music.load(music_path)
pygame.mixer.music.play()
pygame.mixer.music.pause()

music_path_2 = r"D:\Repo\Python\Song\song2.mp3"

music_path_3 = r"D:\Repo\Python\Song\song3.mp3"

music_path_4 = r"D:\Repo\Python\Song\song4.mp3"

music_path_5 = r"D:\Repo\Python\Song\song5.mp3"


global audio1
global audio2
global audio3
global audio4
global audio5
    
audio1 = MP3(music_path)
audio2 = MP3(music_path_2)
audio3 = MP3(music_path_3)
audio4 = MP3(music_path_4)
audio5 = MP3(music_path_5)


frame = tk.Frame(root, bg="#2F2F2E", width=1550, height=75)
frame.place(x=0,y=717)

frame1 = tk.Frame(root, bg="#343634", width=1550, height=60)
frame1.place(x=0,y=657)

frame2 = tk.Frame(root, bg="#091609", width=300, height=577)
frame2.place(x=0,y=80)

frame3 = tk.Frame(root, bg="#111D0D", width=1550, height=80)
frame3.place(x=0,y=0)

lab1 = Label(
    root,
    text="Spotify",
    fg="green",
    bg="#111D0D",
    font=("Arial", 30, "bold"),
)
lab1.place(x=170,y=15)


lab2 = Label(
    root,
    text="|  Library",
    fg="#5D734D",
    bg="#091609",
    width=7,
    font=("Arial", 25),
)
lab2.place(x=35,y=120)


lab4 = Label(
    root,
    text="#Favourites",
    fg="#5D734D",
    bg="#060E08",
    width=10,
    font=("Arial", 60),
)
lab4.place(x=350,y=120)


lab5 = Label(
    root,
    text="No liked songs :(",
    fg="#5D734D",
    bg="#060E08",
    width=20,
    font=("Arial", 20),
    )
lab5.place(x=350,y=320)
        

frame4 = tk.Frame(root, bg="#5D734D", width=1000, height=1)
frame4.place(x=370,y=250)


def playlist_clicked() :
    
    global active_song
    global liked_song
    global active_library
    active_library = 1
    
    frame5 = tk.Frame(root, bg="#060E08", width=1550, height=500)
    frame5.place(x=300,y=80)
    
    lab4 = Label(
        root,
        text="#Favourites",
        fg="#5D734D",
        bg="#060E08",
        width=10,
        font=("Arial", 60),
    )
    lab4.place(x=350,y=120)

    frame4 = tk.Frame(root, bg="#5D734D", width=1000, height=1)
    frame4.place(x=370,y=250)
    
    global values 
    values = 0
    
    for i in liked_song :
        if values != liked_song[i-1] :
            values += 1
    
    if values == 0 :
        
        lab5 = Label(
        root,
        text="No liked songs :(",
        fg="#5D734D",
        bg="#060E08",
        width=20,
        font=("Arial", 20),
        )
        lab5.place(x=350,y=320)
        
    else :
            
            if liked_song[0] == 1 :
                
                def music_clicked() :
                    
                    lab7.config(text="")
                    some_length = audio1.info.length
                    mins = int(some_length // 60)
                    secs = int(some_length % 60)
                    lab7.configure(text=f"{mins}:{secs:02d}")
                    selected_time = int(track_length.get())
                    track_length.config(to=int(some_length))
        
                    global play_button_clicked
                    global active_song
                    active_song = 1
                    
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_path)
                    pygame.mixer.music.play(start=selected_time)
                    play_button.config(text="⏸")
                    like_button.config(text="♡")
                    if like_button1_clicked == False :
                        like_button.config(text="♥")
                    play_button_clicked = True

                music_button = tk.Button(
                root,
                relief=tk.FLAT,
                borderwidth=0, 
                text="|         Mary on a Cross",
                bg="#060E08",
                fg="#326935",
                activebackground="#19260F",
                activeforeground="#AAABAA",
                width=40,
                font=("Arial", 20, "bold"), 
                anchor="w",
                command=music_clicked
                )
                music_button.place(x=390, y=290)
                
            if liked_song[1] == 2 :
                
                def music1_clicked() :
                    
                    lab7.config(text="")
                    some_length = audio2.info.length
                    mins = int(some_length // 60)
                    secs = int(some_length % 60)
                    lab7.configure(text=f"{mins}:{secs:02d}")
                    selected_time = int(track_length.get())
                    track_length.config(to=int(some_length))
                    
        
                    global play_button_clicked
                    global active_song
                    active_song = 2
                    
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_path_2)
                    pygame.mixer.music.play(start=selected_time)
                    play_button.config(text="⏸")
                    like_button.config(text="♡")
                    if like_button2_clicked == False :
                        like_button.config(text="♥")
                    play_button_clicked = True

                music1_button = tk.Button(
                root,
                relief=tk.FLAT,
                borderwidth=0, 
                text="|         Sunflower",
                bg="#060E08",
                fg="#326935",
                activebackground="#19260F",
                activeforeground="#AAABAA",
                width=40,
                font=("Arial", 20, "bold"), 
                anchor="w",
                command=music1_clicked
                )
                music1_button.place(x=390, y=350)
                
            if liked_song[2] == 3 :
                
                def music2_clicked() :
                    
                    lab7.config(text="")
                    some_length = audio3.info.length
                    mins = int(some_length // 60)
                    secs = int(some_length % 60)
                    lab7.configure(text=f"{mins}:{secs:02d}")
                    selected_time = int(track_length.get())
                    track_length.config(to=int(some_length))
        
                    global play_button_clicked
                    global active_song
                    active_song = 3
                    
                    
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_path_3)
                    pygame.mixer.music.play(start=selected_time)
                    play_button.config(text="⏸")
                    like_button.config(text="♡")
                    if like_button3_clicked == False :
                        like_button.config(text="♥")
                    play_button_clicked = True

                music2_button = tk.Button(
                root,
                relief=tk.FLAT,
                borderwidth=0, 
                text="|         Ticking Away",
                bg="#060E08",
                fg="#326935",
                activebackground="#19260F",
                activeforeground="#AAABAA",
                width=40,
                font=("Arial", 20, "bold"), 
                anchor="w",
                command=music2_clicked
                )
                music2_button.place(x=390, y=410)
                
            if liked_song[3] == 4 :
                
                def music3_clicked() :
                    
                    lab7.config(text="")
                    some_length = audio4.info.length
                    mins = int(some_length // 60)
                    secs = int(some_length % 60)
                    lab7.configure(text=f"{mins}:{secs:02d}")
                    selected_time = int(track_length.get())
                    track_length.config(to=int(some_length))
        
                    global play_button_clicked
                    global active_song
                    active_song = 4        
                    

                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_path_4)
                    pygame.mixer.music.play(start=selected_time)
                    play_button.config(text="⏸")
                    like_button.config(text="♡")
                    if like_button4_clicked == False :
                        like_button.config(text="♥")
                    play_button_clicked = True

                music3_button = tk.Button(
                root,
                relief=tk.FLAT,
                borderwidth=0, 
                text="|         Desi Kalakar",
                bg="#060E08",
                fg="#326935",
                activebackground="#19260F",
                activeforeground="#AAABAA",
                width=40,
                font=("Arial", 20, "bold"), 
                anchor="w",
                command=music3_clicked
                )
                music3_button.place(x=390, y=290 + count)
                
            if liked_song[4] == 5 :
                
                def music4_clicked() :
                    
                    lab7.config(text="")
                    some_length = audio5.info.length
                    mins = int(some_length // 60)
                    secs = int(some_length % 60)
                    lab7.configure(text=f"{mins}:{secs:02d}")
                    selected_time = int(track_length.get())
                    track_length.config(to=int(some_length))
        
                    global play_button_clicked
                    global active_song
                    active_song = 5
                    

                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_path_5)
                    pygame.mixer.music.play(start=selected_time)
                    play_button.config(text="⏸")
                    like_button.config(text="♡")
                    if like_button5_clicked == False :
                        like_button.config(text="♥")
                    play_button_clicked = True

                music4_button = tk.Button(
                root,
                relief=tk.FLAT,
                borderwidth=0, 
                text="|         Level",
                bg="#060E08",
                fg="#326935",
                activebackground="#19260F",
                activeforeground="#AAABAA",
                width=40,
                font=("Arial", 20, "bold"), 
                anchor="w",
                command=music4_clicked
                )
                music4_button.place(x=390, y=540)
    

playlist_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="Favourites",
    bg="#1A1A1A",
    fg="#666967",
    activebackground="green",
    activeforeground="#1A1A1A",
    width=15,
    font=("Arial", 20, "bold"), 
    command=playlist_clicked
)
playlist_button.place(x=20, y=220)


def playlist2_clicked() :
    
    global active_library
    active_library = 2
    
    frame5 = tk.Frame(root, bg="#060E08", width=1550, height=500)
    frame5.place(x=300,y=80)
    
    lab4 = Label(
        root,
        text="#English",
        fg="#5D734D",
        bg="#060E08",
        width=10,
        font=("Arial", 60),
    )
    lab4.place(x=350,y=120)

    frame4 = tk.Frame(root, bg="#5D734D", width=1000, height=1)
    frame4.place(x=370,y=250)

    def music_clicked() :
        
        lab7.config(text="")
        some_length = audio1.info.length
        mins = int(some_length // 60)
        secs = int(some_length % 60)
        lab7.configure(text=f"{mins}:{secs:02d}")
        selected_time = int(track_length.get())
        track_length.config(to=int(some_length))
        
        global play_button_clicked
        global active_song
        active_song = 1
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(start=selected_time)
        play_button.config(text="⏸")
        like_button.config(text="♡")
        if like_button1_clicked == False :
            like_button.config(text="♥")
        play_button_clicked = True

    music_button = tk.Button(
        root,
        relief=tk.FLAT,
        borderwidth=0, 
        text="|         Mary on a Cross",
        bg="#060E08",
        fg="#326935",
        activebackground="#19260F",
        activeforeground="#AAABAA",
        width=40,
        font=("Arial", 20, "bold"), 
        anchor="w",
        command=music_clicked
    )
    music_button.place(x=390, y=290)



    def music1_clicked() :
        
        lab7.config(text="")
        some_length = audio2.info.length
        mins = int(some_length // 60)
        secs = int(some_length % 60)
        lab7.configure(text=f"{mins}:{secs:02d}")
        selected_time = int(track_length.get())
        track_length.config(to=int(some_length))
        
        global play_button_clicked
        global active_song
        active_song = 2
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path_2)
        pygame.mixer.music.play(start=selected_time)
        play_button.config(text="⏸")
        like_button.config(text="♡")
        if like_button2_clicked == False :
            like_button.config(text="♥")
        play_button_clicked = True

    music1_button = tk.Button(
        root,
        relief=tk.FLAT,
        borderwidth=0, 
        text="|         Sunflower",
        bg="#060E08",
        fg="#326935",
        activebackground="#19260F",
        activeforeground="#AAABAA",
        width=40,
        font=("Arial", 20, "bold"), 
        anchor="w",
        command=music1_clicked
    )
    music1_button.place(x=390, y=350)



    def music2_clicked() :
        
        lab7.config(text="")
        some_length = audio3.info.length
        mins = int(some_length // 60)
        secs = int(some_length % 60)
        lab7.configure(text=f"{mins}:{secs:02d}")
        selected_time = int(track_length.get())
        track_length.config(to=int(some_length))
        
        global play_button_clicked
        global active_song
        active_song = 3
        
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path_3)
        pygame.mixer.music.play(start=selected_time)
        play_button.config(text="⏸")
        like_button.config(text="♡")
        if like_button3_clicked == False :
            like_button.config(text="♥")
        play_button_clicked = True

    music2_button = tk.Button(
        root,
        relief=tk.FLAT,
        borderwidth=0, 
        text="|         Ticking Away",
        bg="#060E08",
        fg="#326935",
        activebackground="#19260F",
        activeforeground="#AAABAA",
        width=40,
        font=("Arial", 20, "bold"), 
        anchor="w",
        command=music2_clicked
    )
    music2_button.place(x=390, y=410)

playlist2_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="English",
    bg="#1A1A1A",
    fg="#666967",
    activebackground="green",
    activeforeground="#1A1A1A",
    width=15,
    font=("Arial", 20, "bold"), 
    command=playlist2_clicked
)
playlist2_button.place(x=20, y=300)



def playlist3_clicked() :
    
    global active_library
    active_library = 3
    
    frame5 = tk.Frame(root, bg="#060E08", width=1550, height=500)
    frame5.place(x=300,y=80)
    
    lab4 = Label(
        root,
        text="#Hindi",
        fg="#5D734D",
        bg="#060E08",
        width=10,
        font=("Arial", 60),
    )
    lab4.place(x=350,y=120)

    frame4 = tk.Frame(root, bg="#5D734D", width=1000, height=1)
    frame4.place(x=370,y=250)
    
    def music3_clicked() :
        
        lab7.config(text="")
        some_length = audio4.info.length
        mins = int(some_length // 60)
        secs = int(some_length % 60)
        lab7.configure(text=f"{mins}:{secs:02d}")
        selected_time = int(track_length.get())
        track_length.config(to=int(some_length))
        
        global play_button_clicked
        global active_song
        active_song = 4        
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path_4)
        pygame.mixer.music.play(start=selected_time)
        play_button.config(text="⏸")
        like_button.config(text="♡")
        if like_button4_clicked == False :
            like_button.config(text="♥")
        play_button_clicked = True

    music3_button = tk.Button(
        root,
        relief=tk.FLAT,
        borderwidth=0, 
        text="|         Desi Kalakar",
        bg="#060E08",
        fg="#326935",
        activebackground="#19260F",
        activeforeground="#AAABAA",
        width=40,
        font=("Arial", 20, "bold"), 
        anchor="w",
        command=music3_clicked
    )
    music3_button.place(x=390, y=290)
    

playlist3_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="Hindi",
    bg="#1A1A1A",
    fg="#666967",
    activebackground="green",
    activeforeground="#1A1A1A",
    width=15,
    font=("Arial", 20, "bold"), 
    command=playlist3_clicked
)
playlist3_button.place(x=20, y=380)



def playlist4_clicked() :
    
    global active_library
    active_library = 4
    
    frame5 = tk.Frame(root, bg="#060E08", width=1550, height=500)
    frame5.place(x=300,y=80)
    
    lab4 = Label(
        root,
        text="#Pop",
        fg="#5D734D",
        bg="#060E08",
        width=10,
        font=("Arial", 60),
    )
    lab4.place(x=350,y=120)

    frame4 = tk.Frame(root, bg="#5D734D", width=1000, height=1)
    frame4.place(x=370,y=250)
    
    def music_clicked() :
        
        lab7.config(text="")
        some_length = audio1.info.length
        mins = int(some_length // 60)
        secs = int(some_length % 60)
        lab7.configure(text=f"{mins}:{secs:02d}")
        selected_time = int(track_length.get())
        track_length.config(to=int(some_length))
        
        global play_button_clicked
        global active_song
        active_song = 1    
         

        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(start=selected_time)
        play_button.config(text="⏸")
        like_button.config(text="♡")
        if like_button1_clicked == False :
            like_button.config(text="♥")
        play_button_clicked = True

    music_button = tk.Button(
        root,
        relief=tk.FLAT,
        borderwidth=0, 
        text="|         Mary on a Cross",
        bg="#060E08",
        fg="#326935",
        activebackground="#19260F",
        activeforeground="#AAABAA",
        width=40,
        font=("Arial", 20, "bold"), 
        anchor="w",
        command=music_clicked
    )
    music_button.place(x=390, y=290)



    def music2_clicked() :
        
        lab7.config(text="")
        some_length = audio3.info.length
        mins = int(some_length // 60)
        secs = int(some_length % 60)
        lab7.configure(text=f"{mins}:{secs:02d}")
        selected_time = int(track_length.get())
        track_length.config(to=int(some_length))
        
        global play_button_clicked
        global active_song
        active_song = 3

        
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path_3)
        pygame.mixer.music.play(start=selected_time)
        play_button.config(text="⏸")
        like_button.config(text="♡")
        if like_button3_clicked == False :
            like_button.config(text="♥")
        play_button_clicked = True

    music2_button = tk.Button(
        root,
        relief=tk.FLAT,
        borderwidth=0, 
        text="|         Ticking Away",
        bg="#060E08",
        fg="#326935",
        activebackground="#19260F",
        activeforeground="#AAABAA",
        width=40,
        font=("Arial", 20, "bold"), 
        anchor="w",
        command=music2_clicked
    )
    music2_button.place(x=390, y=350)




    def music4_clicked() :
        
        lab7.config(text="")
        some_length = audio5.info.length
        mins = int(some_length // 60)
        secs = int(some_length % 60)
        lab7.configure(text=f"{mins}:{secs:02d}")
        selected_time = int(track_length.get())
        track_length.config(to=int(some_length))
        
        global play_button_clicked
        global active_song
        active_song = 5
        

        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path_5)
        pygame.mixer.music.play(start=selected_time)
        play_button.config(text="⏸")
        like_button.config(text="♡")
        if like_button5_clicked == False :
            like_button.config(text="♥")
        play_button_clicked = True

    music4_button = tk.Button(
        root,
        relief=tk.FLAT,
        borderwidth=0, 
        text="|         Level",
        bg="#060E08",
        fg="#326935",
        activebackground="#19260F",
        activeforeground="#AAABAA",
        width=40,
        font=("Arial", 20, "bold"), 
        anchor="w",
        command=music4_clicked
    )
    music4_button.place(x=390, y=410)
    

playlist4_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="Pop",
    bg="#1A1A1A",
    fg="#666967",
    activebackground="green",
    activeforeground="#1A1A1A",
    width=15,
    font=("Arial", 20, "bold"), 
    command=playlist4_clicked
)
playlist4_button.place(x=20, y=460)



def playlist5_clicked() :
    
    global active_library
    active_library = 5
    
    
    frame5 = tk.Frame(root, bg="#060E08", width=1550, height=500)
    frame5.place(x=300,y=80)
    
    lab4 = Label(
        root,
        text="#Anime",
        fg="#5D734D",
        bg="#060E08",
        width=10,
        font=("Arial", 60),
    )
    lab4.place(x=350,y=120)

    frame4 = tk.Frame(root, bg="#5D734D", width=1000, height=1)
    frame4.place(x=370,y=250)
    
    def music4_clicked() :
        
        lab7.config(text="")
        some_length = audio5.info.length
        mins = int(some_length // 60)
        secs = int(some_length % 60)
        lab7.configure(text=f"{mins}:{secs:02d}")
        selected_time = int(track_length.get())
        track_length.config(to=int(some_length))
        
        global play_button_clicked
        global active_song
        active_song = 5
        
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path_5)
        pygame.mixer.music.play(start=selected_time)
        play_button.config(text="⏸")
        like_button.config(text="♡")
        if like_button5_clicked == False :
            like_button.config(text="♥")
        play_button_clicked = True

    music4_button = tk.Button(
        root,
        relief=tk.FLAT,
        borderwidth=0, 
        text="|         Level",
        bg="#060E08",
        fg="#326935",
        activebackground="#19260F",
        activeforeground="#AAABAA",
        width=40,
        font=("Arial", 20, "bold"), 
        anchor="w",
        command=music4_clicked
    )
    music4_button.place(x=390, y=290)

playlist5_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="Anime",
    bg="#1A1A1A",
    fg="#666967",
    activebackground="green",
    activeforeground="#1A1A1A",
    width=15,
    font=("Arial", 20, "bold"), 
    command=playlist5_clicked
)
playlist5_button.place(x=20, y=540)




def like_clicked() :
    
    global like_button1_clicked
    global like_button2_clicked
    global like_button3_clicked
    global like_button4_clicked
    global like_button5_clicked
    global count
    global liked_song
    global active_song
    
        
    if active_song == 1 :
        if like_button1_clicked == True :
            like_button.config(text="♥")
            like_button1_clicked = False
            liked_song.insert(0,active_song)
            count += 60
        else :
            like_button.config(text="♡")
            like_button1_clicked = True
            liked_song.remove(active_song)
            count -= 60  
            
            
    if active_song == 2 :
        if like_button2_clicked == True :
            like_button.config(text="♥")
            like_button2_clicked = False
            liked_song.insert(1,active_song)
            count += 60
        else :
            like_button.config(text="♡")
            like_button2_clicked = True
            liked_song.remove(active_song)
            count -= 60  
            
            
    if active_song == 3 :
        if like_button3_clicked == True :
            like_button.config(text="♥")
            like_button3_clicked = False
            liked_song.insert(2,active_song)
            count += 60
        else :
            like_button.config(text="♡")
            like_button3_clicked = True
            liked_song.remove(active_song)
            count -= 60  
            
            
    if active_song == 4 :
        if like_button4_clicked == True :
            like_button.config(text="♥")
            like_button4_clicked = False
            liked_song.insert(3,active_song)
            count += 60
        else :
            like_button.config(text="♡")
            like_button4_clicked = True
            liked_song.remove(active_song)
            count -= 60  
            
            
    if active_song == 5 :
        if like_button5_clicked == True :
            like_button.config(text="♥")
            like_button5_clicked = False
            liked_song.insert(4,active_song)
            count += 60
        else :
            like_button.config(text="♡")
            like_button5_clicked = True
            liked_song.remove(active_song)
            count -= 60             
                          


like_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="♡",
    bg="#2F2F2E",
    fg="green",
    activebackground="#2F2F2E",
    activeforeground="green",
    width=3, 
    height=0, 
    font=("Arial", 30, "bold"), 
    command=like_clicked
)
like_button.place(x=40, y=717)
 

def sound_clicked() :
    global sound_button_clicked 
    
    
    if sound_button_clicked == False:
        
        sound_button.config(text="🔇")
        sound_button_clicked = True
        volume.set(0)
        
    else:
        
        sound_button.config(text="🔊")
        sound_button_clicked = False
        volume.set(75)

sound_button_clicked = False
sound_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="🔊",
    bg="#2F2F2E",
    fg="green",
    activebackground="#2F2F2E",
    activeforeground="green",
    width=3, 
    height=0, 
    font=("Arial", 25, "bold"), 
    command=sound_clicked
)
sound_button.place(x=200, y=717)

global volume_is 
def volume_setter(var) :
    
    global sound_button_clicked
    
    volume_is = int(var) / 100
    pygame.mixer.music.set_volume(volume_is)
    
    if int(var) > 0 :
        sound_button.config(text="🔊")
        sound_button_clicked = False

volume = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    bg="green",
    activebackground="green",
    sliderrelief=tk.FLAT,
    relief=tk.FLAT,
    sliderlength=20,
    borderwidth=0,
    highlightthickness=0,
    width=12,
    length=150,
    showvalue=0,
    troughcolor="#242424",
    command=volume_setter
)
volume.set(75)
volume_is = 75 / 100
pygame.mixer.music.set_volume(volume_is)
volume.place(x=270, y=750)


lab6 = Label(
root,
text="0:00",
fg="#E7E7E6",
bg="#343634",
width=5,
font=("Arial", 10),
)
lab6.place(x=125,y=687)


lab7 = Label(
root,
text="0:00",
fg="#E7E7E6",
bg="#343634",
width=5,
font=("Arial", 10),
)
lab7.place(x=1390,y=686)


def set_song_position(val):
    pygame.mixer.music.play(loops=0, start=float(val))

track_length = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    bg="green",
    activebackground="green",
    sliderrelief=tk.FLAT,
    relief=tk.FLAT,
    sliderlength=10,
    borderwidth=0,
    highlightthickness=0,
    width=14,
    length=1200,
    showvalue=0,
    troughcolor="#242424",
    command=set_song_position
)
track_length.set(0)
track_length.place(x=180, y=690)


def previous_clicked() :
    
    global play_button_clicked
    global active_library
    global active_song
    
    if active_library == 2 :
        
        if active_song == 1 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()
            active_song = 1
            play_button.config(text="⏸")
            play_button_clicked = True
            
        elif active_song == 2 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()
            active_song = 1
            play_button.config(text="⏸")
            play_button_clicked = True
            
        elif active_song == 3 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_2)
            pygame.mixer.music.play()
            active_song = 2
            play_button.config(text="⏸")
            play_button_clicked = True
            
    elif active_library == 3 :
        
        if active_song == 4 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_4)
            pygame.mixer.music.play()
            active_song = 4
            play_button.config(text="⏸")
            play_button_clicked = True
            
    elif active_library == 4 :
        
        if active_song == 1 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()
            active_song = 1
            play_button.config(text="⏸")
            play_button_clicked = True
            
        elif active_song == 3 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()
            active_song = 1
            play_button.config(text="⏸")
            play_button_clicked = True
            
        elif active_song == 5 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_3)
            pygame.mixer.music.play()
            active_song = 3
            play_button.config(text="⏸")
            play_button_clicked = True
            
    elif active_library == 5 :
        
        if active_song == 5 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_5)
            pygame.mixer.music.play()
            active_song = 5
            play_button.config(text="⏸")
            play_button_clicked = True
            
            
            
previous_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="⏮",
    bg="#2F2F2E",
    fg="green",
    activebackground="#2F2F2E",
    activeforeground="green",
    width=3, 
    height=0, 
    font=("Arial", 20, "bold"), 
    command=previous_clicked
)
previous_button.place(x=650, y=725)



def play_clicked() :
    global play_button_clicked 
    
    if play_button_clicked == False:
        
        pygame.mixer.music.unpause()
        play_button.config(text="⏸")
        play_button_clicked = True
        
    else:
        
        pygame.mixer.music.pause()
        play_button.config(text="▶")
        play_button_clicked = False

play_button_clicked = True
play_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="▶",
    bg="#2F2F2E",
    fg="green",
    activebackground="#2F2F2E",
    activeforeground="green",
    width=3, 
    height=0, 
    font=("Arial", 20, "bold"), 
    command=play_clicked
)
play_button.place(x=750, y=725)



def next_clicked() :
    
    global play_button_clicked
    global active_library
    global active_song
    
    if active_library == 2 :
        
        if active_song == 1 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_2)
            pygame.mixer.music.play()
            active_song = 2
            play_button.config(text="⏸")
            play_button_clicked = True
            
        elif active_song == 2 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_3)
            pygame.mixer.music.play()
            active_song = 3
            play_button.config(text="⏸")
            play_button_clicked = True
            
        elif active_song == 3 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_3)
            pygame.mixer.music.play()
            active_song = 3
            play_button.config(text="⏸")
            play_button_clicked = True
            
    elif active_library == 3 :
        
        if active_song == 4 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_4)
            pygame.mixer.music.play()
            active_song = 4
            play_button.config(text="⏸")
            play_button_clicked = True
            
    elif active_library == 4 :
        
        if active_song == 1 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_3)
            pygame.mixer.music.play()
            active_song = 3
            play_button.config(text="⏸")
            play_button_clicked = True
            
        elif active_song == 3 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_5)
            pygame.mixer.music.play()
            active_song = 5
            play_button.config(text="⏸")
            play_button_clicked = True
            
        elif active_song == 5 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_5)
            pygame.mixer.music.play()
            active_song = 5
            play_button.config(text="⏸")
            play_button_clicked = True
            
    elif active_library == 5 :
        
        if active_song == 5 :
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path_5)
            pygame.mixer.music.play()
            active_song = 5
            play_button.config(text="⏸")
            play_button_clicked = True
            
            
            
next_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="⏭",
    bg="#2F2F2E",
    fg="green",
    activebackground="#2F2F2E",
    activeforeground="green",
    width=3, 
    height=0, 
    font=("Arial", 20, "bold"), 
    command=next_clicked
)
next_button.place(x=850, y=725)
        


def repeat_clicked() :
    global repeat_button_clicked 
    
    if repeat_button_clicked == False:
        
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.pause()
        repeat_button.config(text="ထ")
        repeat_button_clicked = True
        
    else:
        
        repeat_button.config(text="⟳")
        repeat_button_clicked = False

repeat_button_clicked = False
repeat_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="⟳",
    bg="#2F2F2E",
    fg="green",
    activebackground="#2F2F2E",
    activeforeground="green",
    width=3, 
    height=0, 
    font=("Arial", 20, "bold"), 
    command=repeat_clicked
)
repeat_button.place(x=1370, y=730)



setting_button = tk.Button(
    root,
    relief=tk.FLAT,
    borderwidth=0, 
    text="☰",
    bg="#2F2F2E",
    fg="green",
    activebackground="#2F2F2E",
    activeforeground="green",
    width=3, 
    height=0, 
    font=("Arial", 20, "bold")
)
setting_button.place(x=1450, y=730)



root.mainloop()