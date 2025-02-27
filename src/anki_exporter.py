import genanki


def create_anki_deck(deck_name, notes):
    """Create an Anki deck with given notes."""
    deck = genanki.Deck(2075209145, deck_name)
    model = genanki.Model(
        1337108008,
        "Hellcode Patterns",
        fields=[
            {"name": "Topic"},
            {"name": "Description"},
            {"name": "Iterative Steps"},
            {"name": "Iterative Code"},
            {"name": "Recursive Steps"},
            {"name": "Recursive Code"},
            {"name": "Tags"},
        ],
        templates=[
            {
                "name": "Topic and Description",
                "qfmt": "<h1>{{Topic}}</h1>",
                "afmt": "{{FrontSide}}</h1><p>{{Description}}</p><br><br><b>Tags:</b> {{Tags}}",
            },
            {
                "name": "Topic and Iterative Steps",
                "qfmt": "<h1>{{Topic}}</h1>",
                "afmt": "{{FrontSide}}<br><p>{{Iterative Steps}}</p><br><details><summary>Show Code</summary><pre>{{Iterative Code}}</pre></details><br><b>Tags:</b> {{Tags}}",
            },
            {
                "name": "Topic and Recursive Steps",
                "qfmt": "<h1>{{Topic}}</h1>",
                "afmt": "{{FrontSide}}<br><p>{{Recursive Steps}}</p><br><details><summary>Show Code</summary><pre>{{Recursive Code}}</pre></details><br><b>Tags:</b> {{Tags}}",
            },
        ],
    )

    for note_fields in notes:
        topic, desc, iter_steps, iter_code, rec_steps, rec_code, tags = note_fields

        tags_str = " ".join(tags.split()) if tags else ""

        # Create the main Topic-Description card
        note_main = genanki.Note(
            model=model,
            fields=[topic, desc, "", "", "", "", tags_str],
        )
        deck.add_note(note_main)

        # Create the Iterative Steps card **only if there's content**
        if iter_steps.strip():
            note_iter = genanki.Note(
                model=model,
                fields=[
                    topic,
                    "",
                    iter_steps,
                    iter_code,
                    "",
                    "",
                    tags_str,
                ],
            )
            deck.add_note(note_iter)

        # Create the Recursive Steps card **only if there's content**
        if rec_steps.strip():
            note_rec = genanki.Note(
                model=model,
                fields=[
                    topic,
                    "",
                    "",
                    "",
                    rec_steps,
                    rec_code,
                    tags_str,
                ],
            )
            deck.add_note(note_rec)

    return deck
