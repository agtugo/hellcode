import genanki


def create_anki_deck(deck_name, notes):
    """Create an Anki deck with properly structured cards."""
    deck = genanki.Deck(2075209145, deck_name)  # ✅ Your Custom Deck ID

    # ✅ Model for Topic + Description
    description_model = genanki.Model(
        1590995667,  # ✅ Your Custom Model ID for Description
        "Hellcode Description Model",
        fields=[
            {"name": "Topic"},
            {"name": "Description"},
            {"name": "Tags"},
        ],
        templates=[
            {
                "name": "Topic and Description",
                "qfmt": "<h1>{{Topic}}</h1><p>{{Description}}</p>",
                "afmt": "{{FrontSide}}<br><br><b>Tags:</b> {{Tags}}",
            }
        ],
    )

    # ✅ Model for Iterative Steps
    iterative_model = genanki.Model(
        1134111604,  # ✅ Your Custom Model ID for Iterative
        "Hellcode Iterative Model",
        fields=[
            {"name": "Topic"},
            {"name": "Iterative Steps"},
            {"name": "Iterative Code"},
            {"name": "Tags"},
        ],
        templates=[
            {
                "name": "Topic and Iterative Steps",
                "qfmt": "<h1>{{Topic}}</h1><p>{{Iterative Steps}}</p>",
                "afmt": "{{FrontSide}}<br><details><summary>Show Code</summary><pre>{{Iterative Code}}</pre></details><br><b>Tags:</b> {{Tags}}",
            }
        ],
    )

    # ✅ Model for Recursive Steps
    recursive_model = genanki.Model(
        1420682326,  # ✅ Your Custom Model ID for Recursive
        "Hellcode Recursive Model",
        fields=[
            {"name": "Topic"},
            {"name": "Recursive Steps"},
            {"name": "Recursive Code"},
            {"name": "Tags"},
        ],
        templates=[
            {
                "name": "Topic and Recursive Steps",
                "qfmt": "<h1>{{Topic}}</h1><p>{{Recursive Steps}}</p>",
                "afmt": "{{FrontSide}}<br><details><summary>Show Code</summary><pre>{{Recursive Code}}</pre></details><br><b>Tags:</b> {{Tags}}",
            }
        ],
    )

    for note_fields in notes:
        topic, desc, iter_steps, iter_code, rec_steps, rec_code, tags = note_fields

        # Ensure tags are stored as a properly formatted string
        tags_str = " ".join(tags.split()) if tags else ""

        # ✅ Create the main Topic-Description card
        if desc.strip():
            note_main = genanki.Note(
                model=description_model,
                fields=[topic, desc, tags_str],
            )
            deck.add_note(note_main)

        # ✅ Create the Iterative Steps card **only if there's content**
        if iter_steps.strip():
            note_iter = genanki.Note(
                model=iterative_model,
                fields=[topic, iter_steps, iter_code, tags_str],
            )
            deck.add_note(note_iter)

        # ✅ Create the Recursive Steps card **only if there's content**
        if rec_steps.strip():
            note_rec = genanki.Note(
                model=recursive_model,
                fields=[topic, rec_steps, rec_code, tags_str],
            )
            deck.add_note(note_rec)

    return deck
