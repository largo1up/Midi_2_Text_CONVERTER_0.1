import mido
from mido import MidiFile
import tkinter as tk
from tkinter import filedialog, scrolledtext

def midi_to_text(midi_file):
    midi = MidiFile(midi_file)
    note_data = []

    for track in midi.tracks:
        current_time = 0
        for msg in track:
            current_time += msg.time
            if msg.type == 'note_on':
                note_data.append((msg.note, msg.velocity, current_time))

    return note_data

def choose_midi_file():
    midi_file = filedialog.askopenfilename(
        title = "Select MIDI File",
        filetypes = [("MIDI Files", "*.mid"), ("All Files", "*.*")])
    return midi_file

def convert_midi_to_text():
    midi_file = choose_midi_file()
    if midi_file:
        note_data = midi_to_text(midi_file)
        note_data_text.configure(state='normal')
        note_data_text.delete(1.0, tk.END)
        for note, velocity, time in note_data:
            note_data_text.insert(tk.END, f"Note: {note}, Velocity: {velocity}, Time: {time}\n")
        note_data_text.configure(state='disabled')

def save_note_data():
    note_data = note_data_text.get(1.0, tk.END)
    save_file = filedialog.asksaveasfilename(
        title = "Save Note Data",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if save_file:
        with open(save_file, 'w') as f:
            f.write(note_data)

root = tk.Tk()
root.title("MIDI to Text Converter")

button = tk.Button(root, text="Choose MIDI File", command=convert_midi_to_text)
button.pack(padx=20, pady=10)

note_data_text = scrolledtext.ScrolledText(root, width=50, height=20)
note_data_text.pack(padx=20, pady=10)
note_data_text.configure(state='disabled')

save_button = tk.Button(root, text="Save Note Data", command=save_note_data)
save_button.pack(padx=20, pady=10)

root.mainloop()

import time
time.sleep(5)
