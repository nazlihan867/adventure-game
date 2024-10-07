from game_utils import solve_riddle, end_game, enter_room
# Define the function greeting and welcome the user.
# Definiere die Funktion greeting und begrüße den Benutzer.
def greeting():
    print("Hello, welcome to 'The Lost Teasure Hunt'.")
# ("Hallo, willkommen bei 'Die verlorene Schatzsuche'.")    
    print("You will navigate through different rooms where you have to solve riddles to proceed. The goal is to find the lost treasure.")
# ("Du wirst durch verschiedene Räume navigiert, in denen du ein Rätsel lösen musst, um weiterzukommen. Das Ziel ist es, den verlorenen Schatz zu finden.")

    def main():
        greeting()
        rooms=[
            {
                "name":"dream world",
                "description":"A space for relaxation.",
                "riddle":{
                    "question":"At dawn I scream, please don't hit me. Can you guess me?",
                    "answer":"alarm clock"
                }
            },
            {
                "name": "office time",
                "description":"No matter whether it's computer, laptop or cell phone. You can connect with me invisibly.",
                "riddle":{
                    "question":"Paper moves in and out, words and images as if in a frenzy. Can you guess me?"
                    "answer": "Printer"
                }
            },
            {
                "name": "The treasure chamber",
                "description": "A shining treasure lies before you".
                "riddle":{
                    "question": "What is always in front of you but you can't see it?",
                    "answer":"the future"
                }
             }
           ]
           currentroom = 0
          while currentroom < len(rooms):
                room=rooms[currentroom]
                enter_room(room)
                if currentroom < len(rooms) -1:
                     user_input = input("Do you want to enter the next room? (yes/no) \n")
                     if user_input.strip().lower() != "yes":
                          end_game()
                          currentroom += 1
                          print("You found the treasure. Congrats!")
                          
                          
                          
                          
                          
                          
  main()