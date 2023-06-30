/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    let brackets = {
        '(':')',
        '{':'}',
        '[':']'
    }
    for(const c of s){
        if(c in brackets){
            stack.push(c);
        }else{
            if(!stack.length){
                return false;
            }else{
                let previousOpening = stack.pop();
                if(brackets[previousOpening]!=c){
                    return false;
                }
            }
        }
    }
    return !stack.length;
};