import json
import os
import subprocess
from  warnings   import warn
from .Phase      import Phase
from .Basics     import Basics
from .Predicates import Predicates
from .Fragments  import Fragments
from .Deriver    import Deriver


def getphase(key):
    phases = {
        "basics"     : Basics,
        "predicates" : Predicates,
        "fragments"  : Fragments,
    }
    if key not in phases:
        raise RuntimeError("invalid phase: {}".format(key))
    return phases[key]


def matchall(phasekey):
    with open(os.environ['rules101dump']) as f:
        rules = json.load(f)["results"]["rules"]
    return getphase(phasekey)(rules).run()


def derive(*args, **kwargs):
    return Deriver(*args, **kwargs).derive()


def runcommand(*args):
    try :
        return (0, subprocess.check_output(args))
    except subprocess.CalledProcessError as e:
        warn(e)
        return (e.returncode, e.output)
