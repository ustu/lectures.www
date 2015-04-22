# -*- coding: utf-8 -*-
from pprint import pprint
from common import get_session

if '__main__' in __name__:
    """Test if the data is actually persistent across requests"""
    session = get_session()
    session['Suomi'] = 'Kimi Räikkönen'
    session['Great Britain'] = 'Jenson Button'
    session['Deutchland'] = 'Sebastian Vettel'
    session.save()
    print("Session ID: " + session.id)
    pprint(session)

    session.delete()
    print
    print("Delete session")
    print("Session ID: " + session.id)
    pprint(session)

    assert 'Suomi' not in session
    assert 'Great Britain' not in session
    assert 'Deutchland' not in session
    assert 'Russian' not in session
