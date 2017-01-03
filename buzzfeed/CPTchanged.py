"""
File:       ICS3U_CPT.py

Purpose:    A pygame based quiz game for ICS3U
Author:
Created On:
"""


#initialize pygame screen
import pygame
pygame.init()

# define colours
RED = (255,0,0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (73,204,6)
CHARCOAL = (87,87,87)


def load_quizList(datafilename):
    """
    Access the data file and loads the contents into a list called qList[] in the following format:
    [[q1,a1,image1,optA,optB, optC, optD],[q2,a2,image1,optA,optB, optC, optD],...,[qN,aN,imageN,optA,optB, optC, optD]]

    This function operates under the assumption that the file that is being read (specified by the datafilename parameter)
    is of the format:

    10
    question1
    answer1
    imagefilename1
    question1 optionA
    question1 optionB
    question1 optionC
    question1 optionD
    question2
    answer2
    imagefilename2
    question2 optionA
    question2 optionB
    question2 optionC
    question2 optionD
    ...
    questionN
    answerN
    imagefilenameN
    questionN optionA
    questionN optionB
    questionN optionC
    questionN optionD

    The first line of the file (in this example 10) is the number of questions represented in the file.  All questions
    have 4 options (a,b,c,d)

    :param datafilename: string
    the filename of the file to load

    :return: qList[]
    """

   # your code here


    qList = []
    data_file = open(datafilename , "r")

    data_file.readline()

    for number_question in range (15):
        collection = []
        for i in range (7):
            collection.append((data_file.readline()).strip())

        qList.append(collection)

    return qList

def play_game(screen, game_data):
    """
    The playable quiz. For each question in game_data,
    presents each question to the screen, gets the response from the user, shows result, and goes next question

    :param screen: pygame screen object
    :param game_data: list object containing quiz data
    :return:
        game_state values - "results" or "quit": string
        score: int - the final total score of the user
        results_list: a list containing the results of each question, each element in the list is a three element list
        consisting of [correctAnswerLetter, playerAnswerLetter, pointsInt] i.e [['a','a',1],['d','b',0], ... ['a','c',0]]

    """

    # your code here
    # your code here
    done = False
    clock = pygame.time.Clock()
    question_index = 0
    advance_question = False
    response = ""
    score = 0
    score_update = 0
    question_state = 0

    while done == False:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit" , score

            else:
                if event.type == pygame.KEYUP:
                    if event.key != pygame.K_RETURN:
                        response = chr(event.key)
                        if response != "a" and response !="b" and response != "c" and response != "d":
                            response = ""

                    elif response != "":
                        if game_data[question_index][2].lower() == response.lower():
                            score_update = 1

                        advance_question = True

        if advance_question == True:
            score += score_update
            question_index += 1
            response = ""
            advance_question = False
            score_update = 0
        else:
            show_question_response(screen , game_data[question_index], response)

        if question_index >= len(game_data):
            done = True

        clock.tick(20)
        pygame.display.flip()


    return "final", score





def show_question_response(screen, q_data, user_response):
    """
    Shows the text for the question, options and user response to the screen

    :param screen: pygame screen object to display to
    :param q_data: list containing the info for the question to
    show in format [question_text,answer,imagefile, optionA, optionB,optionC, optionD]
    :param user_response: string -
    :return: None
    """




    # your code here
    screen.fill(WHITE)
    image = pygame.image.load(q_data[1]).convert()
    screen.blit(image, [0,0])

    question_text = pygame.font.SysFont(None, 40, True, False)
    the_question = question_text.render(q_data[0], True, BLACK)
    screen.blit(the_question, [10,500])

    option_text = pygame.font.SysFont(None, 30, True, False)

    y = 510
    for option in range (3,7):
        option_question = option_text.render(q_data[option], True, BLACK)
        y+= 30
        screen.blit (option_question, [20, y])

    screen.blit(question_text.render(user_response, True, RED), [671,498])
    screen.blit(question_text.render("_", True , BLACK), [670, 500])

def show_question_result(screen, answer, user_response):
    """
    Compare the correct answer to the user response and display the appropriate result


    :param screen: pygames screen object to draw to
    :param answer: string - the answer of the question
    :param user_response: string - the response of the user
    :return: int - value to update the score by (0 or 1)
    """
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit the function
                return "quit"

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return "quit"
            screen.fill(GREEN)



def show_welcome(screen):
    """
    Shows the welcome screen of the game in a pygame screen.
    Stops displaying when the user closes the screen or hits enter.

    :param screen: pygame screen object to display to
    :return: string: game_state values - "play"or "quit"
    """


    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit the function
                return "quit"

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return "play"

            # YOUR Welcome Screen code goes here
            screen.fill(GREEN)

            image_background = pygame.image.load("background.jpg").convert()
            image_background = pygame.transform.scale(image_background, (1100, 700))
            screen.blit(image_background, [0,0])

            question_text = pygame.font.SysFont(None, 50, True, False)
            the_question = question_text.render("This is Jason's CPT Press 'Enter' to Continue", True, WHITE)
            screen.blit(the_question, [120,350])



        clock.tick(20)
        pygame.display.flip()

def show_final_results(screen, score, out_of):
    """
   Shows the final score to the screen (with out of). i.e You're final score is 18/20
   Shows a final statement based on score i.e "Great Job", "Study Harder", "Nice Try"

    :param screen: pygame screen object to display to
    :param score: int - final user score
    :param out_of: int - number of questions

    :return: string: game_state values - "play"or "quit"
    """

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit the function
                return "quit"

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return "quit"


        # your code here
        screen.fill(WHITE)

        image_background = pygame.image.load("ending.jpg").convert()
        image_background = pygame.transform.scale(image_background, (1100, 700))
        screen.blit(image_background, [0,0])

        question_text = pygame.font.SysFont(None, 40, True, False)
        the_question = question_text.render("Your score is: " + str(score) + " / " + str(out_of), True, BLACK)
        screen.blit(the_question, [400,350])

        if score <=7:
            question_text = pygame.font.SysFont(None, 30, True, False)
            the_question = question_text.render("You FAILED", True, RED)
            screen.blit(the_question, [480,450])

        elif score == 15:

            question_text = pygame.font.SysFont(None, 30, True, False)
            the_question = question_text.render("You got Perfect", True, GREEN)
            screen.blit(the_question, [480,450])
        elif score <= 14:
            question_text = pygame.font.SysFont(None, 30, True, False)
            the_question = question_text.render("You did Okay", True, CHARCOAL)
            screen.blit(the_question, [480,450])


        clock.tick(20)
        pygame.display.flip()

def main():
    """
    The top function to control the overall game

    :return: None
    """

    # load data into quizList
    quizList = load_quizList("data.txt")
    size = [1100, 700]

    pyscreen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Fabrizzinator")

    #initialize the game state
    game_state = "start"

    while game_state != "quit":


        if game_state == "start":
             game_state = show_welcome(pyscreen)
        elif game_state == "play":
             game_state, score = play_game(pyscreen,quizList)
        elif game_state == "final":
            # show final screen
            game_state = show_final_results(pyscreen, score,len(quizList))

        else:
            pygame.quit()

main()