import tkinter as tk
import random

hiragana = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "wo", "ん": "n"
}

class HiraganaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hiragana Flashcards")

        self.score = 0
        self.total = 0

        self.current_kana = ""
        self.current_answer = ""

        self.label = tk.Label(root, text="", font=("Arial", 48))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 20))
        self.entry.pack()
        self.entry.bind("<Return>", self.check_answer)

        self.result = tk.Label(root, text="", font=("Arial", 14))
        self.result.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0/0", font=("Arial", 12))
        self.score_label.pack()

        self.next_card()

    def next_card(self):
        self.current_kana, self.current_answer = random.choice(list(hiragana.items()))
        self.label.config(text=self.current_kana)
        self.entry.delete(0, tk.END)
        self.result.config(text="")
        self.entry.focus()

    def check_answer(self, event=None):
        user_input = self.entry.get().strip().lower()
        self.total += 1

        if user_input == self.current_answer:
            self.result.config(text="✅ Correct!", fg="green")
            self.score += 1
        else:
            self.result.config(
                text=f"❌ Wrong! Answer: {self.current_answer}",
                fg="red"
            )

        self.score_label.config(text=f"Score: {self.score}/{self.total}")

        # ⏱ Auto move to next card after 1 second
        self.root.after(1000, self.next_card)


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = HiraganaApp(root)
    root.mainloop()
