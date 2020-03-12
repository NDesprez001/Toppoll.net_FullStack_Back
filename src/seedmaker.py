    ##################
    #     POLLS
    ##################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 8,
        username = "kolis10",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Telekinesis"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 8,
        username = "Naz",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Super Strength"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 8,
        username = "Curly-Fry",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Flight"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 8,
        username = "Coder",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Flight"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 8,
        username = "Rager",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Super Strength"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 8,
        username = "Tony",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Invisibility"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 8,
        username = "Garcia Sausage",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Telekinesis"
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 8,
        username = "Boss Mom",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Invisibility"
    ))


    db.session.add(Polls(
        creator_user = Ms_Achille,
        poll_question = "If you could have one of these superpowers, which one would you choose?",
        poll_description = "We've all dreamt of having superpowers and being more than ordinary; which of these abilities fits you best?",
        info_link = "",
        image_link = "https://images.pexels.com/photos/346796/pexels-photo-346796.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "Invisibility",
        option2 = "Super Strength",
        option3 = "Flight",
        option4 = "Telekinesis"
    ))