from tkinter.messagebox import askyesno

answers = []

def submit():
    answers.append(askyesno(title='Survey',
                          message='Has your doctor ever said that you have a heart condition and that you should only do physical activity recommended by a doctor??'))
    answers.append(askyesno(title='Survey',
                          message='Do you feel pain in your chest when you do physical activity?'))
    answers.append(askyesno(title='Survey',
                          message='In the past month, have you had chest pain when you were not doing physical activity?'))
    answers.append(askyesno(title='Survey',
                          message='Do you lose your balance because of dizziness or do you ever lose consciousness?'))
    answers.append(askyesno(title='Survey',
                          message='Do you have a bone or joint problem that could be made worse by a change in your physical activity?'))
    answers.append(askyesno(title='Survey',
                          message='Is your doctor currently prescribing drugs (for example, water pills) for your blood pressure or heart condition?'))
    answers.append(askyesno(title='Survey',
                          message='Do you know of any other reason why you should not do physical activity?'))
    print('fg')
    if any(answers):
        return False
    return True