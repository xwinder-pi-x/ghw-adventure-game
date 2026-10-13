from adventure import play


def run(moves):
    it = iter(moves)
    return play(input_fn=lambda _: next(it), print_fn=lambda *_: None)


def test_win_path():
    assert run(["1", "2", "1"]) == "win"


def test_lose_path():
    assert run(["2", "1"]) == "lose"


def test_invalid_input_then_win():
    assert run(["9", "1", "2", "1"]) == "win"
