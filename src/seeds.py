from models import db, Users, Polls, Voters_Table
import utils
def run():

    Voters_Table.query.delete()   #Arrange the deletes in the opposite order of the models
    Polls.query.delete()
    Users.query.delete()
    
    db.session.execute("ALTER TABLE polls AUTO_INCREMENT = 1")
    db.session.execute("ALTER TABLE users AUTO_INCREMENT = 1")
    db.session.execute("ALTER TABLE voters_table AUTO_INCREMENT = 1")

    ##################
    #     USERS
    ##################
    Issac = Users(
        first_name = 'Issac',
        last_name = 'Alleyne',
        username = 'kolis10',
        password = utils.sha256('Awesom3'),
        date_of_birth = '10/22/1994',
        email = 'issacalleyne@gmail.com'
    )
    db.session.add(Issac)
    Naz = Users(
        first_name = 'Nhinhoshxhy',
        last_name = 'Desprez',
        username = 'Naz',
        password = utils.sha256('HHH'),
        date_of_birth = '1/2/1999',
        email = 'noztril@gmail.com'
    )
    db.session.add(Naz)
    Chouerlee = Users(
        first_name = 'Chouerlee',
        last_name = 'Victor',
        username = 'Curly-Fry',
        password = utils.sha256('Fry'),
        date_of_birth = '10/12/1997',
        email = 'curly@gmail.com'
    )
    db.session.add(Chouerlee)
    Zion = Users(
        first_name = 'Zion',
        last_name = 'Raymond',
        username = 'Coder',
        password = utils.sha256('Zee'),
        date_of_birth = '1/33/1998',
        email = 'coderzee@gmail.com'
    )
    db.session.add(Zion)
    Rajae = Users(
        first_name = 'Rajae',
        last_name = 'Lindsay',
        username = 'Rager',
        password = utils.sha256('$$'),
        date_of_birth = '4/4/1996',
        email = 'ceo?@gmail.com'
    )
    db.session.add(Rajae)
    Anthony = Users(
        first_name = 'Anthony',
        last_name = 'Smith',
        username = 'Tony',
        password = utils.sha256('Dez'),
        date_of_birth = '1/23/1995',
        email = 'anthony@gmail.com'
    )
    db.session.add(Anthony)

    ##################
    #     POLLS
    ##################
    db.session.add(Polls(
        creator_user = Chouerlee,
        poll_question = "Who would you want to do your front-end?",
        poll_description = "Naz and Anthony both think themselves artists when it comes to web design, but we're gonna see who's the class favorite",
        info_link = "",
        option1 = "Naz",
        option2 = "Anthony",
        option3 = "Zion???",
        option4 = "They're all overrated"
    ))
    db.session.add(Polls(
        creator_user = Issac,
        poll_question = "Which do you prefer; front-end or back-end?",
        poll_description = "Since the beginning of this class we've been divided on whether or not coding a webpage's data is more enjoyable than building the layout of the page.",
        info_link = "",
        option1 = "Front-End",
        option2 = "Back-End",
        option3 = "I like them equally",
        option4 = "I really don't care"
    ))
    db.session.add(Polls(
        creator_user = Naz,
        poll_question = "Are Even numbers better than Odd numbers?",
        poll_description = "This is dumb",
        info_link = "",
        option1 = "Evens are Better",
        option2 = "Odds are Awesome",
        option3 = "This is really dumb"
    ))
    db.session.add(Polls(
        creator_user = Zion,
        poll_question = "Does Zion really need to come to class?",
        poll_description = "Zion has ditched 3 days in a row, should we be concerned",
        info_link = "",
        option1 = "Nah, let him spend time with his girl!",
        option2 = "His future is important, get his ass in class",
        option3 = "I forgot Zion was in this class"
    ))
    db.session.add(Polls(
        creator_user = Rajae,
        poll_question = "How rich will Rajae be?",
        poll_description = "We all know Raj is gonna make it big, the question is; how big?",
        info_link = "https://media1.giphy.com/media/PyZEkItObZrnW/giphy.gif",
        option1 = "Millionaire",
        option2 = "Billionaire",
        option3 = "So rich they have to make up a new number for it",
        option4 = "Middle Class at best"
    ))
    db.session.add(Polls(
        creator_user = Anthony,
        poll_question = "Do these pants make Anthony's ass look big?",
        poll_description = "This is very important information?",
        info_link = "",
        option1 = "Yes",
        option2 = "Nah",
        option3 = "They make you look gay"
    ))

    ##################
    #  VOTERS_TABLE
    ##################

    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 1,
        username = "kolis10",
        poll_name = "Who would you want to do your front-end?",
        option_picked = "Naz"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 1,
        username = "Naz",
        poll_name = "Who would you want to do your front-end?",
        option_picked = "Naz"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 1,
        username = "Curly-Fry",
        poll_name = "Who would you want to do your front-end?",
        option_picked = "Anthony"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 1,
        username = "Coder",
        poll_name = "Who would you want to do your front-end?",
        option_picked = "Zion???"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 1,
        username = "Rager",
        poll_name = "Who would you want to do your front-end?",
        option_picked = "They're all overrated"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 1,
        username = "Tony",
        poll_name = "Who would you want to do your front-end?",
        option_picked = "Anthony"
    ))
    #########################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 2,
        username = "kolis10",
        poll_name = "Which do you prefer; front-end or back-end?",
        option_picked = "Back-End"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 2,
        username = "Naz",
        poll_name = "Which do you prefer; front-end or back-end?",
        option_picked = "I like them equally"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 2,
        username = "Curly-Fry",
        poll_name = "Which do you prefer; front-end or back-end?",
        option_picked = "Front-End"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 2,
        username = "Coder",
        poll_name = "Which do you prefer; front-end or back-end?",
        option_picked = "I like them equally"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 2,
        username = "Rager",
        poll_name = "Which do you prefer; front-end or back-end?",
        option_picked = "I like them equally"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 2,
        username = "Tony",
        poll_name = "Which do you prefer; front-end or back-end?",
        option_picked = "Front-End"
    ))
    ######################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 3,
        username = "kolis10",
        poll_name = "Are Even numbers better than Odd numbers?",
        option_picked = "This is really dumb"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 3,
        username = "Naz",
        poll_name = "Are Even numbers better than Odd numbers?",
        option_picked = "Evens are Better"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 3,
        username = "Curly-Fry",
        poll_name = "Are Even numbers better than Odd numbers?",
        option_picked = "Evens are Better"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 3,
        username = "Coder",
        poll_name = "Are Even numbers better than Odd numbers?",
        option_picked = "Odds are Awesome"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 3,
        username = "Rager",
        poll_name = "Are Even numbers better than Odd numbers?",
        option_picked = "Evens are Better"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 3,
        username = "Tony",
        poll_name = "Are Even numbers better than Odd numbers?",
        option_picked = "This is really dumb"
    ))
    ########################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 4,
        username = "kolis10",
        poll_name = "Does Zion really need to come to class?",
        option_picked = "His future is important, get his ass in class"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 4,
        username = "Naz",
        poll_name = "Does Zion really need to come to class?",
        option_picked = "His future is important, get his ass in class"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 4,
        username = "Curly-Fry",
        poll_name = "Does Zion really need to come to class?",
        option_picked = "His future is important, get his ass in class"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 4,
        username = "Coder",
        poll_name = "Does Zion really need to come to class?",
        option_picked = "Nah, let him spend time with his girl!"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 4,
        username = "Rager",
        poll_name = "Does Zion really need to come to class?",
        option_picked = "His future is important, get his ass in class"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 4,
        username = "Tony",
        poll_name = "Does Zion really need to come to class?",
        option_picked = "I forgot Zion was in this class"
    ))
    ###########################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 5,
        username = "kolis10",
        poll_name = "How rich will Rajae be?",
        option_picked = "Middle Class at best"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 5,
        username = "Naz",
        poll_name = "How rich will Rajae be?",
        option_picked = "Millionaire"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 5,
        username = "Curly-Fry",
        poll_name = "How rich will Rajae be?",
        option_picked = "Middle Class at best"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 5,
        username = "Coder",
        poll_name = "How rich will Rajae be?",
        option_picked = "Middle Class at best"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 5,
        username = "Rager",
        poll_name = "How rich will Rajae be?",
        option_picked = "So rich they have to make up a new number for it"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 5,
        username = "Tony",
        poll_name = "How rich will Rajae be?",
        option_picked = "Middle Class at best"
    ))
    ######################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 6,
        username = "kolis10",
        poll_name = "Do these pants make Anthony's ass look big?",
        option_picked = "They make you look gay"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 6,
        username = "Naz",
        poll_name = "Do these pants make Anthony's ass look big?",
        option_picked = "Nah"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 6,
        username = "Curly-Fry",
        poll_name = "Do these pants make Anthony's ass look big?",
        option_picked = "Yes"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 6,
        username = "Coder",
        poll_name = "Do these pants make Anthony's ass look big?",
        option_picked = "Nah"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 6,
        username = "Rager",
        poll_name = "Do these pants make Anthony's ass look big?",
        option_picked = "They make you look gay"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 6,
        username = "Tony",
        poll_name = "Do these pants make Anthony's ass look big?",
        option_picked = "Yes"
    ))
    db.session.commit()
    return 'seeds ran successfully'