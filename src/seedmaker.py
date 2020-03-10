    ##################
    #     CHATS
    ##################
    db.session.add(Messages(
        poll_id = 1,
        username = "kolis10",
        message = "'Sup",
        created_at = now
    ))
    db.session.add(Messages(
        poll_id = 2,
        username = "Naz",
        message = "Konichiwa",
        created_at = now
    ))
    db.session.add(Messages(
        poll_id = 3,
        username = "Curly-Fry",
        message = "Hey",
        created_at = now
    ))
    db.session.add(Messages(
        poll_id = 4,
        username = "Coder",
        message = "Dude",
        created_at = now
    ))
    db.session.add(Messages(
        poll_id = 5,
        username = "Rager",
        message = "Yo",
        created_at = now
    ))
    db.session.add(Messages(
        poll_id = 6,
        username = "Tony",
        message = "Hi",
        created_at = now
    ))
    ############################################
    db.session.add(Messages(
        poll_id = 1,
        username = "Naz",
        message = "Konichiwa, kolis10",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        poll_id = 2,
        username = "kolis10",
        message = "'Sup, Naz",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        poll_id = 3,
        username = "Tony",
        message = "Hi, Curly-Fry",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        poll_id = 4,
        username = "Rager",
        message = "Yo, Coder",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        poll_id = 5,
        username = "Coder",
        message = "Dude, Rager",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        poll_id = 6,
        username = "Curly-Fry",
        message = "Hey, Tony",
        created_at = now + timedelta(minutes=2)
    ))