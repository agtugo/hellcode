import genanki


def create_anki_deck(deck_name, notes):
    """Create an Anki deck with given notes."""
    deck = genanki.Deck(2039748058, deck_name)
    model = genanki.Model(
        476140248,
        "Hellcode Patterns",
        fields=[
            {"name": "Topic"},
            {"name": "Description"},
            {"name": "Iterative Steps"},
            {"name": "Iterative Code"},
            {"name": "Recursive Steps"},
            {"name": "Recursive Code"},
        ],
        templates=[
            {
                "name": "Topic and Description",
                "qfmt": "<h1>{{Topic}}</h1><p>{{Description}}</p>",
                "afmt": "{{FrontSide}}",
            },
            {
                "name": "Topic and Iterative Steps",
                "qfmt": "<h1>{{Topic}}</h1><p>{{Iterative Steps}}</p>",
                "afmt": "{{FrontSide}}<br><details><summary>Show Code</summary><pre>{{Iterative Code}}</pre></details>",
            },
            {
                "name": "Topic and Recursive Steps",
                "qfmt": "<h1>{{Topic}}</h1><p>{{Recursive Steps}}</p>",
                "afmt": "{{FrontSide}}<br><details><summary>Show Code</summary><pre>{{Recursive Code}}</pre></details>",
            },
        ],
    )

    for note_fields in notes:
        note = genanki.Note(model=model, fields=note_fields)
        deck.add_note(note)

    return deck
