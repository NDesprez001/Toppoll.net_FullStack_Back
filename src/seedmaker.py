    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 6,
        username = "kolis10",
        poll_name = "What element would you want to control?",
        option_picked = "Earth"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 6,
        username = "Naz",
        poll_name = "What element would you want to control?",
        option_picked = "Air"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 6,
        username = "Curly-Fry",
        poll_name = "What element would you want to control?",
        option_picked = "Water"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 6,
        username = "Coder",
        poll_name = "What element would you want to control?",
        option_picked = "Water"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 6,
        username = "Rager",
        poll_name = "What element would you want to control?",
        option_picked = "Fire"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 6,
        username = "Tony",
        poll_name = "What element would you want to control?",
        option_picked = "Fire"
    ))


    db.session.add(Polls(
        creator_user = Anthony,
        poll_question = "What element would you want to control?",
        poll_description = "Is this is very important information? No, but it's fun.",
        info_link = "",
        image_link = "",
        option1 = "Water",
        option2 = "Earth",
        option3 = "Fire",
        option4 = "Air"
    ))