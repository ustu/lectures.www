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

    print
    print("Check session")
    session2 = get_session(id=session.id)
    assert 'Suomi' in session2
    assert 'Great Britain' in session2
    assert 'Deutchland' in session2

    assert session2['Suomi'] == 'Kimi Räikkönen'
    assert session2['Great Britain'] == 'Jenson Button'
    assert session2['Deutchland'] == 'Sebastian Vettel'
    print("OK")
    print
    assert session2['Russian'] == 'Alexey Popov'
