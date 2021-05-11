# -*- coding: utf-8 -*-
from . import helpers

def get_hmm():
    """Get a thought."""
    return 'hmmm...2'


def hmm2():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())