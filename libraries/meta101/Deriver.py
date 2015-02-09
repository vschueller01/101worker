import json
import os
import incremental101
from   .util          import diff, sourcetotarget, valuebykey


class Deriver(object):


    def __init__(self,
                 suffix,
                 callback,
                 key     =None,
                 getvalue=valuebykey,
                 dump    ={"problems" : {}}):
        self.key      = key
        self.suffix   = suffix
        self.callback = callback
        self.dump     = dump
        self.getvalue = getvalue


    def derive(self):
        diff(self.suffix, A=self.onfile, M=self.onfile, D=self.ondelete)
        return self.dump


    def rmdump(self, target):
        if target in self.dump["problems"]:
            del self.dump["problems"][target]


    def onfile(self, target, **kwargs):
        self.rmdump(target)

        try:
            matchesfile = sourcetotarget(kwargs["filename"]) + ".matches.json"
            with open(matchesfile) as f:
                matches = json.load(f)
            value = self.getvalue(self, matches)
        except Exception:
            return

        try:
            result = self.callback(value, target=target, **kwargs)
            if result is None:
                incremental101.deletefile(target)
            elif type(result) in [dict, list]:
                incremental101.writejson(target, result)
            else:
                incremental101.writefile(target, result)

        except Exception as e:
            self.dump["problems"][target] = str(e)


    def ondelete(self, target, **kwargs):
        self.rmdump(target)
        incremental101.deletefile(target)
