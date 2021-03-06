import sys
import json

sys.path.append('..')
import interpretRules

sys.path.append('../../libraries')
from service_api import *

sys.path.append('../../libraries/101meta')
import const101
import tools101

def main(data):
    print data
    data = expand_data(data)

    rules = json.load(open(const101.rulesDump))

    fpredicate_rules = interpretRules.group_fast_predicates(rules)


    interpretRules.apply_rules(data['data'], fpredicate_rules, lambda rule: rule['rule']['fpredicate'] == "technologies/fpredicate_generic_platform/import.py", append=True)

if __name__ == '__main__':
    print main({
        'type': 'files',
        'data': ['/tmp/antlrParser/contributions/antlrParser/src/main/java/org/softlang/company/features/Total.java']
    })

