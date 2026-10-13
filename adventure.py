#!/usr/bin/env python3
"""The Lost Lighthouse - a tiny choose-your-own-adventure game."""

STORY = {
    "start": ("You wake on a foggy beach. A dark lighthouse stands to the north, "
              "a forest path leads east.", {"1": ("Walk to the lighthouse", "lighthouse"),
                                            "2": ("Follow the forest path", "forest")}),
    "lighthouse": ("The lighthouse door is locked, but a window is open.",
                   {"1": ("Climb through the window", "stairs"),
                    "2": ("Knock and wait", "keeper")}),
    "keeper": ("An old keeper opens the door and hands you a lamp. 'Light the beacon, "
               "a ship is lost!'", {"1": ("Run up the stairs", "beacon")}),
    "stairs": ("You climb in the dark and slip on a loose step...", {}),
    "forest": ("The path splits by a glowing mushroom ring.",
               {"1": ("Step into the ring", "fairy"),
                "2": ("Go back to the beach", "start")}),
    "fairy": ("You are whisked away to a fairy feast forever. Not bad, but the ship is lost.", {}),
    "beacon": ("You light the beacon. The ship turns safely toward harbor. You win!", {}),
}
ENDINGS = {"stairs": "lose", "fairy": "lose", "beacon": "win"}


def play(input_fn=input, print_fn=print):
    scene = "start"
    while True:
        text, choices = STORY[scene]
        print_fn("\n" + text)
        if not choices:
            print_fn("*** You " + ("WIN" if ENDINGS.get(scene) == "win" else "lose") + "! ***")
            return ENDINGS.get(scene)
        for key, (label, _) in choices.items():
            print_fn(f"  {key}) {label}")
        choice = input_fn("> ").strip()
        if choice in choices:
            scene = choices[choice][1]
        else:
            print_fn("Please pick one of the listed numbers.")


if __name__ == "__main__":
    play()
