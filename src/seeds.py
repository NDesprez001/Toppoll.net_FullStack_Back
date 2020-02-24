from models import db, Users
def run():

    Users.query.delete()
    
    db.session.execute("ALTER TABLE users AUTO_INCREMENT = 1")

    db.session.add(Users(
        first_name = 'Issac',
        last_name = 'Alleyne',
        username = 'kolis10',
        password = 'Awesom3',
        date_of_birth = '10/22/1994',
        email = 'issacalleyne@gmail.com'
    ))
    db.session.add(Users(
        first_name = 'Nhinhoshxhy',
        last_name = 'Desprez',
        username = 'Noz',
        password = 'HHH',
        date_of_birth = '1/2/1999',
        email = 'noztril@gmail.com'
    ))
    db.session.add(Users(
        first_name = 'Chouerlee',
        last_name = 'Victor',
        username = 'Curly-Fry',
        password = 'Fry',
        date_of_birth = '10/12/1997',
        email = 'curly@gmail.com'
    ))
    db.session.add(Users(
        first_name = 'Zion',
        last_name = 'Raymond',
        username = 'Coder',
        password = 'Zee',
        date_of_birth = '1/33/1998',
        email = 'coderzee@gmail.com'
    ))
    db.session.add(Users(
        first_name = 'Rajae',
        last_name = 'Lindsay',
        username = 'Rager',
        password = '$$',
        date_of_birth = '4/4/1996',
        email = 'ceo?@gmail.com'
    ))
    db.session.add(Users(
        first_name = 'Anthony',
        last_name = 'Smith',
        username = 'Tony',
        password = 'Dez',
        date_of_birth = '1/23/1995',
        email = 'anthony@gmail.com'
    ))
    db.session.commit()
    return 'seeds ran successfully'