import random, os
from art import logo


#initialize global variable
CONT = True


def deal_card():
    '''Returns a random card from the deck.'''
    #11 acts as an ace. later logic dicates whether user will bust, if so, ace aces as 1
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(cards):
    '''Take list of cards and return the score.'''
    #accounting for ace in-game functionality
    #if user will bust due to ace being 11 then change ace to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    '''Determine the winner. u for user and c for computer.'''
    if u_score > 21 and c_score > 21:
        return "You went over. You lose 😤"
    elif u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 21:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    '''Main function of blackjack game.'''
    global CONT
    #initialize local variables
    u_cards = []
    c_cards = []

    #deal starting cards
    for _ in range(2):
        u_cards.append(deal_card())
        c_cards.append(deal_card())
    
    #start game loop
    while CONT:
        #compute score for user cards while also displaying a single card from computer to emulate a blackjack dealer
        u_score = calc_score(u_cards)
        c_score = calc_score(c_cards)
        print(logo)
        print(f'Your cards: {u_cards}, current score: {u_score}')
        print(f'Computer\'s first card: {c_cards[0]}')

        #if conditions met end game loop otherwise query for additional card
        if u_score == 21 or u_score > 21:
            os.system('clear')
            CONT = False
        else:
            more = input('\nType "yes" to get another card, type "no" to pass:\n ~ ')
            if more == 'yes':
                #print logo and clear screen to show newest set of cards
                os.system('clear')
                u_cards.append(deal_card())
            else:
                os.system('clear')
                cont = False

    #if computer has reached 21 or has more than a 17 card value then stop adding additional cards
    while c_score != 21 and c_score < 17:
        c_cards.append(deal_card())
        c_score = calc_score(c_cards)
    
    print(f'Your final hand: {u_cards}, final score: {u_score}')
    print(f'Computer\'s final hand: {c_cards}, final score: {c_score}')
    print(compare(u_score, c_score))


#initiate game functionality
try:
    while input('Do you want to play a game of Blackjack?\nType "yes" or "no":\n ~ ') == 'yes':
        os.system('clear')
        play_game()

except KeyboardInterrupt:
    print('\nSee you later.')