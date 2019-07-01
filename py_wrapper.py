from execjs import get
import os
import json

# from https://www.codementor.io/jstacoder/integrating-nodejs-python-how-to-write-cross-language-modules-pyexecjs-du107xfep
runtime = get('Node')

context = runtime.compile('''
    module.paths.push('%s');
    const dJSON = require('dirty-json');
    function fix_json(input_string){
        const r = dJSON.parse(input_string)
        return JSON.stringify(r);
    }
''' % os.path.join(os.path.dirname(__file__),'node_modules'))

def fix_json(input_string):
    """Both the input and output are strings"""
    return context.call('fix_json',input_string)

if __name__ == '__main__':
    with open('broken_json.txt') as f:
        string = f.read()
    result = fix_json(string)
    # now the string should be good json, can load with standard JSON library
    p = json.loads(result)
    print(p)