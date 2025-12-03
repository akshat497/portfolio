#!/usr/bin/env python3
"""
QuizPro: Console-Based Trivia

Features:
 - Categories & difficulty
 - Randomized question order & options
 - Lifelines: 50-50, Ask the Audience, Skip
 - Tracks score & saves high scores in highscores.json
 - Easily extendable question bank (list of dicts below or load from JSON)
"""

import json
import random
import os
from datetime import datetime

# -------------------------
# ---------- CONFIG --------
# -------------------------
HIGHSCORE_FILE = "highscores.json"

# ANSI colors (works on most terminals)
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"

# -------------------------
# ---- SAMPLE QUESTIONS----
# -------------------------
# Each question: text, options (dict key->text), answer (key), category, difficulty
QUESTION_BANK = [
    {
        "text": "What is the capital of France?",
        "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
        "answer": "C",
        "category": "Geography",
        "difficulty": "Easy"
    },
    {
        "text": "Which built-in Python type is immutable?",
        "options": {"A": "list", "B": "set", "C": "dict", "D": "tuple"},
        "answer": "D",
        "category": "Programming",
        "difficulty": "Easy"
    },
    {
        "text": "Who wrote 'Pride and Prejudice'?",
        "options": {"A": "Jane Austen", "B": "Charlotte Brontë", "C": "George Eliot", "D": "Mary Shelley"},
        "answer": "A",
        "category": "Literature",
        "difficulty": "Medium"
    },
    {
        "text": "What is the 8-bit binary for decimal 13?",
        "options": {"A": "00001101", "B": "00001011", "C": "00001110", "D": "00000111"},
        "answer": "A",
        "category": "Computers",
        "difficulty": "Medium"
    },
    {
        "text": "Which gas is most abundant in the Earth's atmosphere?",
        "options": {"A": "Oxygen", "B": "Nitrogen", "C": "Argon", "D": "Carbon Dioxide"},
        "answer": "B",
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "text": "Who proposed the theory of general relativity?",
        "options": {"A": "Isaac Newton", "B": "Albert Einstein", "C": "Niels Bohr", "D": "Galileo Galilei"},
        "answer": "B",
        "category": "Science",
        "difficulty": "Medium"
    },
    {
        "text": "Which year did the first man land on the Moon?",
        "options": {"A": "1965", "B": "1969", "C": "1971", "D": "1959"},
        "answer": "B",
        "category": "History",
        "difficulty": "Easy"
    },
    {
        "text": "In CSS, which property controls the horizontal space between letters?",
        "options": {"A": "letter-spacing", "B": "word-spacing", "C": "text-indent", "D": "line-height"},
        "answer": "A",
        "category": "Web",
        "difficulty": "Medium"
    },
    {
        "text": "What is the output of: len({'a':1,'b':2}) in Python?",
        "options": {"A": "1", "B": "2", "C": "3", "D": "Error"},
        "answer": "B",
        "category": "Programming",
        "difficulty": "Easy"
    },
    {
        "text": "Which city hosted the 2016 Summer Olympics?",
        "options": {"A": "Tokyo", "B": "Rio de Janeiro", "C": "London", "D": "Beijing"},
        "answer": "B",
        "category": "Sports",
        "difficulty": "Easy"
    }
]

# -------------------------
# ----- Persistence -------
# -------------------------
def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    try:
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_highscores(scores):
    with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)

# -------------------------
# ---- Utility Functions---
# -------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def prompt_enter():
    input(f"\n{C.CYAN}Press Enter to continue...{C.RESET}")

def print_banner():
    print(f"{C.BOLD}{C.CYAN}=== QuizPro ==={C.RESET}\n")

def get_categories_and_difficulties(bank):
    cats = sorted({q["category"] for q in bank})
    diffs = sorted({q["difficulty"] for q in bank})
    return cats, diffs

