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

    session2 = get_session(id=session.id)
    del session2['Suomi']
    session2['Great Britain'] = 'Lewis Hamilton'
    session2['Deutchland'] = 'Michael Schumacher'
    session2['España'] = 'Fernando Alonso'

    print
    print("Modified session")
    print("Session ID: " + session2.id)
    pprint(session2)

    session2.revert()

    print
    print("Revert session")
    print("Session ID: " + session2.id)
    pprint(session2)
