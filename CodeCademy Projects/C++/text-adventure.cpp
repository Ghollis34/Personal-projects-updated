#include <iostream>

// This project was made following a series of open-ended questions
// For the adventure it is inspired by heist episodes of Brooklyn Nine-nine, the characters viewpoint will be that of the character Jake

int main() {
// The beginning will be an explanation into the story world
    std::cout << "You walk into the presinct excited for Haloween, albeit, running a bit late.\n";
    std::cout << "After walking past Captain Holt he gives you a hard time for being late to work\n";
    std::cout << "You want to get back at him for embarressing you infront of everyone\n\n";

    //This next step is the first set of choices, giving the user the options to select from as well as definining each choice
    char choice_one_path;
    char choice_two_path;
    char choice_three_path;
    //This for function is listed to make sure that the user is inputting the correct options, for which it gives them 3 chances to do so
    for (int i = 0; i < 3 && choice_one_path != 'A' && choice_one_path != 'B' && choice_one_path != 'C'; i++) {
        std::cout << "What do you do? (Note that the options are case sensitive)\n\n";
        std::cout << "A) Try to steal his Medal of Valor\n";
        std::cout << "B) Attempt to steal his watch\n";
        std::cout << "C) Sit down and do your boring police work\n\n";

        std::cin >> choice_one_path;
        std::cout << "\n\n";

    }

    if (choice_one_path== 'A') {
        std::cout << "You have decided to try and steal his Medal of Valor\n";

        //To try and continue down each storyline the logic tree will follow each answer

        std::cout << "To go about stealing his Medal of Valor, you need a plan\n";
        std::cout << "There are several ways that you can go about stealing it\n\n";

        for (int i = 0; i < 3 && choice_two_path != 'A' && choice_two_path != 'B' && choice_two_path != 'C'; i++) {
            std::cout << "A) You can climb into his air vent and steal it when he leaves his office\n";
            std::cout << "B) You can throw a smoke bomb into his office and try to lure him out, from there you can enter and steal it\n";
            std::cout << "C) You ask your team for help in saying that you will do their overtime if they help you steal it\n\n";

            std::cin >> choice_two_path;
            std::cout << "\n\n";
        }
        if (choice_two_path == 'A'){
            std::cout << "You head to supply room F and unscrew the vent\n";
            std::cout << "You follow the map that Charles gave to you to Holt's office\n";
            std::cout << "You find yourself above Holts office where he has found you out.\nYou have failed to steal his medal of Valor.\n";
            std::cout << "Game Over\n";
        }
        else if (choice_two_path == 'B'){
            std::cout << "You go and grab a smoke bomb from the gun room\n";
            std::cout << "You open up Holt's door and throw the bomb into it\n";
            std::cout << "Just as you planned he leaves his office, leaving his Medal of Valor unguarded!!\n\n";
            std::cout << "However\n\n";
            std::cout << "As he leaves his office, he simply turns and locks the door.\nThere is no other way in.\n You have failed to steal his Medal of Valor\n";
            std::cout << "Game Over\n";
        }
        else if (choice_two_path == 'C'){
            std::cout << "You gather the team together and give them a series of instructions, a plan so smart, nothing can go wrong\n";
            std::cout << "You hire royal babies to swarm the bullpen. One of the babies swipes Holt's key and he is so concerned about getting it back that he doesn't notice Terry stealing his phone. Charles dusts the phone for fingerprints, the greasiest smudges revealing the 4 numbers he uses the most, thus his passcode. You suspects, given Holt's age, his password is the same for everything.\n"; 
            std::cout << "You then get  arrested on purpose, drawing Holt into the interrogation room. Charles stuffs himself through Holt's window and opens the safe.\n";
            std::cout << "This is where you reveal that you got the squad's help by telling them you would do all their paperwork for the night. Since Holt is doing your paperwork, he also has to do all of the squad's paperwork as well.\n\n\n";
            std::cout << "Congratulations!\n You have successfully managed to steal the Medal of Valor!\n";
        }
    }
    else if (choice_one_path == 'B') {
        std::cout << "You are going to attempt to steal his watch\n";
        std::cout << "Which way should you go about stealing it?\n\n";

        for (int i = 0; i < 3 && choice_three_path != 'A' && choice_three_path != 'B' && choice_three_path != 'C'; i++) {
            std::cout << "A) You hire a pickpocket artist that you arrested to steal the watch for you\n";
            std::cout << "B) You ask Captain Holt if he'd just give the watch to you\n";
            std::cout << "C) You gather the squad and ask for their help, after all, why wouldn't they help you? Right?\n\n";

            std::cin >> choice_three_path;
            std::cout << "\n\n";
        }
        if (choice_three_path == 'A'){
            std::cout << "\"Fingers\" the pickpocket that you hired successfully steals Captain Holt's watch!\n";
            std::cout << "He asks to meet you at Shaw's pub\n";
            std::cout << "You arrive at the pub and Fingers is nowhere to be found! Who would have thought that the criminal you hired would steal from you?\n";
            std::cout << "Panicked, you head back to the precinct to tell Holt that you lost his watch\n";
            std::cout << "You find the squad and Holt waiting for you.\nConfused, you ask what's happening\n";
            std::cout << "You find out that this was Holt's plan all along, and that it was a Decoy watch that had been stolen.\n You have failed to steal his watch\n";
            std::cout << "Game Over\n";
        }
        if (choice_three_path == 'B') {
            std::cout << "You go up to Captain Holt and ask if he'll just give you the watch.\n";
            std::cout << "Much to your surprise, he does!\n";
            std::cout << "You have successfully stolen the watch!\nCongratulations!\n";
        }
    if (choice_three_path == 'C') {
        std::cout << "You gather the squad together\n";
        std::cout << "You ask the squad whether or not they will help you\n";
        std::cout << "They all start laughing at you, and will not help you this time\n";
        std::cout << "Out of options you try to steal the watch with no plan and you fail to do so\n";
        std::cout << "Game Over\n";
        }
    }
    else if (choice_one_path == 'C') {
        std::cout << "You question if you are feeling okay, choosing such a boring option\n";
        std::cout << "Game Over\n";
    }
    else {
        std::cout << "Your choice isn't an option, please try again.\n";
    }


}