# -------------------------
# ------ Lifelines --------
# -------------------------
class Lifelines:
    def __init__(self):
        self.available = {"50-50": True, "audience": True, "skip": True}

    def use_5050(self, question):
        if not self.available["50-50"]:
            return None
        self.available["50-50"] = False
        # Keep the correct option and one random wrong option
        correct = question["answer"]
        wrongs = [k for k in question["options"].keys() if k != correct]
        choice = random.choice(wrongs)
        kept = sorted([correct, choice])
        return {k: question["options"][k] for k in kept}

    def use_audience(self, question):
        if not self.available["audience"]:
            return None
        self.available["audience"] = False
        # Simulate audience poll: favor correct answer
        keys = list(question["options"].keys())
        weights = [10] * len(keys)
        correct_idx = keys.index(question["answer"])
        # boost correct
        weights[correct_idx] += 60
        # normalize to percentages
        total = sum(weights)
        percentages = [int(w * 100 / total) for w in weights]
        # fix rounding residuals
        diff = 100 - sum(percentages)
        percentages[0] += diff
        poll = dict(zip(keys, percentages))
        return poll

    def use_skip(self):
        if not self.available["skip"]:
            return False
        self.available["skip"] = False
        return True

# -------------------------
# ----- Quiz Engine -------
# -------------------------
def play_quiz(question_bank):
    clear_screen()
    print_banner()

    name = input("Enter your name: ").strip() or "Player"
    cats, diffs = get_categories_and_difficulties(question_bank)

    # Choose category
    print("\nChoose category:")
    print("0) All")
    for i, c in enumerate(cats, 1):
        print(f"{i}) {c}")
    cat_choice = input("Select (number): ").strip()
    try:
        cat_idx = int(cat_choice)
    except:
        cat_idx = 0
    chosen_cat = None if cat_idx == 0 else (cats[cat_idx - 1] if 1 <= cat_idx <= len(cats) else None)

    # Choose difficulty
    print("\nChoose difficulty:")
    print("0) All")
    for i, d in enumerate(diffs, 1):
        print(f"{i}) {d}")
    diff_choice = input("Select (number): ").strip()
    try:
        diff_idx = int(diff_choice)
    except:
        diff_idx = 0
    chosen_diff = None if diff_idx == 0 else (diffs[diff_idx - 1] if 1 <= diff_idx <= len(diffs) else None)

    # Filter questions
    pool = [q.copy() for q in question_bank
            if (chosen_cat is None or q["category"] == chosen_cat)
            and (chosen_diff is None or q["difficulty"] == chosen_diff)]
    if not pool:
        print(f"{C.RED}No questions match your selection. Exiting.{C.RESET}")
        return

    # Shuffle options inside each question
    for q in pool:
        # Convert options into list of (key, text), shuffle their order but keep keys as A.. etc.
        items = list(q["options"].items())
        random.shuffle(items)
        # Reassign keys to standard A.. based on current order
        new_keys = ["A", "B", "C", "D"][:len(items)]
        new_options = {}
        map_old_to_new = {}
        for new_k, (old_k, text) in zip(new_keys, items):
            new_options[new_k] = text
            map_old_to_new[old_k] = new_k
        # update answer (map old key to new key)
        new_answer = map_old_to_new[q["answer"]]
        q["options"] = new_options
        q["answer"] = new_answer

    random.shuffle(pool)
    total_questions = min(len(pool), 10)  # limit to 10 questions for play
    score = 0
    lifelines = Lifelines()

    for idx in range(total_questions):
        clear_screen()
        q = pool[idx]
        print_banner()
        print(f"{C.BOLD}Player:{C.RESET} {name}    {C.BOLD}Score:{C.RESET} {score}")
        print(f"\nQuestion {idx+1}/{total_questions} — {q['category']} / {q['difficulty']}")
        print(f"\n{q['text']}\n")

        # display options
        def show_options(opts):
            for k, v in sorted(opts.items()):
                print(f"  {C.YELLOW}{k}{C.RESET}) {v}")
        show_options(q["options"])

        # show available lifelines
        available = [k for k, v in lifelines.available.items() if v]
        if available:
            print(f"\nLifelines available: {', '.join(available)}")
            print("Type lifeline name to use it (e.g. 50-50), or type A/B/C/D to answer.")

        answered = False
        while not answered:
            user = input("\nYour answer: ").strip()
            if not user:
                continue
            u = user.upper()

            # lifeline use
            if u in ("50-50", "5050", "50"):
                result = lifelines.use_5050(q)
                if result is None:
                    print(f"{C.RED}50-50 already used.{C.RESET}")
                else:
                    print(f"{C.CYAN}50-50 applied — two options kept:{C.RESET}")
                    show_options(result)
                continue
            if u in ("AUDIENCE", "ASK", "AUDIO"):
                poll = lifelines.use_audience(q)
                if poll is None:
                    print(f"{C.RED}Audience lifeline already used.{C.RESET}")
                else:
                    print(f"{C.CYAN}Audience poll (percentages):{C.RESET}")
                    for k, v in poll.items():
                        print(f"  {k}: {v}%")
                continue
            if u in ("SKIP", "S"):
                ok = lifelines.use_skip()
                if not ok:
                    print(f"{C.RED}Skip already used.{C.RESET}")
                else:
                    print(f"{C.CYAN}Question skipped. No points awarded.{C.RESET}")
                    answered = True
                continue

            # treat as answer
            if u in q["options"].keys():
                if u == q["answer"]:
                    print(f"\n{C.GREEN}Correct! +10 points{C.RESET}")
                    score += 10
                else:
                    print(f"\n{C.RED}Wrong!{C.RESET} Correct answer was {C.BOLD}{q['answer']}{C.RESET}) {q['options'][q['answer']]}")
                answered = True
            else:
                print(f"{C.RED}Invalid input. Choose A/B/C/D or a lifeline.{C.RESET}")

        # small pause between questions
        prompt_enter()

    # Quiz finished
    clear_screen()
    print_banner()
    print(f"{C.BOLD}Final Score for {name}:{C.RESET} {score}\n")

    # Save high score
    highs = load_highscores()
    highs.append({"name": name, "score": score, "date": datetime.now().isoformat()})
    highs = sorted(highs, key=lambda x: x["score"], reverse=True)[:10]  # keep top 10
    save_highscores(highs)

    print(f"{C.CYAN}Top Scores:{C.RESET}")
    for i, rec in enumerate(highs, 1):
        print(f" {i}. {rec['name']} — {rec['score']} ({rec['date'][:19]})")

    print("\nThanks for playing QuizPro!")
    prompt_enter()

