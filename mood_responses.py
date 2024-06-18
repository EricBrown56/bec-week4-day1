def mood_response(mood):
    '''The function returns a different response based on the moods "happy", "nervous", "sad", "excited", and "relaxed". If the mood is not recognized, the function returns "I don't recognize this mood.'''
    if mood == "happy":
        return '''
        ████████ ██   ██  █████  ████████ ███████      █████  ██     ██ ███████ ███████  ██████  ███    ███ ███████ ██ ██ 
            ██    ██   ██ ██   ██    ██    ██          ██   ██ ██     ██ ██      ██      ██    ██ ████  ████ ██      ██ ██ 
            ██    ███████ ███████    ██    ███████     ███████ ██  █  ██ █████   ███████ ██    ██ ██ ████ ██ █████   ██ ██ 
            ██    ██   ██ ██   ██    ██         ██     ██   ██ ██ ███ ██ ██           ██ ██    ██ ██  ██  ██ ██            
            ██    ██   ██ ██   ██    ██    ███████     ██   ██  ███ ███  ███████ ███████  ██████  ██      ██ ███████ ██ ██ 
    '''  
                                                                                                                  
                                
    elif mood == "nervous":
        return "Take a deep breath 3 times. You got this! Don't criticize yourself for those feelings: Instead, say, 'This is a normal, healthy response by my body to these circumstances, which are complicated, stressful, or difficult. It's OK to feel this way.'"
    elif mood == "sad":
        return "I am so sorry you feel sad. When I feel sad I say to myself, 'I am strong and resilient. I have made it through other challenges, and I will make it through this one. My depression does not define me. I have agency in my life, and depression does not need to control me.'"
    elif mood == "excited":
        return "That's great! I am excited for you. https://tenor.com/view/freak-out-oh-my-god-excited-omg-gif-10202717285280473443 Im this excited for you!"
    elif mood == "relaxed":
        return '''When you're relaxed, your body and mind experience many changes:
                                                Body
Your parasympathetic nervous system releases acetylcholine, a hormone that signals your body to conserve energy. Your blood pressure and heart rate decrease, your breathing slows, and your muscles relax. Your immune system may also function better.
                                                Mind
Your thought processes become slower and clearer, which can help with concentration, memory, decision making, and positive thinking. You may also have a more positive outlook on life and be better able to resist future stressors. 
'''
    else:
        return "I don't recognize this mood."