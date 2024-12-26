"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    fooziman = result.upper().replace("O", "0").replace("I", "1").replace("A", "@")
    result = []
    for i in fooziman:
        result.append(i)
    return result