# -------------------------
# --------- MAIN ----------
# -------------------------
def main():
    while True:
        clear_screen()
        print_banner()
        print("1) Play Quiz")
        print("2) View High Scores")
        print("3) Add Custom Questions (JSON file)")
        print("4) Quit")
        choice = input("\nSelect: ").strip()
        if choice == "1":
            play_quiz(QUESTION_BANK)
        elif choice == "2":
            highs = load_highscores()
            if highs:
                clear_screen()
                print_banner()
                print("High Scores (Top 10):\n")
                for i, rec in enumerate(highs, 1):
                    print(f"{i}. {rec['name']} — {rec['score']} ({rec['date'][:19]})")
            else:
                print("No scores yet.")
            prompt_enter()
        elif choice == "3":
            # helper: asks for path to JSON. JSON should be list of questions like QUESTION_BANK entries.
            path = input("Enter path to JSON file containing questions: ").strip()
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # basic validation
                if isinstance(data, list) and all("text" in q and "options" in q and "answer" in q for q in data):
                    QUESTION_BANK.extend(data)
                    print(f"{C.GREEN}Loaded {len(data)} questions into the pool.{C.RESET}")
                else:
                    print(f"{C.RED}Invalid format in JSON. Expected a list of question objects.{C.RESET}")
            except Exception as e:
                print(f"{C.RED}Failed to load file: {e}{C.RESET}")
            prompt_enter()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            prompt_enter()

if __name__ == "__main__":
    main()
