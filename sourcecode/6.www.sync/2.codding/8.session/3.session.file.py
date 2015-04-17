# -*- coding: utf-8 -*-
from pprint import pprint
from common import get_session

if '__main__' in __name__:
    """Test if the data is actually persistent across requests"""
    session = get_session(data_dir='./cache', type='file')
    session['Suomi'] = 'Kimi Räikkönen'
    session['Great Britain'] = 'Jenson Button'
    session['Deutchland'] = 'Sebastian Vettel'
    session.save()
    print("Session ID: " + session.id)
    pprint(session)

    session2 = get_session(id=session.id, data_dir='./cache', type='file')

    print
    print("File storage session")
    print("Session ID: " + session2.id)
    pprint(session2)
